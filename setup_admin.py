#!/usr/bin/env python
"""
Setup script to create admin user and initialize database
"""

from app import app
from models import db, User, BlogPost
from werkzeug.security import generate_password_hash
from datetime import datetime

def create_admin():
    """Create admin user"""
    print("Creating admin user...")
    
    email = input("Enter admin email (default: admin@lmnindustries.com): ") or "admin@lmnindustries.com"
    password = input("Enter admin password (default: admin123): ") or "admin123"
    
    with app.app_context():
        # Check if admin exists
        existing_admin = db.session.query(User).filter_by(email=email).first()
        if existing_admin:
            print(f"Admin user with email {email} already exists!")
            return
        
        admin = User(
            email=email,
            password=generate_password_hash(password),
            company_name='LMN Industries',
            country='India',
            is_admin=True
        )
        db.session.add(admin)
        db.session.commit()
        
        print(f"\n✅ Admin user created successfully!")
        print(f"Email: {email}")
        print(f"Password: {password}")
        print(f"\nLogin at: http://localhost:5000/client/login")
        print(f"Admin Panel: http://localhost:5000/admin")

def create_sample_blog_posts():
    """Create sample blog posts"""
    print("\nCreating sample blog posts...")
    
    with app.app_context():
        posts = [
            {
                'title': 'Understanding CNC Turning Precision: A Complete Guide',
                'slug': 'understanding-cnc-turning-precision',
                'category': 'CNC Technology',
                'content': '''<p>CNC turning is a manufacturing process where bars of material are held in a chuck and rotated while a tool is fed to the piece to remove material and create the desired shape.</p>
                
                <h3>What is Precision in CNC Turning?</h3>
                <p>Precision in CNC turning refers to the ability to manufacture components with extremely tight tolerances, typically ranging from ±0.01mm to ±0.001mm. This level of accuracy is crucial for industries like aerospace, medical devices, and automotive manufacturing.</p>
                
                <h3>Key Factors Affecting Precision</h3>
                <ul>
                    <li>Machine rigidity and stability</li>
                    <li>Tool quality and sharpness</li>
                    <li>Material properties</li>
                    <li>Environmental conditions</li>
                    <li>Operator skill and experience</li>
                </ul>
                
                <h3>Achieving High Precision</h3>
                <p>At LMN Industries, we achieve precision tolerances of ±0.01mm through state-of-the-art CNC machines, regular calibration, and skilled operators with decades of experience.</p>''',
                'meta_description': 'Learn about CNC turning precision, tolerances, and how to achieve high-accuracy manufacturing for industrial components.',
                'meta_keywords': 'CNC turning, precision machining, tight tolerances, manufacturing accuracy',
                'author': 'LMN Technical Team'
            },
            {
                'title': 'Export Guide: Shipping Precision Components Internationally',
                'slug': 'export-guide-shipping-precision-components',
                'category': 'Export Insights',
                'content': '''<p>Exporting precision-machined components requires careful planning, proper documentation, and specialized packaging to ensure products arrive in perfect condition.</p>
                
                <h3>Essential Export Documentation</h3>
                <ul>
                    <li>Commercial Invoice</li>
                    <li>Packing List</li>
                    <li>Certificate of Origin</li>
                    <li>Material Test Certificates (MTC)</li>
                    <li>Quality Inspection Reports</li>
                </ul>
                
                <h3>Packaging for International Shipping</h3>
                <p>We use VCI (Vapor Corrosion Inhibitor) paper, custom wooden crates, and moisture-proof packaging to protect components during transit. All wood packaging complies with ISPM 15 standards.</p>
                
                <h3>Customs and Compliance</h3>
                <p>Understanding HS codes, duty rates, and country-specific regulations is crucial for smooth customs clearance. Our export team handles all documentation and compliance requirements.</p>''',
                'meta_description': 'Complete guide to exporting precision machined components internationally, including documentation, packaging, and customs compliance.',
                'meta_keywords': 'export machining, international shipping, precision components export, customs compliance',
                'author': 'LMN Export Team'
            },
            {
                'title': 'ISO 9001:2015 Certification: What It Means for Quality',
                'slug': 'iso-9001-certification-quality-management',
                'category': 'Quality Standards',
                'content': '''<p>ISO 9001:2015 is the international standard for quality management systems (QMS). It helps organizations ensure they meet customer and regulatory requirements consistently.</p>
                
                <h3>Key Principles of ISO 9001</h3>
                <ul>
                    <li>Customer focus</li>
                    <li>Leadership commitment</li>
                    <li>Process approach</li>
                    <li>Continuous improvement</li>
                    <li>Evidence-based decision making</li>
                </ul>
                
                <h3>Benefits for Customers</h3>
                <p>When you work with an ISO 9001:2015 certified manufacturer like LMN Industries, you benefit from:</p>
                <ul>
                    <li>Consistent product quality</li>
                    <li>Reduced defect rates</li>
                    <li>Better communication</li>
                    <li>Reliable delivery schedules</li>
                    <li>Documented processes</li>
                </ul>''',
                'meta_description': 'Understanding ISO 9001:2015 certification and its importance in precision manufacturing quality management.',
                'meta_keywords': 'ISO 9001, quality management, manufacturing certification, quality standards',
                'author': 'LMN Quality Team'
            }
        ]
        
        for post_data in posts:
            existing_post = db.session.query(BlogPost).filter_by(slug=post_data['slug']).first()
            if not existing_post:
                post = BlogPost(**post_data, published=True)
                db.session.add(post)
        
        db.session.commit()
        print("✅ Sample blog posts created!")

def initialize_database():
    """Initialize database with all tables"""
    print("Initializing database...")
    
    with app.app_context():
        db.create_all()
        print("✅ Database initialized!")

def main():
    print("=" * 60)
    print("LMN Industries - Setup Script")
    print("=" * 60)
    print()
    
    # Initialize database
    initialize_database()
    
    # Create admin user
    create_admin()
    
    # Create sample blog posts
    create_sample = input("\nCreate sample blog posts? (y/n): ").lower()
    if create_sample == 'y':
        create_sample_blog_posts()
    
    print("\n" + "=" * 60)
    print("Setup Complete! 🎉")
    print("=" * 60)
    print("\nYou can now:")
    print("1. Run the application: python app.py")
    print("2. Access the website: http://localhost:5000")
    print("3. Login to admin panel: http://localhost:5000/admin")
    print()

if __name__ == '__main__':
    main()
