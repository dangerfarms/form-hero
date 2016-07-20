from django.test import TestCase

from formhero.apps.models import App
from formhero.forms.models import Form
from formhero.providers.dbform import Backend
from formhero.providers.dbform.models import FormEntry


class DatabaseFormTest(TestCase):

    def setUp(self):
        self.an_app = App.objects.create(name='this_app')
        self.data = {'name': 'Dave',
                'inquirer email': 'dave@example.com',
                'message': 'This is a test message'
                }
        self.a_form = Form.objects.create(app=self.an_app, name='Form name', handler='db')

        self.db_backend = Backend()

    def test_should_save_a_form_entry(self):
        self.db_backend.handle_data(self.a_form, self.data)
        my_form_entry = FormEntry.objects.get(form=self.a_form)

        self.assertEqual(my_form_entry.form, self.a_form)

    def test_should_check_form_entry_data_is_the_same_as_form_data(self):
        self.db_backend.handle_data(self.a_form, self.a_form.config)
        my_form_entry = FormEntry.objects.get(form=self.a_form)

        self.assertEqual(my_form_entry.form_data['message'], self.data['message'])
        self.assertEqual(my_form_entry.form_data['name'], self.data['name'])
        self.assertEqual(my_form_entry.form_data['inquirer email'], self.data['inquirer email'])
