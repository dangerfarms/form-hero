from django.test import TestCase

from formhero.apps.models import App
from formhero.forms.models import Form
from formhero.providers.dbform import Backend
from formhero.providers.dbform.models import FormSubmission


class DatabaseFormTest(TestCase):
    def setUp(self):
        """
        Create an app, a form, data, and a backend for the tests.
        Variable db_config is empty as we don't need any
        configurations (but django complains if nothing is given
        to the config field of Form)
        """
        self.an_app = App.objects.create(name='this_app')
        self.data = {'name': 'Dave',
                     'inquirer email': 'dave@example.com',
                     'message': 'This is a test message'
                     }
        self.db_config = ''
        self.a_form = Form.objects.create(app=self.an_app, name='Form name', handler='db', config=self.db_config)

        self.db_backend = Backend()

    def test_should_save_a_form_submission(self):
        """
        Check that FormSubmission is saved in the db.
        """
        self.db_backend.handle_data(self.a_form, self.data)
        my_form_submission = FormSubmission.objects.get(form=self.a_form)

        self.assertEqual(my_form_submission.form, self.a_form)

    def test_should_check_form_submission_data_is_the_same_as_form_data(self):
        """
        Check that data saved in FormSubmission is the same as
        original test data.
        """
        self.db_backend.handle_data(self.a_form, self.data)
        my_form_submission = FormSubmission.objects.get(form=self.a_form)

        self.assertEqual(my_form_submission.form_data['message'], self.data['message'])
        self.assertEqual(my_form_submission.form_data['name'], self.data['name'])
        self.assertEqual(my_form_submission.form_data['inquirer email'], self.data['inquirer email'])
