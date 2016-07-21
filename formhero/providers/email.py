from django.core.mail import send_mail
from django.core.mail.backends.base import BaseEmailBackend
from django.core.mail.backends.smtp import EmailBackend


class Backend(BaseEmailBackend):
    """
    Send email out, requires
    email host, port, user, password

    """

    def handle_data(self, form_obj, data):
        backend = EmailBackend(
            host=form_obj.config['EMAIL_HOST'],
            port=form_obj.config['EMAIL_PORT'],
            username=form_obj.config['EMAIL_USER'],
            password=form_obj.config['EMAIL_PASSWORD']
        )
        send_mail(
            subject='',
            message=data,
            from_email=form_obj.config['FORWARD_EMAIL'],
            recipient_list=[form_obj.config['TO_EMAIL']],
            auth_user=form_obj.config['EMAIL_USER'],
            auth_password=form_obj.config['EMAIL_PASSWORD'],
            connection=backend
        )
