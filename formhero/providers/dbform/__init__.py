from formhero.providers.base import BaseBackend
from formhero.providers.dbform.models import FormSubmission


class Backend(BaseBackend):
    """
    Save form data on form instance.
    """
    def handle_data(self, form_obj, data):
        FormSubmission.objects.create(form=form_obj, form_data=data)
