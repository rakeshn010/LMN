# LMN Industries - Deployment Guide

## 🚀 Quick Start (Local Development)

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone or download the project**
```bash
cd lmn-industries
```

2. **Create virtual environment**
```bash
python -m venv venv
```

3. **Activate virtual environment**
- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

5. **Set up environment variables**
```bash
copy .env.example .env
# Edit .env file with your configuration
```

6. **Initialize database**
```bash
python
>>> from app import app, db
>>> with app.app_context():
...     db.create_all()
>>> exit()
```

7. **Run the application**
```bash
python app.py
```

8. **Access the website**
Open browser: http://localhost:5000

---

## 🌐 Railway Deployment

### Step 1: Prepare Your Project
Ensure these files exist:
- `requirements.txt` ✓
- `Procfile` ✓
- `runtime.txt` ✓
- `app.py` ✓

### Step 2: Create Railway Account
1. Go to https://railway.app
2. Sign up with GitHub

### Step 3: Deploy
1. Click "New Project"
2. Select "Deploy from GitHub repo"
3. Connect your repository
4. Railway will auto-detect Flask app

### Step 4: Configure Environment Variables
In Railway dashboard, add:
```
SECRET_KEY=your-production-secret-key-here
DATABASE_URL=postgresql://... (Railway provides this)
FLASK_ENV=production
```

### Step 5: Add PostgreSQL Database
1. In Railway project, click "New"
2. Select "Database" → "PostgreSQL"
3. Railway automatically sets DATABASE_URL

### Step 6: Deploy
Railway automatically deploys on git push.

---

## 🔧 Configuration

### Database Setup
- Development: SQLite (automatic)
- Production: PostgreSQL (recommended)

### Email Configuration (Optional)
For quote notifications, configure in `.env`:
```
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

### File Upload Configuration
- Max file size: 16MB
- Allowed formats: PDF, DWG, DXF
- Upload folder: `uploads/`

---

## 📝 Post-Deployment Checklist

### Essential Updates
1. **Update Contact Information**
   - Edit `templates/base.html` footer
   - Update phone numbers and email addresses
   - Add real company address

2. **Update Company Profile**
   - Replace placeholder text in About page
   - Add real certifications
   - Update statistics

3. **Add Google Maps**
   - Get Google Maps embed code
   - Add to `templates/contact.html`

4. **Configure WhatsApp**
   - Update WhatsApp number in floating button
   - Update in footer and contact page

5. **Add Company Logo**
   - Place logo in `static/images/logo.png`
   - Update logo in header

6. **SSL Certificate**
   - Railway provides automatic HTTPS
   - Ensure all links use HTTPS

7. **Google Analytics**
   - Add tracking code to `templates/base.html`

8. **Social Media Links**
   - Update LinkedIn, Twitter, Facebook URLs
   - Add in footer section

---

## 🎨 Customization

### Colors
Edit `static/css/style.css`:
```css
:root {
    --primary-blue: #0A2463;
    --accent-gold: #D4AF37;
    /* Modify as needed */
}
```

### Content
- Homepage: `templates/index.html`
- About: `templates/about.html`
- Services: `templates/services.html`

### Translations
Edit JSON files in `translations/` folder:
- `en.json` - English
- `de.json` - German
- `ar.json` - Arabic
- `fr.json` - French

---

## 🔐 Security

### Production Security Checklist
- [ ] Change SECRET_KEY in production
- [ ] Use PostgreSQL (not SQLite)
- [ ] Enable HTTPS (automatic on Railway)
- [ ] Set strong admin passwords
- [ ] Configure CORS if needed
- [ ] Regular database backups
- [ ] Monitor error logs

---

## 📊 Admin Features

### Create Admin User
```python
from app import app, db, User
from werkzeug.security import generate_password_hash

with app.app_context():
    admin = User(
        email='admin@lmnindustries.com',
        password=generate_password_hash('your-secure-password'),
        company_name='LMN Industries',
        country='India',
        is_admin=True
    )
    db.session.add(admin)
    db.session.commit()
```

---

## 🐛 Troubleshooting

### Database Issues
```bash
# Reset database
python
>>> from app import app, db
>>> with app.app_context():
...     db.drop_all()
...     db.create_all()
```

### Port Already in Use
Change port in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Module Not Found
```bash
pip install -r requirements.txt --upgrade
```

---

## 📞 Support

For technical support:
- Email: tech@lmnindustries.com
- Documentation: Check README.md

---

## 🎯 SEO Optimization

### Already Configured
- ✓ Meta tags
- ✓ Schema markup
- ✓ Sitemap.xml
- ✓ Robots.txt
- ✓ Semantic HTML
- ✓ Mobile responsive

### Additional Steps
1. Submit sitemap to Google Search Console
2. Set up Google Analytics
3. Configure Facebook Pixel (if needed)
4. Add structured data for products
5. Optimize images (compress, add alt text)

---

## 📈 Performance

### Optimization Tips
- Enable caching in production
- Use CDN for static files
- Compress images before upload
- Minify CSS/JS (optional)
- Enable gzip compression

---

Built with ❤️ for LMN Industries
