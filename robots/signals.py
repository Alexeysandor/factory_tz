from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save

from robots.models import Robots
from orders.models import Order


@receiver(post_save, sender=Robots)
def send_if_robot_available(sender, instance, **kwargs):
    subject = "Робот которого вы оформляли теперь в наличии!"
    message = ("Добрый день!\n"
               "Недавно вы интересовались нашим роботом модели"
               f"{instance.model}, версии {instance.version}.\n"
               "Этот робот теперь в наличии. Если вам подходит этот вариант "
               "- пожалуйста, свяжитесь с нами")
    customers = Order.objects.filter(
        robot_serial=instance.serial,
        waiting_list=True).prefetch_related('customer')
    for customer in customers:
        recipient_list = [customer.customer.email]
        send_mail(subject, message, 'mail@mail.mail', recipient_list)
        customer.waiting_list = False
        customer.save()
