from django.conf import settings
from django.core.mail import send_mail

def send_reset_password_mail(email,token):
    subject='Reset Your Password'
    message=f'Hi, You recently requested a password reset. To complete the process, click the link below. http://127.0.0.1:8000/reset-password/{token}'
    email_from=settings.EMAIL_HOST_USER
    recipient_list=[email]
    print(recipient_list*100)
    send_mail(subject,message,email_from,recipient_list)
    return True

