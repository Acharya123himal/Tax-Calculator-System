from django.conf import settings
from django.core.mail import send_mail

def sendmail(email,subject,message):
    subject=subject
    message=message
    email_from=settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject,message,email_from,recipient_list)
    return True