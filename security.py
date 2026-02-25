"""
LMN Industries - Security Configuration
Comprehensive security measures for production deployment
"""
from flask import request, abort
from functools import wraps
import re
from datetime import datetime, timedelta

# Rate limiting storage (in production, use Redis)
rate_limit_storage = {}

def rate_limit(max_requests=5, window=60):
    """Rate limiting decorator to prevent abuse"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            ip = request.remote_addr
            now = datetime.now()
            
            # Clean old entries
            if ip in rate_limit_storage:
                rate_limit_storage[ip] = [
                    req_time for req_time in rate_limit_storage[ip]
                    if now - req_time < timedelta(seconds=window)
                ]
            else:
                rate_limit_storage[ip] = []
            
            # Check rate limit
            if len(rate_limit_storage[ip]) >= max_requests:
                abort(429)  # Too Many Requests
            
            rate_limit_storage[ip].append(now)
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def sanitize_input(text):
    """Sanitize user input to prevent XSS attacks"""
    if not text:
        return text
    
    # Remove potentially dangerous characters
    dangerous_patterns = [
        r'<script[^>]*>.*?</script>',
        r'javascript:',
        r'on\w+\s*=',
        r'<iframe',
        r'<object',
        r'<embed'
    ]
    
    for pattern in dangerous_patterns:
        text = re.sub(pattern, '', text, flags=re.IGNORECASE)
    
    return text

def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_password(password):
    """Validate password strength"""
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter"
    
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter"
    
    if not re.search(r'[0-9]', password):
        return False, "Password must contain at least one number"
    
    return True, "Password is strong"

def check_sql_injection(text):
    """Check for SQL injection attempts"""
    if not text:
        return False
    
    sql_patterns = [
        r"(\bUNION\b.*\bSELECT\b)",
        r"(\bDROP\b.*\bTABLE\b)",
        r"(\bINSERT\b.*\bINTO\b)",
        r"(\bDELETE\b.*\bFROM\b)",
        r"(\bUPDATE\b.*\bSET\b)",
        r"(--)",
        r"(;.*--)",
        r"(\bOR\b.*=.*)",
        r"('.*OR.*'.*=.*')"
    ]
    
    for pattern in sql_patterns:
        if re.search(pattern, str(text), re.IGNORECASE):
            return True
    
    return False

def admin_required(f):
    """Decorator to require admin access"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        from flask_login import current_user
        if not current_user.is_authenticated or not current_user.is_admin:
            abort(403)  # Forbidden
        return f(*args, **kwargs)
    return decorated_function

def secure_headers(response):
    """Add security headers to response"""
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self' 'unsafe-inline' https://fonts.googleapis.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data:;"
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    response.headers['Permissions-Policy'] = 'geolocation=(), microphone=(), camera=()'
    return response
