from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db, Order
from datetime import datetime
import os
import json

payment_bp = Blueprint('payment', __name__, url_prefix='/payment')

# Stripe configuration (add your keys in .env)
STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY', 'pk_test_your_key_here')
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY', 'sk_test_your_key_here')

@payment_bp.route('/checkout/<int:order_id>')
@login_required
def checkout(order_id):
    order = Order.query.get_or_404(order_id)
    if order.user_id != current_user.id:
        flash('Unauthorized access')
        return redirect(url_for('client_dashboard'))
    
    return render_template('payment/checkout.html', 
                         order=order,
                         stripe_public_key=STRIPE_PUBLIC_KEY)

@payment_bp.route('/process', methods=['POST'])
@login_required
def process_payment():
    try:
        order_id = request.form.get('order_id')
        payment_method = request.form.get('payment_method')
        
        order = Order.query.get_or_404(order_id)
        
        if payment_method == 'stripe':
            # Stripe payment processing
            # In production, integrate with Stripe API
            order.status = 'paid'
            db.session.commit()
            flash('Payment successful!')
            return redirect(url_for('client_dashboard'))
        
        elif payment_method == 'paypal':
            # PayPal payment processing
            order.status = 'paid'
            db.session.commit()
            flash('Payment successful!')
            return redirect(url_for('client_dashboard'))
        
        elif payment_method == 'bank_transfer':
            # Bank transfer instructions
            order.status = 'awaiting_payment'
            db.session.commit()
            return render_template('payment/bank_transfer.html', order=order)
        
        else:
            flash('Invalid payment method')
            return redirect(url_for('payment.checkout', order_id=order_id))
    
    except Exception as e:
        flash(f'Payment failed: {str(e)}')
        return redirect(url_for('payment.checkout', order_id=order_id))

@payment_bp.route('/success/<int:order_id>')
@login_required
def payment_success(order_id):
    order = Order.query.get_or_404(order_id)
    return render_template('payment/success.html', order=order)

@payment_bp.route('/webhook', methods=['POST'])
def webhook():
    # Handle payment gateway webhooks
    payload = request.get_data()
    
    try:
        # Process webhook data
        # Update order status based on payment confirmation
        return jsonify({'status': 'success'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
