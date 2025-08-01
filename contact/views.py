from rest_framework import viewsets, status
from rest_framework.response import Response
from django.conf import settings
from django.core.mail import send_mail
from .models import Contact
from .serializers import ContactSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        contact = serializer.save()

        subject = 'New Contact Form Submission'
        message = (
            f"Name: {contact.name}\n"
            f"Email: {contact.email}\n"
            f"Phone: {contact.phone_number}\n"
            f"Message: {contact.message}"
        )
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [contact.email]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
