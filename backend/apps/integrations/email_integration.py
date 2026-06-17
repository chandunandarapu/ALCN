"""
Email service integration (SendGrid/SMTP)
"""
from django.core.mail import send_mail
from django.conf import settings


class EmailService:
    """Handle email operations"""
    
    @staticmethod
    def send_welcome_email(user_email, username):
        """Send welcome email"""
        subject = "Welcome to ALCN"
        message = f"Hello {username},\n\nWelcome to ALCN Ecosystem!"
        
        return send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user_email],
            fail_silently=False,
        )
    
    @staticmethod
    def send_invoice_email(recipient_email, invoice_number, invoice_url):
        """Send invoice email"""
        subject = f"Invoice {invoice_number} - ALCN"
        message = f"Your invoice is ready.\nView: {invoice_url}"
        
        return send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [recipient_email],
            fail_silently=False,
        )
    
    @staticmethod
    def send_proposal_email(recipient_email, proposal_title, proposal_url):
        """Send proposal email"""
        subject = f"New Proposal: {proposal_title} - ALCN"
        message = f"A new proposal has been created for you.\nView: {proposal_url}"
        
        return send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [recipient_email],
            fail_silently=False,
        )
