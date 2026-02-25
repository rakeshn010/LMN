# LMN Industries - Global Precision CNC Manufacturing Website

## 🏭 Enterprise Industrial B2B Platform

A world-class, production-ready website for LMN Industries - showcasing precision CNC turning, lathe works, and custom machining capabilities to international markets.

## ✨ Complete Feature Set

### 🌐 Multi-Page Website (10+ Pages)
- **Homepage** - Hero, stats, services, industries, testimonials
- **About Us** - Company story, infrastructure, certifications
- **Services** - 6 detailed service offerings with specifications
- **Machinery** - Equipment showcase with technical specs
- **Export** - International markets, compliance, packaging
- **Industries** - 8 industry sectors with detailed pages
- **Quote Calculator** - AI-powered quotation system
- **Blog** - SEO-optimized articles and insights
- **Contact** - Multi-channel contact options
- **Client Portal** - Secure login, order tracking, dashboard

### 🎯 Advanced Features
- ✅ **Admin Dashboard** - Complete management system
- ✅ **AI Smart Quotation** - Instant price estimates with file upload
- ✅ **Client Portal** - Order tracking, invoices, production status
- ✅ **Multi-Language** - English, German, Arabic, French
- ✅ **Dark/Light Mode** - User preference toggle
- ✅ **Payment Integration** - Stripe, PayPal, Bank Transfer ready
- ✅ **Email Notifications** - Automated quote confirmations
- ✅ **Analytics Dashboard** - Business insights and metrics
- ✅ **Blog Management** - Full CMS for content
- ✅ **Newsletter System** - Subscriber management
- ✅ **SEO Optimized** - Meta tags, schema, sitemap
- ✅ **Mobile Responsive** - Perfect on all devices
- ✅ **Security** - CSRF, XSS, SQL injection protection

### 🎨 Premium Design
- Industrial corporate aesthetic (dark blue + metallic grey + gold)
- Smooth animations and transitions
- Professional typography (Inter font)
- Clean, modern UI/UX
- Touch-friendly mobile interface
- Floating action buttons (WhatsApp, Quote)

## 🚀 Quick Start

### Option 1: Automated Setup (Recommended)

**Windows:**
```bash
start.bat
```

**Mac/Linux:**
```bash
chmod +x start.sh
./start.sh
```

### Option 2: Manual Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Setup admin user and database
python setup_admin.py

# Run application
python app.py
```

Then open: **http://localhost:5000**

## 📊 Admin Panel

### Create Admin User

```bash
python setup_admin.py
```

Default credentials:
- Email: `admin@lmnindustries.com`
- Password: `admin123`

Access admin panel: **http://localhost:5000/admin**

### Admin Features
- 📊 Dashboard with analytics
- 💼 Quote management
- 📦 Order tracking
- 👥 Client management
- 📝 Blog post editor
- 📧 Newsletter subscribers
- 📈 Business analytics
- ⚙️ Settings management

## 🌐 Deploy to Production

### Railway (Recommended - 5 Minutes)

1. **Push to GitHub**
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/lmn-industries.git
git push -u origin main
```

2. **Deploy to Railway**
- Go to https://railway.app
- Sign up with GitHub
- Click "New Project" → "Deploy from GitHub repo"
- Select your repository
- Add PostgreSQL database
- Set environment variables (see DEPLOY_NOW.md)
- Deploy automatically!

Your site will be live at: `https://your-app.up.railway.app`

**Detailed deployment guide:** See `DEPLOY_NOW.md`

### Alternative Platforms
- Heroku
- Render
- PythonAnywhere
- AWS Elastic Beanstalk
- DigitalOcean App Platform
- Google Cloud Run

## 🔧 Configuration

### Environment Variables

Create `.env` file:

```env
# Required
SECRET_KEY=your-super-secret-key-here
DATABASE_URL=postgresql://user:pass@host:port/db

# Optional - Email
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password

# Optional - Analytics
GOOGLE_ANALYTICS_ID=G-XXXXXXXXXX
FACEBOOK_PIXEL_ID=XXXXXXXXXX

# Optional - Payments
STRIPE_PUBLIC_KEY=pk_live_xxxxx
STRIPE_SECRET_KEY=sk_live_xxxxx

# Company Info
COMPANY_EMAIL=info@lmnindustries.com
COMPANY_PHONE=+91-XXXXXXXXXX
COMPANY_WHATSAPP=+91-XXXXXXXXXX
```

## 📁 Project Structure

```
lmn-industries/
├── app.py                 # Main Flask application
├── admin.py              # Admin dashboard
├── payment.py            # Payment integration
├── config.py             # Configuration
├── setup_admin.py        # Setup script
├── requirements.txt      # Dependencies
├── Procfile             # Deployment config
├── static/
│   ├── css/style.css    # Styles
│   ├── js/main.js       # JavaScript
│   ├── images/          # Images
│   ├── robots.txt       # SEO
│   └── sitemap.xml      # SEO
├── templates/
│   ├── base.html        # Master template
│   ├── index.html       # Homepage
│   ├── admin/           # Admin templates
│   └── ...              # Other pages
├── translations/        # Multi-language
├── uploads/            # File uploads
└── docs/               # Documentation
```

## 🎯 Target Markets

### Primary Countries
- 🇺🇸 USA - Automotive, Aerospace, Medical
- 🇩🇪 Germany - Industrial Machinery
- 🇦🇪 UAE - Oil & Gas, Construction
- 🇬🇧 UK - Medical Devices, Electronics
- 🇨🇦 Canada - Heavy Engineering, Mining
- 🇦🇺 Australia - Mining Equipment

### Industries
- Automotive (OEM & Tier-1)
- Aerospace (Aircraft components)
- Oil & Gas (Drilling equipment)
- Medical (Surgical instruments)
- Electrical (Connectors, terminals)
- Construction (Heavy machinery)
- Heavy Engineering
- Electronics

## 📈 SEO Features

- ✅ Meta tags on all pages
- ✅ Schema.org markup
- ✅ Sitemap.xml
- ✅ Robots.txt
- ✅ Semantic HTML5
- ✅ Mobile-friendly
- ✅ Fast loading
- ✅ Clean URLs
- ✅ Alt text ready
- ✅ Open Graph tags

## 🔒 Security

- Password hashing (Werkzeug)
- CSRF protection (Flask-WTF)
- SQL injection prevention (SQLAlchemy)
- XSS protection
- Secure file uploads
- Session security
- Environment variables
- HTTPS ready

## 📱 Mobile Optimization

- Responsive design (mobile-first)
- Touch-friendly buttons
- Hamburger navigation
- Optimized images
- Fast loading
- Swipe gestures ready

## 🛠 Tech Stack

- **Backend**: Python Flask 3.0
- **Database**: SQLite (dev) / PostgreSQL (prod)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS
- **Authentication**: Flask-Login
- **Forms**: Flask-WTF
- **Email**: Flask-Mail
- **Deployment**: Railway, Heroku, Render

## 📚 Documentation

- **README.md** - This file
- **QUICKSTART.md** - 5-minute setup guide
- **DEPLOYMENT.md** - Detailed deployment instructions
- **DEPLOY_NOW.md** - Railway deployment guide
- **PROJECT_OVERVIEW.md** - Complete feature documentation

## 🎓 Customization

### Update Colors
Edit `static/css/style.css`:
```css
:root {
    --primary-blue: #0A2463;
    --accent-gold: #D4AF37;
}
```

### Add Content
- Homepage: `templates/index.html`
- About: `templates/about.html`
- Services: `templates/services.html`

### Add Languages
Create JSON file in `translations/`:
```json
{
    "nav": {
        "home": "Home",
        ...
    }
}
```

## 🐛 Troubleshooting

### Port Already in Use
Change port in `app.py`:
```python
app.run(port=5001)
```

### Database Issues
Reset database:
```bash
python
>>> from app import app, db
>>> with app.app_context():
...     db.drop_all()
...     db.create_all()
```

### Module Not Found
```bash
pip install -r requirements.txt --upgrade
```

## 📞 Support

For technical support:
- Check documentation files
- Review error logs
- Contact: tech@lmnindustries.com

## 🎉 Success Metrics

### Target Performance
- Page Load: < 3 seconds
- Lighthouse Score: > 90
- Mobile Friendly: Yes
- SEO Score: > 95

### Business Goals
- Generate international B2B leads
- Attract bulk industrial clients
- Showcase manufacturing capacity
- Position as ISO-certified manufacturer
- Ready for global exports

## 📄 License

Proprietary - LMN Industries

## 🙏 Acknowledgments

Built with precision and care for LMN Industries - Your trusted partner in precision manufacturing.

---

**Ready to deploy?** See `DEPLOY_NOW.md` for step-by-step instructions!

**Need help?** Check `QUICKSTART.md` for quick setup guide!

---

© 2026 LMN Industries. All rights reserved.

