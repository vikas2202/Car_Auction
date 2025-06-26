from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Auction

@receiver(post_save, sender=Auction)
def send_winner_email(sender, instance, **kwargs):
    if instance.end_time <= timezone.now() and instance.winner:
        subject = "🎉 You Won the Auction!"
        message = f"Hi {instance.winner.username},\n\nYou won the auction for {instance.car.name}.\nVisit your dashboard for details."
        send_mail(subject, message, 'admin@carauction.com', [instance.winner.email])
