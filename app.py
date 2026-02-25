from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, session, send_file
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from datetime import datetime
import os
import json

# Import models and db
from models import db, User, Quote, Order, BlogPost, Newsletter

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-change-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///lmn_industries.db')
if app.config['SQLALCHEMY_DATABASE_URI'].startswith('postgres://'):
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config['SQLALCHEMY_DATABASE_URI'].replace('postgres://', 'postgresql://', 1)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Initialize extensions
db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'admin.login'  # Only admin login exists

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Register admin blueprint
from admin import admin_bp
app.register_blueprint(admin_bp)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Load translations
def load_translations(lang='en'):
    try:
        with open(f'translations/{lang}.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        with open('translations/en.json', 'r', encoding='utf-8') as f:
            return json.load(f)

@app.context_processor
def inject_translations():
    lang = session.get('language', 'en')
    return {'t': load_translations(lang), 'current_lang': lang, 'datetime': datetime}

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set-language/<lang>')
def set_language(lang):
    session['language'] = lang
    return redirect(request.referrer or url_for('index'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/services/<service_name>')
def service_detail(service_name):
    return render_template('service_detail.html', service=service_name)

@app.route('/machinery')
def machinery():
    return render_template('machinery.html')

@app.route('/export')
def export_page():
    return render_template('export.html')

@app.route('/industries')
def industries():
    return render_template('industries.html')

@app.route('/industries/<industry_name>')
def industry_detail(industry_name):
    return render_template('industry_detail.html', industry=industry_name)

@app.route('/quote-calculator')
def quote_calculator():
    return render_template('quote_calculator.html')

@app.route('/submit-quote', methods=['POST'])
def submit_quote():
    try:
        file_path = None
        if 'drawing_file' in request.files:
            file = request.files['drawing_file']
            if file.filename:
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{filename}")
                file.save(file_path)
        
        # Calculate estimated price (simplified logic)
        quantity = int(request.form.get('quantity', 0))
        material = request.form.get('material', '')
        base_price = {'stainless_steel': 50, 'mild_steel': 30, 'brass': 60, 'aluminum': 40}.get(material, 40)
        estimated_price = base_price * quantity * 0.8  # Bulk discount factor
        
        quote = Quote(
            name=request.form.get('name'),
            email=request.form.get('email'),
            company=request.form.get('company'),
            country=request.form.get('country'),
            phone=request.form.get('phone'),
            material=material,
            quantity=quantity,
            dimensions=request.form.get('dimensions'),
            tolerance=request.form.get('tolerance'),
            surface_finish=request.form.get('surface_finish'),
            description=request.form.get('description'),
            file_path=file_path,
            estimated_price=estimated_price
        )
        db.session.add(quote)
        db.session.commit()
        
        return jsonify({'success': True, 'estimated_price': estimated_price, 'quote_id': quote.id})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/blog')
def blog():
    posts = BlogPost.query.filter_by(published=True).order_by(BlogPost.created_at.desc()).all()
    return render_template('blog.html', posts=posts)

@app.route('/blog/<slug>')
def blog_post(slug):
    post = BlogPost.query.filter_by(slug=slug).first_or_404()
    return render_template('blog_post.html', post=post)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    # Handle contact form submission
    return jsonify({'success': True, 'message': 'Thank you for contacting us. We will respond within 24 hours.'})

@app.route('/newsletter-subscribe', methods=['POST'])
def newsletter_subscribe():
    try:
        email = request.form.get('email')
        if Newsletter.query.filter_by(email=email).first():
            return jsonify({'success': False, 'message': 'Email already subscribed'})
        
        newsletter = Newsletter(email=email)
        db.session.add(newsletter)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Successfully subscribed to newsletter'})
    except:
        return jsonify({'success': False, 'message': 'Subscription failed'}), 400

# Client portal removed - customers use contact form and quote calculator directly

@app.route('/sitemap.xml')
def sitemap():
    return send_file('static/sitemap.xml')

@app.route('/robots.txt')
def robots():
    return send_file('static/robots.txt')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)
