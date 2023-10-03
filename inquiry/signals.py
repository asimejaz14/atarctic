from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Inquiry


@receiver(post_save, sender=Inquiry)
def send_notification(sender, instance, created, **kwargs):
    # TODO: update fields
    if created:
        content = f"Name: {instance.name}\nEmail: {instance.email}\nMessage: {instance.message}"
        subject = f'Inquiry from {instance.name}'
        message = content
        email_from = 'your_email@example.com'
        recipient_list = ['recipient@example.com']

        send_mail(subject, message, email_from, recipient_list)
