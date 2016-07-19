from unittest import mock

from django.core import mail
from django.test import TestCase

from formhero.apps.models import App
from formhero.forms.models import Form
from formhero.providers.email import Backend


class SendEmailTest(TestCase):
    @mock.patch('formhero.providers.email.send_mail')
    def test_should_return_true_if_send_mail_method_called(self, mock_send_mail):
        an_app = App(name='this_app')
        a_form = Form(name=an_app,handler='email', config='Whatever')
        my_backend = Backend()
        data = {'forward email': 'forwarder@example.com',
                'inquirer email': 'dave@example.com',
                'email host': '',
                'email port': '',
                'host username': '',
                'host password': '',
                'body': 'This is a test message body',
                'subject': 'test subject'
        }
        my_backend.handle_data(form_obj=a_form, data=data)

        self.assertTrue(mock_send_mail.called)
