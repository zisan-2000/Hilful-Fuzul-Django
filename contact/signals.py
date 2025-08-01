# contact/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact


def send_contact_email(contact):
    """
    Send an email notification when a new contact form is submitted.
    """
    subject = f"New Message from {contact.name}"
    message = (
        f"Name: {contact.name}\n"
        f"Email: {contact.email}\n"
        f"Phone: {contact.phone_number or 'N/A'}\n\n"
        f"Message:\n{contact.message}"
    )

    # Admin or site owner email - configurable from settings
    admin_email = getattr(settings, "CONTACT_RECEIVER_EMAIL", settings.DEFAULT_FROM_EMAIL)

    recipient_list = [admin_email]  
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        recipient_list,
        fail_silently=False
    )


@receiver(post_save, sender=Contact)
def contact_post_save(sender, instance, created, **kwargs):
    """
    Signal to send email after a new Contact is created.
    """
    if created:
        send_contact_email(instance)
