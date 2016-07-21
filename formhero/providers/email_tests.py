from unittest import mock

from django.test import TestCase

from formhero.apps.models import App
from formhero.forms.models import Form
from formhero.providers.email import Backend


class SendEmailTest(TestCase):
    def setUp(self):
        """
        Create an app, a form, data,email config, and a backend
        to be used in all tests
        """
        self.an_app = App(name='this_app')
        self.email_config = {
            'EMAIL_HOST': '',
            'EMAIL_PORT': '',
            'EMAIL_USER': '',
            'EMAIL_PASSWORD': '',
        }
        self.data = {'forward email': 'forwarder@example.com',
                     'inquirer email': 'dave@example.com',
                     'body': 'This is a test message body',
                     'subject': 'test subject'
                     }
        self.a_form = Form(name=self.an_app, handler='email', config=self.email_config)
        self.my_backend = Backend()

    def email_config_checker(self, config):
        """
        Check that configuration settings of a form are correct.
        Returns an error if they are not, ie valuable information
        is missing
        """
        list_of_keys_that_should_be_in_email_config = (
            'EMAIL_HOST',
            'EMAIL_PORT',
            'EMAIL_USER',
            'EMAIL_PASSWORD'
        )
        self.assertEqual(len(list_of_keys_that_should_be_in_email_config), len(config))
        for setting in list_of_keys_that_should_be_in_email_config:
            self.assertTrue(setting in config)

    @mock.patch('formhero.providers.email.send_mail')
    def test_should_return_true_if_send_mail_method_called(self, mock_send_mail):
        """
        Mock out send_mail() in Backend to avoid testing connection.
        Check that mock_send_mail was called.
        """
        self.email_config_checker(self.a_form.config)
        self.my_backend.handle_data(form_obj=self.a_form, data=self.data)

        self.assertTrue(mock_send_mail.called)

    @mock.patch('formhero.providers.email.send_mail')
    def test_should_check_send_mail_args_are_correct(self, mock_send_mail):
        """
        Mock out send_mail() in Backend. Test that it was given the
        correct arguments.
        """
        self.email_config_checker(self.a_form.config)
        self.my_backend.handle_data(form_obj=self.a_form, data=self.data)
        arguments = mock_send_mail.call_args[1]

        self.assertEqual(arguments['subject'], self.data['subject'])
        self.assertEqual(arguments['message'], self.data['body'])
        self.assertEqual(arguments['from_email'], self.data['forward email'])
        self.assertEqual(arguments['recipient_list'], [Backend.TO_EMAIL])
        self.assertEqual(arguments['auth_user'], self.a_form.config['EMAIL_USER'])
        self.assertEqual(arguments['auth_password'], self.a_form.config['EMAIL_PASSWORD'])

    @mock.patch('formhero.providers.email.send_mail')
    def test_should_raise_error_if_data_invalid(self, mock_send_mail):
        """
        Create data missing the 'body' parameter, and Check that send_mail raises
        a KeyError
        """
        modified_data = {'forward email': 'forwarder@example.com',
                         'inquirer email': 'dave@example.com',
                         'subject': 'test subject'
                         }
        with self.assertRaises(KeyError):
            self.my_backend.handle_data(form_obj=self.a_form, data=modified_data)
