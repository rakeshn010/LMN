# 🚀 Deploy to Railway - Complete Guide

## Quick Deploy (5 Minutes)

### Step 1: Push to GitHub

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - LMN Industries Website"

# Create GitHub repository and push
git remote add origin https://github.com/YOUR_USERNAME/lmn-industries.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy to Railway

1. **Go to Railway**: https://railway.app
2. **Sign up/Login** with GitHub
3. **Click "New Project"**
4. **Select "Deploy from GitHub repo"**
5. **Choose your repository**: `lmn-industries`
6. **Railway will auto-detect** Flask and start deploying

### Step 3: Add PostgreSQL Database

1. In your Railway project, click **"New"**
2. Select **"Database"** → **"PostgreSQL"**
3. Railway automatically connects it to your app
4. DATABASE_URL is set automatically

### Step 4: Set Environment Variables

In Railway dashboard, go to **Variables** and add:

```
SECRET_KEY=your-super-secret-production-key-here-change-this
FLASK_ENV=production
COMPANY_EMAIL=info@lmnindustries.com
COMPANY_PHONE=+91-XXXXXXXXXX
COMPANY_WHATSAPP=+91-XXXXXXXXXX
```

Optional (for email notifications):
```
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

Optional (for analytics):
```
GOOGLE_ANALYTICS_ID=G-XXXXXXXXXX
FACEBOOK_PIXEL_ID=XXXXXXXXXX
```

Optional (for payments):
```
STRIPE_PUBLIC_KEY=pk_live_xxxxx
STRIPE_SECRET_KEY=sk_live_xxxxx
```

### Step 5: Deploy!

Railway will automatically deploy. Wait 2-3 minutes.

Your site will be live at: `https://your-app-name.up.railway.app`

---

## Post-Deployment Setup

### 1. Create Admin User

Access your Railway app's terminal or use Python shell:

```python
from app import app, db, User
from werkzeug.security import generate_password_hash

with app.app_context():
    admin = User(
        email='admin@lmnindustries.com',
        password=generate_password_hash('YourSecurePassword123!'),
        company_name='LMN Industries',
        country='India',
        is_admin=True
    )
    db.session.add(admin)
    db.session.commit()
    print("Admin user created!")
```

### 2. Add Custom Domain (Optional)

1. In Railway project, go to **Settings**
2. Click **"Generate Domain"** for free subdomain
3. Or add your custom domain:
   - Click **"Custom Domain"**
   - Enter your domain: `www.lmnindustries.com`
   - Add DNS records as shown

### 3. Enable HTTPS

Railway provides automatic HTTPS. No configuration needed!

---

## Alternative Deployment Options

### Deploy to Heroku

```bash
# Install Heroku CLI
# Login
heroku login

# Create app
heroku create lmn-industries

# Add PostgreSQL
heroku addons:create heroku-postgresql:mini

# Set environment variables
heroku config:set SECRET_KEY=your-secret-key
heroku config:set FLASK_ENV=production

# Deploy
git push heroku main

# Open app
heroku open
```

### Deploy to Render

1. Go to https://render.com
2. Click "New" → "Web Service"
3. Connect GitHub repository
4. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Add PostgreSQL database
6. Set environment variables
7. Deploy!

### Deploy to PythonAnywhere

1. Upload files to PythonAnywhere
2. Create virtual environment
3. Install requirements
4. Configure WSGI file
5. Set up database
6. Reload web app

---

## Monitoring & Maintenance

### Check Logs

**Railway:**
- Go to your project
- Click "Deployments"
- View logs in real-time

**Heroku:**
```bash
heroku logs --tail
```

### Database Backups

**Railway:**
- Automatic backups included
- Manual backup: Use Railway CLI

**Heroku:**
```bash
heroku pg:backups:capture
heroku pg:backups:download
```

### Update Application

```bash
# Make changes
git add .
git commit -m "Update description"
git push origin main

# Railway auto-deploys on push
# Heroku: git push heroku main
```

---

## Performance Optimization

### Enable Caching

Add to `app.py`:
```python
from flask_caching import Cache
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
```

### Compress Responses

```bash
pip install flask-compress
```

Add to `app.py`:
```python
from flask_compress import Compress
Compress(app)
```

### CDN for Static Files

Use Cloudflare or AWS CloudFront for static assets.

---

## Security Checklist

- [x] SECRET_KEY is strong and unique
- [x] DEBUG = False in production
- [x] HTTPS enabled (automatic on Railway)
- [x] Database credentials secure
- [x] File upload validation
- [x] CSRF protection enabled
- [x] SQL injection prevention (SQLAlchemy)
- [x] XSS protection
- [ ] Set up firewall rules
- [ ] Enable rate limiting
- [ ] Regular security updates

---

## Troubleshooting

### App Won't Start

Check logs for errors:
```bash
# Railway: View in dashboard
# Heroku: heroku logs --tail
```

Common issues:
- Missing environment variables
- Database connection failed
- Port binding issues

### Database Connection Error

Ensure DATABASE_URL is set correctly:
```bash
# Railway: Automatic
# Heroku: heroku config:get DATABASE_URL
```

### Static Files Not Loading

Check:
- Files are in `static/` folder
- Paths use `url_for('static', filename='...')`
- Permissions are correct

---

## Success! 🎉

Your website is now live and accessible worldwide!

**Next Steps:**
1. Test all features
2. Add real content and images
3. Set up Google Analytics
4. Submit sitemap to Google Search Console
5. Start marketing!

**Admin Panel:** `https://your-domain.com/admin`
**Website:** `https://your-domain.com`

---

## Support

Need help? Check:
- Railway Docs: https://docs.railway.app
- Flask Docs: https://flask.palletsprojects.com
- Project README.md

---

Built with ❤️ for LMN Industries
