from formhero.providers.base import BaseBackend


class Backend(BaseBackend):
    """
    Send email out, requires
    email host, port, user, password

    """
    def handle_data(self, form_obj, data):
        pass
