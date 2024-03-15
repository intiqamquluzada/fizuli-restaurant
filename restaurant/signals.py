from django.dispatch import receiver
from django.db.models.signals import post_save
from restaurant.models import Reserve
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail


@receiver(post_save, sender=Reserve)
def reserve_sender(instance, created, **kwargs):
    subject = 'REZERV VAR'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['Fizuligrill@gmail.com']
    context = {
        "booking": instance,
    }
    html_message = render_to_string('letter.html', context)
    send_mail(subject, strip_tags(html_message), from_email, recipient_list)


