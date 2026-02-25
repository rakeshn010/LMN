# 🚂 Deploy to Railway - Step by Step Guide

## Quick Deploy in 5 Minutes! 🚀

Railway is the easiest way to deploy your Flask website. Follow these simple steps:

---

## ✅ Prerequisites

- [x] Your code is ready (it is!)
- [ ] GitHub account
- [ ] Railway account (free)

---

## 📋 Step-by-Step Instructions

### Step 1: Push Code to GitHub

**If you haven't already:**

```bash
# Initialize git (if not done)
git init

# Add all files
git add .

# Commit
git commit -m "LMN Industries website ready for deployment"

# Create repository on GitHub (github.com/new)
# Then connect and push:
git remote add origin https://github.com/YOUR_USERNAME/lmn-industries.git
git branch -M main
git push -u origin main
```

---

### Step 2: Create Railway Account

1. Go to: **https://railway.app**
2. Click **"Start a New Project"**
3. Sign up with GitHub (recommended)
4. Authorize Railway to access your repositories

---

### Step 3: Deploy Your Project

1. **Click "New Project"**
2. **Select "Deploy from GitHub repo"**
3. **Choose your repository** (lmn-industries)
4. Railway will automatically:
   - ✅ Detect it's a Flask app
   - ✅ Read `Procfile`
   - ✅ Install dependencies from `requirements.txt`
   - ✅ Start building

**Wait 2-3 minutes for build to complete** ⏳

---

### Step 4: Add PostgreSQL Database

1. In your Railway project dashboard
2. Click **"+ New"** → **"Database"** → **"Add PostgreSQL"**
3. Railway automatically:
   - ✅ Creates database
   - ✅ Sets `DATABASE_URL` environment variable
   - ✅ Connects to your app

---

### Step 5: Set Environment Variables

1. Click on your **web service** (not database)
2. Go to **"Variables"** tab
3. Click **"+ New Variable"**
4. Add these variables:

```
SECRET_KEY = <generate-random-key>
```

**To generate SECRET_KEY:**
```python
# Run this in Python:
import secrets
print(secrets.token_hex(32))
```

Copy the output and paste as SECRET_KEY value.

**Note:** `DATABASE_URL` is automatically set by Railway when you add PostgreSQL!

---

### Step 6: Generate Domain

1. Go to **"Settings"** tab
2. Scroll to **"Domains"**
3. Click **"Generate Domain"**
4. You'll get a URL like: `lmn-industries.up.railway.app`

**Your website is now LIVE!** 🎉

---

### Step 7: Initialize Database & Create Admin

**Option A: Using Railway CLI (Recommended)**

```bash
# Install Railway CLI
npm i -g @railway/cli

# Login
railway login

# Link to your project
railway link

# Run setup script
railway run python setup_admin.py
```

**Option B: Using Railway Dashboard**

1. Go to your project
2. Click on web service
3. Go to **"Deployments"** tab
4. Click on latest deployment
5. Click **"View Logs"**
6. You'll see the app running

Then manually create admin via Python shell:
```bash
railway run python
```

```python
from app import app
from models import db, User
from werkzeug.security import generate_password_hash

with app.app_context():
    db.create_all()
    admin = User(
        email='admin@lmnindustries.com',
        password=generate_password_hash('admin123'),
        company_name='LMN Industries',
        is_admin=True
    )
    db.session.add(admin)
    db.session.commit()
    print("Admin created!")
```

---

## 🎯 Your Live URLs

After deployment, you'll have:

- **Website**: `https://your-app.up.railway.app`
- **Admin Panel**: `https://your-app.up.railway.app/admin/login`

**Admin Credentials:**
- Email: admin@lmnindustries.com
- Password: admin123

**⚠️ Change password after first login!**

---

## 🔧 Railway Configuration Files

Your project already has these files configured:

### `Procfile`
```
web: gunicorn app:app
```

### `railway.json`
```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "gunicorn app:app",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

### `requirements.txt`
Already includes all dependencies including `gunicorn`

---

## 📊 Monitoring Your App

### View Logs
1. Go to Railway dashboard
2. Click your web service
3. Click **"Deployments"**
4. Click **"View Logs"**

### Check Metrics
1. Go to **"Metrics"** tab
2. See:
   - CPU usage
   - Memory usage
   - Network traffic
   - Request count

---

## 🔄 Updating Your Website

Whenever you make changes:

```bash
# Make your changes
# Then commit and push:
git add .
git commit -m "Updated content"
git push

# Railway automatically redeploys! 🚀
```

**No manual deployment needed!** Railway watches your GitHub repo.

---

## 💰 Railway Pricing

### Free Tier (Hobby Plan)
- ✅ $5 free credit per month
- ✅ Enough for small websites
- ✅ Automatic SSL
- ✅ Custom domains
- ✅ PostgreSQL included

### Paid Plans (if needed later)
- **Developer**: $20/month
- **Team**: $50/month
- Only pay for what you use

**Your website will likely stay free!** 🎉

---

## 🛠️ Troubleshooting

### Build Failed?

**Check logs:**
1. Go to Deployments
2. Click failed deployment
3. Read error message

**Common fixes:**
- Ensure `requirements.txt` is correct
- Check `Procfile` syntax
- Verify Python version in `runtime.txt`

### Database Connection Error?

**Fix:**
1. Ensure PostgreSQL is added
2. Check `DATABASE_URL` variable exists
3. Restart deployment

### App Not Starting?

**Check:**
1. View logs for errors
2. Ensure `gunicorn` is in requirements.txt
3. Verify `app:app` in Procfile

### Static Files Not Loading?

**Already configured!** Flask serves static files automatically.

---

## 🎨 Custom Domain (Optional)

### Add Your Own Domain

1. Buy domain from Namecheap, GoDaddy, etc.
2. In Railway:
   - Go to Settings → Domains
   - Click "Custom Domain"
   - Enter your domain: `www.lmnindustries.com`
3. Add DNS records at your domain registrar:
   ```
   Type: CNAME
   Name: www
   Value: your-app.up.railway.app
   ```
4. Wait 5-60 minutes for DNS propagation
5. SSL certificate automatically generated!

---

## 📱 Post-Deployment Checklist

After deploying:

- [ ] Visit your live website
- [ ] Test on mobile device
- [ ] Login to admin panel
- [ ] Change admin password
- [ ] Test contact form
- [ ] Test quote calculator
- [ ] Add blog posts
- [ ] Upload company photos
- [ ] Check all pages load correctly
- [ ] Test navigation menu
- [ ] Verify contact information displays
- [ ] Check footer links
- [ ] Test on different browsers

---

## 🚀 Quick Commands Reference

```bash
# Install Railway CLI
npm i -g @railway/cli

# Login to Railway
railway login

# Link to project
railway link

# View logs
railway logs

# Run commands
railway run python setup_admin.py

# Open in browser
railway open

# Check status
railway status
```

---

## 📈 Next Steps After Deployment

### 1. Content
- [ ] Add 3-5 blog posts via admin
- [ ] Upload company photos to `static/images/`
- [ ] Update service descriptions if needed

### 2. SEO
- [ ] Submit to Google Search Console
- [ ] Submit sitemap: `your-site.com/sitemap.xml`
- [ ] Create Google My Business listing
- [ ] Add Google Analytics

### 3. Marketing
- [ ] Share on social media
- [ ] Add to business directories
- [ ] Email existing customers
- [ ] Update email signatures with website link

### 4. Monitoring
- [ ] Set up uptime monitoring (UptimeRobot - free)
- [ ] Check Railway metrics weekly
- [ ] Monitor quote submissions
- [ ] Respond to contact forms promptly

---

## 🆘 Need Help?

### Railway Support
- Docs: https://docs.railway.app
- Discord: https://discord.gg/railway
- Twitter: @Railway

### Your App
- Check logs in Railway dashboard
- Review error messages
- Test locally first: `python app.py`

---

## ✅ Deployment Checklist

- [ ] Code pushed to GitHub
- [ ] Railway account created
- [ ] Project deployed from GitHub
- [ ] PostgreSQL database added
- [ ] SECRET_KEY environment variable set
- [ ] Domain generated
- [ ] Database initialized
- [ ] Admin user created
- [ ] Website accessible
- [ ] Admin panel working
- [ ] SSL certificate active (automatic)
- [ ] All pages loading correctly

---

## 🎉 Congratulations!

Your LMN Industries website is now live on the internet!

**Your Live Website:**
- 🌐 Website: `https://your-app.up.railway.app`
- 🔐 Admin: `https://your-app.up.railway.app/admin/login`

**Share it with the world!** 🚀

---

## 📞 Your Live Contact Info

Once deployed, customers can reach you at:
- 📱 Phone: +91 7795533453
- 📧 Email: lmnindustries1@gmail.com
- 📍 Location: Bengaluru, Karnataka
- 🕐 Hours: 9 AM - 11 PM Daily

**Your professional industrial website is live!** 🏭✨

---

*Deployment guide for LMN Industries*
*Built with Flask • Deployed on Railway*
