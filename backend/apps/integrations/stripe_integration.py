"""
Stripe payment processing integration
"""
import stripe
from django.conf import settings


class StripePaymentProcessor:
    """Handle Stripe payment operations"""
    
    def __init__(self):
        stripe.api_key = settings.STRIPE_SECRET_KEY
    
    def create_payment_intent(self, amount, invoice_id):
        """Create a Stripe payment intent"""
        try:
            intent = stripe.PaymentIntent.create(
                amount=int(amount * 100),  # Stripe uses cents
                currency='inr',
                metadata={'invoice_id': invoice_id}
            )
            return intent
        except stripe.error.StripeError as e:
            return None
    
    def confirm_payment(self, payment_intent_id):
        """Confirm a Stripe payment"""
        try:
            intent = stripe.PaymentIntent.retrieve(payment_intent_id)
            return intent.status == 'succeeded'
        except stripe.error.StripeError as e:
            return False
