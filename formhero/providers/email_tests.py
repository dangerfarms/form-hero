from unittest import mock

from django.test import TestCase

from formhero.apps.models import App
from formhero.forms.models import Form
from formhero.providers.email import Backend


class SendEmailTest(TestCase):
    def setUp(self):
        """
        Create an app, a form, data, and a backend
        to be used in all tests
        """
        self.an_app = App(name='this_app')
        self.a_form = Form(name=self.an_app, handler='email')
        self.data = {'forward email': 'forwarder@example.com',
                     'inquirer email': 'dave@example.com',
                     'email host': '',
                     'email port': '',
                     'host username': '',
                     'host password': '',
                     'body': 'This is a test message body',
                     'subject': 'test subject'
                     }
        self.my_backend = Backend(
            host=self.data['email host'],
            port=self.data['email port'],
            username=self.data['host username'],
            password=self.data['host password']
        )

    @mock.patch('formhero.providers.email.send_mail')
    def test_should_return_true_if_send_mail_method_called(self, mock_send_mail):
        """
        Mock out send_mail() in Backend to avoid testing connection.
        Check that mock_send_mail was called.
        """
        self.my_backend.handle_data(form_obj=self.a_form, data=self.data)

        self.assertTrue(mock_send_mail.called)

    @mock.patch('formhero.providers.email.send_mail')
    def test_should_check_args_are_correct(self, mock_send_mail):
        """
        Mock out send_mail() in Backend. Test that it was given the
        correct arguments.
        """
        self.my_backend.handle_data(form_obj=self.a_form, data=self.data)
        arguments = mock_send_mail.call_args[1]

        self.assertEqual(arguments['subject'], self.data['subject'])
        self.assertEqual(arguments['message'], self.data['body'])
        self.assertEqual(arguments['from_email'], self.data['forward email'])
        self.assertEqual(arguments['recipient_list'], [Backend.TO_EMAIL])
        self.assertEqual(arguments['auth_user'], self.data['host username'])
        self.assertEqual(arguments['auth_password'], self.data['host password'])

    @mock.patch('formhero.providers.email.send_mail')
    def test_should_raise_error_if_data_invalid(self):
        """
        Create data missing the 'body' parameter, and Check that send_mail raises
        a KeyError
        """
        modified_data = {'forward email': 'forwarder@example.com',
                     'inquirer email': 'dave@example.com',
                     'email host': '',
                     'email port': '',
                     'host username': '',
                     'host password': '',
                     'subject': 'test subject'
                     }
        with self.assertRaises(KeyError):
            self.my_backend.handle_data(form_obj=self.a_form, data=modified_data)
