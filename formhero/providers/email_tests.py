from django.test import TestCase
from unittest import mock

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
            'FROM_EMAIL': 'forwarder@example.com',
            'TO_EMAIL': 'company.email@example.com',
            'SUBJECT': 'generic subject'

        }
        self.data = {'name': 'Dave',
                     'message': 'This is a test message'

                     }
        self.a_form = Form(name=self.an_app, handler='email', config=self.email_config)
        self.my_backend = Backend()

    def check_email_config(self, config):
        """
        Check that configuration settings of a form are correct.
        Returns an error if they are not, ie valuable information
        is missing
        """
        list_of_keys_that_should_be_in_email_config = (
            'EMAIL_HOST',
            'EMAIL_PORT',
            'EMAIL_USER',
            'EMAIL_PASSWORD',
            'FROM_EMAIL',
            'TO_EMAIL',
            'SUBJECT'
        )
        self.assertEqual(len(list_of_keys_that_should_be_in_email_config), len(config))
        for setting in list_of_keys_that_should_be_in_email_config:
            self.assertTrue(setting in config)

    def test_should_raise_error_if_form_config_invalid(self):
        """
        create email config missing 'FROM_EMAIL' key, check that error
        is raised
        """
        modified_config = {
            'EMAIL_HOST': '',
            'EMAIL_PORT': '',
            'EMAIL_USER': '',
            'EMAIL_PASSWORD': '',
            'TO_EMAIL': 'company.email@example.com',
            'SUBJECT': 'generic subject'
        }
        self.a_form.config = modified_config
        with self.assertRaises(AssertionError):
            self.check_email_config(self.a_form.config)

    @mock.patch('formhero.providers.email.send_mail')
    def test_should_return_true_if_send_mail_method_called(self, mock_send_mail):
        """
        Mock out send_mail() in Backend to avoid testing connection.
        Check that mock_send_mail was called.
        """
        self.my_backend.handle_data(form_obj=self.a_form, data=self.data)

        self.assertTrue(mock_send_mail.called)

    @mock.patch('formhero.providers.email.send_mail')
    def test_should_check_send_mail_args_are_correct(self, mock_send_mail):
        """
        Mock out send_mail() in Backend. Test that it was given the
        correct arguments.
        """
        self.my_backend.handle_data(form_obj=self.a_form, data=self.data)
        arguments = mock_send_mail.call_args[1]

        self.assertEqual(arguments['subject'], self.a_form.config['SUBJECT'])
        self.assertEqual(arguments['message'], self.data)
        self.assertEqual(arguments['from_email'], self.a_form.config['FROM_EMAIL'])
        self.assertEqual(arguments['recipient_list'], [self.a_form.config['TO_EMAIL']])
        self.assertEqual(arguments['auth_user'], self.a_form.config['EMAIL_USER'])
        self.assertEqual(arguments['auth_password'], self.a_form.config['EMAIL_PASSWORD'])
