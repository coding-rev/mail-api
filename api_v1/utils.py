from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.contrib.auth import get_user_model
User = get_user_model()


class Util:
    def sendClientEmailFunc(data):
        context = {
            "company": data["company"],
            "name": data['name'],
            "email_to": data['email_to'],
            "message": data['message']
        }
        mailTemplate = get_template(
            "api_v1/email_client.html").render(context)
        email = EmailMultiAlternatives(
            subject=data['company'],
            body=' ',
            to=[data["email_to"]])
        email.attach_alternative(mailTemplate, "text/html")
        email.send()

    def sendAdminEmailFunc(data):
        context = {
            "company": data['company'],
            "name": data['name'],
            "email_from": data['email_from'],
            "email_to": data["email_to"],
            "message": data["message"]
        }
        mailTemplate = get_template(
            "api_v1/email_admin.html").render(context)
        email = EmailMultiAlternatives(
            subject=data["company"],
            body=' ',
            to=[data["email_to"]])
        email.attach_alternative(mailTemplate, "text/html")
        email.send()
