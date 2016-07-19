from email.message import EmailMessage

from django.core.mail import send_mail, get_connection
from django.core.mail.backends.smtp import EmailBackend

from formhero.providers.base import BaseBackend


class Backend(BaseBackend):
    TO_EMAIL = 'company.email@example.com'
    """
    Send email out, requires
    email host, port, user, password

    """

    def handle_data(self, form_obj, data):
        import ipdb; ipdb.set_trace()
        backend = EmailBackend(
            host=data['email host'],
            port=data['email port'],
            username=data['host username'],
            password=data['host password'],
        )
        send_mail(
            subject=data['subject'],
            message=data['body'],
            from_email=data['forward email'],
            recipient_list=[self.TO_EMAIL],
            auth_user=data['host username'],
            auth_password=['host password'],
            connection=backend
        )
