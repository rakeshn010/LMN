# Website Customization Guide

## 🎯 How to Add Your Original Company Details

This guide will help you replace placeholder content with your actual company information.

---

## 1. Company Information

### Update in `templates/base.html`

**Footer Section** (around line 50-80):
```html
<!-- Replace these placeholders -->
<li>📍 Industrial Area, India</li>  <!-- Your actual address -->
<li>📞 +91 XXX XXX XXXX</li>        <!-- Your phone number -->
<li>✉️ info@lmnindustries.com</li> <!-- Your email -->
<li>🕐 Mon-Sat: 9AM-6PM IST</li>    <!-- Your business hours -->
```

### Update in `templates/contact.html`

**Contact Information Card** (around line 50-90):
```html
<strong>Address</strong>
<p>Industrial Area<br>City, State 12345<br>India</p>
<!-- Replace with your actual address -->

<strong>Phone</strong>
<p>+91 XXX XXX XXXX</p>
<!-- Replace with your phone number -->

<strong>Email</strong>
<p>info@lmnindustries.com<br>sales@lmnindustries.com</p>
<!-- Replace with your email addresses -->
```

---

## 2. Company Name & Branding

### If you want to change "LMN Industries":

**Files to update:**
1. `templates/base.html` - Logo in header (line 20)
2. All page titles (search for "LMN Industries")
3. `app.py` - Email subjects and system messages
4. Footer copyright text

**Search and Replace:**
- Find: `LMN Industries`
- Replace: `Your Company Name`

---

## 3. About Page Content

### Update in `templates/about.html`

**Company Story** (around line 20):
```html
<h3>Our Story</h3>
<p>Founded in 1998, LMN Industries has grown...</p>
<!-- Replace with your actual company history -->
```

**Statistics** (around line 60-80):
```html
<span class="stat-number" data-count="25">0+</span>
<span class="stat-label">Years in Business</span>
<!-- Update with your actual years -->

<span class="stat-number" data-count="50">0+</span>
<span class="stat-label">Countries Served</span>
<!-- Update with your actual numbers -->
```

---

## 4. Services & Capabilities

### Update in `templates/services.html`

**Service Descriptions** (throughout the file):
- Update service capabilities
- Modify technical specifications
- Add/remove services as needed

**Materials** (around line 150):
```html
<h3>Metals</h3>
<p>Stainless Steel, Mild Steel, Aluminum...</p>
<!-- Add your actual materials -->
```

---

## 5. Machinery & Equipment

### Update in `templates/machinery.html`

**Machine Counts** (around line 20-100):
```html
<h3>CNC Turning Centers</h3>
<p><strong>15+ Machines</strong></p>
<!-- Update with your actual machine count -->
```

**Specifications**:
- Update diameter capacities
- Modify length capabilities
- Change tolerance specifications
- Update software names

---

## 6. Certifications

### Update Throughout Website

**Current Certifications:**
- ISO 9001:2015
- AS9100 (Aerospace)
- ISO 13485 (Medical)
- IATF 16949 (Automotive)

**To Update:**
1. `templates/about.html` - Certifications section
2. `templates/services.html` - Quality mentions
3. `templates/industries.html` - Industry standards

**Add your actual certifications or remove if not applicable**

---

## 7. Images & Media

### Add Company Photos

**Create folders and add images:**

```
static/images/
├── logo.png              # Your company logo
├── hero-bg.jpg          # Homepage hero background
├── about-team.jpg       # Team photo
├── facility-1.jpg       # Factory photos
├── facility-2.jpg
├── machinery-1.jpg      # Equipment photos
├── machinery-2.jpg
└── certifications/      # Certificate images
    ├── iso-9001.jpg
    └── other-certs.jpg
```

### Update Image References

**In templates, replace:**
```html
<!-- Add actual images -->
<img src="{{ url_for('static', filename='images/your-image.jpg') }}" alt="Description">
```

---

## 8. Social Media Links

### Update in `templates/base.html`

**Footer Social Links** (around line 55):
```html
<div class="social-links">
    <a href="https://facebook.com/yourpage">📘</a>
    <a href="https://linkedin.com/company/yourcompany">🔗</a>
    <a href="mailto:info@yourcompany.com">📧</a>
</div>
<!-- Replace with your actual social media URLs -->
```

---

## 9. Email Configuration

### Update in `app.py`

**Email Settings** (if you want email notifications):

```python
# Add at the top of app.py
import smtplib
from email.mime.text import MIMEText

# Configure email
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USERNAME = 'your-email@gmail.com'
SMTP_PASSWORD = 'your-app-password'
```

---

## 10. Google Maps

### Add Map to Contact Page

**In `templates/contact.html`** (around line 150):

Replace the placeholder with actual Google Maps embed:

```html
<iframe 
    src="https://www.google.com/maps/embed?pb=YOUR_EMBED_CODE"
    width="100%" 
    height="400" 
    style="border:0; border-radius: 16px;" 
    allowfullscreen="" 
    loading="lazy">
</iframe>
```

**To get embed code:**
1. Go to Google Maps
2. Search for your address
3. Click "Share" → "Embed a map"
4. Copy the iframe code

---

## 11. SEO & Analytics

### Update Meta Tags

**In each template file:**
```html
{% block meta_description %}
Your actual company description here
{% endblock %}

{% block meta_keywords %}
your, actual, keywords, here
{% endblock %}
```

### Add Google Analytics

**In `templates/base.html`** (before `</head>`):
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

---

## 12. Blog Content

### Add Blog Posts via Admin Panel

1. Go to: http://localhost:5000/admin/login
2. Login with admin credentials
3. Navigate to "Blog" section
4. Click "New Post"
5. Fill in:
   - Title
   - Slug (URL-friendly)
   - Category
   - Content (HTML supported)
   - Meta description
   - Keywords
   - Author name
6. Check "Published" to make it live
7. Click "Create Post"

**Recommended First Posts:**
- Company introduction
- Service capabilities overview
- Quality standards explanation
- Industry expertise showcase
- Customer success story

---

## 13. Pricing & Quote Calculator

### Update Base Prices

**In `app.py`** (around line 90):
```python
base_price = {
    'stainless_steel': 50,  # Update with your actual pricing
    'mild_steel': 30,
    'brass': 60,
    'aluminum': 40
}.get(material, 40)
```

---

## 14. Legal Pages

### Create Additional Pages

**Add these files in `templates/`:**

1. **privacy-policy.html** - Privacy policy
2. **terms-of-service.html** - Terms and conditions
3. **shipping-policy.html** - Shipping information
4. **return-policy.html** - Return/refund policy

**Update footer links in `templates/base.html`**

---

## 15. Database Customization

### Update Admin User

**Run this to change admin credentials:**
```bash
python setup_admin.py
```

Enter your preferred:
- Admin email
- Admin password

---

## 16. Production Configuration

### Before Deploying

**Update in `app.py`:**
```python
# Change SECRET_KEY
app.config['SECRET_KEY'] = 'your-secure-random-key-here'

# Use environment variables
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['DATABASE_URL'] = os.environ.get('DATABASE_URL')
```

**Generate secure key:**
```python
import secrets
print(secrets.token_hex(32))
```

---

## 17. Quick Checklist

Before going live, update:

- [ ] Company name and logo
- [ ] Contact information (phone, email, address)
- [ ] Business hours
- [ ] About page content
- [ ] Service descriptions
- [ ] Machinery specifications
- [ ] Certifications
- [ ] Social media links
- [ ] Google Maps location
- [ ] Pricing in quote calculator
- [ ] Admin credentials
- [ ] Add company photos
- [ ] Create 3-5 blog posts
- [ ] Add Google Analytics
- [ ] Update meta descriptions
- [ ] Test contact form
- [ ] Test quote calculator
- [ ] Review all pages on mobile
- [ ] Change SECRET_KEY for production

---

## 18. Testing Checklist

After customization:

- [ ] All links work correctly
- [ ] Contact form sends properly
- [ ] Quote calculator calculates correctly
- [ ] Admin panel accessible
- [ ] Blog posts display properly
- [ ] Mobile responsive on all pages
- [ ] Images load correctly
- [ ] Social media links work
- [ ] Google Maps displays
- [ ] Newsletter subscription works

---

## 19. Content Writing Tips

### Homepage Hero
- Keep it concise (10-15 words)
- Focus on main value proposition
- Include a clear call-to-action

### Service Descriptions
- Start with benefits
- Include technical specifications
- Add real-world applications
- Use bullet points for clarity

### About Page
- Tell your story authentically
- Highlight unique strengths
- Include team/facility photos
- Show certifications prominently

### Blog Posts
- Write 800-1500 words
- Use clear headings
- Include images/diagrams
- Add internal links
- Optimize for SEO

---

## 20. Need Help?

If you need assistance with customization:

1. **Content Writing**: Consider hiring a technical writer
2. **Photography**: Professional facility photos recommended
3. **SEO**: Consult with SEO specialist
4. **Design**: Minor tweaks can be made in `static/css/style.css`

---

## Quick Start Commands

```bash
# Start the server
python app.py

# Access website
http://localhost:5000

# Access admin panel
http://localhost:5000/admin/login

# Setup new admin user
python setup_admin.py
```

---

**Your professional website is ready for customization!** 🎉

Simply follow this guide to replace placeholder content with your actual company information.
