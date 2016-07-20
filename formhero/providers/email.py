from django.core.mail import send_mail
from django.core.mail.backends.base import BaseEmailBackend
from django.core.mail.backends.smtp import EmailBackend


class Backend(BaseEmailBackend):
    TO_EMAIL = 'company.email@example.com'
    """
    Send email out, requires
    email host, port, user, password

    """

    def handle_data(self, form_obj, data):
        backend = EmailBackend(
            host=form_obj.config['EMAIL_HOST'],
            port=form_obj.config['EMAIL_PORT'],
            username=form_obj.config['HOST_USER'],
            password=form_obj.config['HOST_PASSWORD']
        )

        send_mail(
            subject=data['subject'],
            message=data['body'],
            from_email=data['forward email'],
            recipient_list=[self.TO_EMAIL],
            auth_user=form_obj.config['HOST_USER'],
            auth_password=form_obj.config['HOST_PASSWORD'],
            connection=backend
        )
