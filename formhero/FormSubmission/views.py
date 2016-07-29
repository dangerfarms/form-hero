from rest_framework.generics import GenericAPIView


class SubmitForm(GenericAPIView):
    def post(self, request, *args, **kwargs):
        handler = self.get_handler(request.form_obj.handler)
        handler.handle_data()
