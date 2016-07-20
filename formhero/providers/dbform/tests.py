from django.test import TestCase

from formhero.apps.models import App
from formhero.forms.models import Form
from formhero.providers.dbform import Backend
from formhero.providers.dbform.models import FormEntry


class DatabaseFormTest(TestCase):
    def test_should_save_a_form_entry(self):
        an_app = App.objects.create(name='this_app')
        data = {'name': 'Dave',
                'inquirer email': 'dave@example.com',
                'message': 'This is a test message'
                }
        a_form = Form.objects.create(app=an_app, name='Form name', handler='db', config=data)

        db_backend = Backend()
        db_backend.handle_data(a_form, a_form.config)
        my_form_entry = FormEntry.objects.get(form=a_form)

        self.assertEquals(my_form_entry.form, a_form)
