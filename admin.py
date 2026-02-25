from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
from flask_login import login_required, current_user, login_user, logout_user
from functools import wraps
from werkzeug.security import check_password_hash
from datetime import datetime, timedelta
from models import db, User, Quote, Order, BlogPost, Newsletter
from sqlalchemy import func

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            flash('Access denied. Admin privileges required.')
            return redirect(url_for('admin.login'))
        return f(*args, **kwargs)
    return decorated_function

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated and current_user.is_admin:
        return redirect(url_for('admin.dashboard'))
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = db.session.query(User).filter_by(email=email, is_admin=True).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Invalid admin credentials or not an admin account')
    
    return render_template('admin/login.html')

@admin_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('admin.login'))

@admin_bp.route('/')
@login_required
@admin_required
def dashboard():
    # Statistics
    total_quotes = db.session.query(Quote).count()
    pending_quotes = db.session.query(Quote).filter_by(status='pending').count()
    total_orders = db.session.query(Order).count()
    total_clients = db.session.query(User).filter_by(is_admin=False).count()
    total_subscribers = db.session.query(Newsletter).count()
    
    # Recent quotes
    recent_quotes = db.session.query(Quote).order_by(Quote.created_at.desc()).limit(10).all()
    
    # Revenue calculation
    total_revenue = db.session.query(func.sum(Order.amount)).scalar() or 0
    
    # Monthly stats
    thirty_days_ago = datetime.utcnow() - timedelta(days=30)
    monthly_quotes = db.session.query(Quote).filter(Quote.created_at >= thirty_days_ago).count()
    monthly_orders = db.session.query(Order).filter(Order.created_at >= thirty_days_ago).count()
    
    return render_template('admin/dashboard.html',
                         total_quotes=total_quotes,
                         pending_quotes=pending_quotes,
                         total_orders=total_orders,
                         total_clients=total_clients,
                         total_subscribers=total_subscribers,
                         recent_quotes=recent_quotes,
                         total_revenue=total_revenue,
                         monthly_quotes=monthly_quotes,
                         monthly_orders=monthly_orders)

@admin_bp.route('/quotes')
@login_required
@admin_required
def quotes():
    status_filter = request.args.get('status', 'all')
    if status_filter == 'all':
        quotes = db.session.query(Quote).order_by(Quote.created_at.desc()).all()
    else:
        quotes = db.session.query(Quote).filter_by(status=status_filter).order_by(Quote.created_at.desc()).all()
    return render_template('admin/quotes.html', quotes=quotes, status_filter=status_filter)

@admin_bp.route('/quotes/<int:quote_id>')
@login_required
@admin_required
def quote_detail(quote_id):
    quote = db.session.query(Quote).filter_by(id=quote_id).first()
    if not quote:
        flash('Quote not found')
        return redirect(url_for('admin.quotes'))
    return render_template('admin/quote_detail.html', quote=quote)

@admin_bp.route('/quotes/<int:quote_id>/update-status', methods=['POST'])
@login_required
@admin_required
def update_quote_status(quote_id):
    quote = db.session.query(Quote).filter_by(id=quote_id).first()
    if not quote:
        flash('Quote not found')
        return redirect(url_for('admin.quotes'))
    new_status = request.form.get('status')
    quote.status = new_status
    db.session.commit()
    flash(f'Quote status updated to {new_status}')
    return redirect(url_for('admin.quote_detail', quote_id=quote_id))

@admin_bp.route('/orders')
@login_required
@admin_required
def orders():
    orders = db.session.query(Order).order_by(Order.created_at.desc()).all()
    return render_template('admin/orders.html', orders=orders)

@admin_bp.route('/clients')
@login_required
@admin_required
def clients():
    clients = db.session.query(User).filter_by(is_admin=False).order_by(User.created_at.desc()).all()
    return render_template('admin/clients.html', clients=clients)

@admin_bp.route('/blog')
@login_required
@admin_required
def blog_posts():
    posts = db.session.query(BlogPost).order_by(BlogPost.created_at.desc()).all()
    return render_template('admin/blog_posts.html', posts=posts)

@admin_bp.route('/blog/new', methods=['GET', 'POST'])
@login_required
@admin_required
def new_blog_post():
    if request.method == 'POST':
        title = request.form.get('title')
        slug = request.form.get('slug') or title.lower().replace(' ', '-')
        category = request.form.get('category')
        content = request.form.get('content')
        meta_description = request.form.get('meta_description')
        meta_keywords = request.form.get('meta_keywords')
        author = request.form.get('author')
        published = request.form.get('published') == 'on'
        
        post = BlogPost(
            title=title,
            slug=slug,
            category=category,
            content=content,
            meta_description=meta_description,
            meta_keywords=meta_keywords,
            author=author,
            published=published
        )
        db.session.add(post)
        db.session.commit()
        flash('Blog post created successfully')
        return redirect(url_for('admin.blog_posts'))
    
    return render_template('admin/blog_form.html', post=None)

@admin_bp.route('/blog/<int:post_id>/edit', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_blog_post(post_id):
    post = db.session.query(BlogPost).filter_by(id=post_id).first()
    if not post:
        flash('Blog post not found')
        return redirect(url_for('admin.blog_posts'))
    
    if request.method == 'POST':
        post.title = request.form.get('title')
        post.slug = request.form.get('slug')
        post.category = request.form.get('category')
        post.content = request.form.get('content')
        post.meta_description = request.form.get('meta_description')
        post.meta_keywords = request.form.get('meta_keywords')
        post.author = request.form.get('author')
        post.published = request.form.get('published') == 'on'
        
        db.session.commit()
        flash('Blog post updated successfully')
        return redirect(url_for('admin.blog_posts'))
    
    return render_template('admin/blog_form.html', post=post)

@admin_bp.route('/blog/<int:post_id>/delete', methods=['POST'])
@login_required
@admin_required
def delete_blog_post(post_id):
    post = db.session.query(BlogPost).filter_by(id=post_id).first()
    if not post:
        flash('Blog post not found')
        return redirect(url_for('admin.blog_posts'))
    db.session.delete(post)
    db.session.commit()
    flash('Blog post deleted successfully')
    return redirect(url_for('admin.blog_posts'))

@admin_bp.route('/newsletter')
@login_required
@admin_required
def newsletter_subscribers():
    subscribers = db.session.query(Newsletter).order_by(Newsletter.subscribed_at.desc()).all()
    return render_template('admin/newsletter.html', subscribers=subscribers)

@admin_bp.route('/analytics')
@login_required
@admin_required
def analytics():
    # Quote analytics
    quotes_by_country = db.session.query(
        Quote.country, func.count(Quote.id)
    ).group_by(Quote.country).all()
    
    quotes_by_material = db.session.query(
        Quote.material, func.count(Quote.id)
    ).group_by(Quote.material).all()
    
    # Monthly trends
    monthly_data = db.session.query(
        func.strftime('%Y-%m', Quote.created_at).label('month'),
        func.count(Quote.id).label('count')
    ).group_by('month').order_by('month').limit(12).all()
    
    return render_template('admin/analytics.html',
                         quotes_by_country=quotes_by_country,
                         quotes_by_material=quotes_by_material,
                         monthly_data=monthly_data)

@admin_bp.route('/settings', methods=['GET', 'POST'])
@login_required
@admin_required
def settings():
    if request.method == 'POST':
        # Handle settings update
        flash('Settings updated successfully')
        return redirect(url_for('admin.settings'))
    
    return render_template('admin/settings.html')
