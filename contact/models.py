from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

@receiver(post_save, sender=Contact)
def send_contact_email(sender, instance, created, **kwargs):
    if created:
        subject = 'New Contact Form Submission'
        message = (
            f"Name: {instance.name}\n"
            f"Email: {instance.email}\n"
            f"Phone: {instance.phone_number}\n"
            f"Message: {instance.message}"
        )
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [instance.email]  # অথবা আপনার নির্দিষ্ট কোনো ইমেইল

        # Send email
        send_mail(subject, message, from_email, recipient_list)
