#!/usr/bin/env python3
"""Initialize database for production deployment"""
from app import app, db
from models import User
from werkzeug.security import generate_password_hash

def init_database():
    with app.app_context():
        # Create all tables
        db.create_all()
        print("✅ Database tables created!")
        
        # Check if admin user exists
        admin = User.query.filter_by(email='admin@lmnindustries.com').first()
        if not admin:
            # Create default admin user
            admin = User(
                email='admin@lmnindustries.com',
                password=generate_password_hash('admin123'),
                company_name='LMN Industries',
                country='India',
                is_admin=True
            )
            db.session.add(admin)
            db.session.commit()
            print("✅ Admin user created!")
            print("   Email: admin@lmnindustries.com")
            print("   Password: admin123")
            print("   ⚠️  CHANGE THIS PASSWORD IMMEDIATELY!")
        else:
            print("✅ Admin user already exists")

if __name__ == '__main__':
    init_database()
