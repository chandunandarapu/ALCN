"""
Third-party integrations module
- Stripe payment processing
- SendGrid email delivery
- SMS gateway (Twilio)
- Cloud storage (S3, GCS)
"""

from .stripe_integration import StripePaymentProcessor
from .email_integration import EmailService
from .storage_integration import CloudStorageHandler

__all__ = [
    'StripePaymentProcessor',
    'EmailService',
    'CloudStorageHandler',
]
