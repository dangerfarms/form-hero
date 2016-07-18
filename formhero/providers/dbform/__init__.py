from formhero.providers.base import BaseBackend



class Backend(BaseBackend):
    """
    Save form data on form instance.
    """
    def handle_data(self, form_obj, data):
        from formhero.providers.dbform.models import FormEntry
        FormEntry.objects.create(form=form_obj, form_data=data)
