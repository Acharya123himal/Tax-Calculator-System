from django.conf import settings
from django.core.mail import send_mail

def send_feedback_mail(name,contact,email,message):
    subject='Feedback Received'
    message_admin=f'Feedback received from {name}, Phone: {contact}, email:{email}, message:{message}'
    message_client=f'Hi {name}, We have successfully received your feedback. We will get back to you as soon as we can. Thank you for your golden feedback.'
    email_from=settings.EMAIL_HOST_USER
    recipient_list=[email]
    print(recipient_list*100)
    send_mail(subject,message_admin,email_from,['himal.acharya12377@gmail.com'])
    send_mail(subject,message_client,email_from,recipient_list)
    return True
