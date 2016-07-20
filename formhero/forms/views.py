from rest_framework.generics import CreateAPIView
from formhero.forms.serializers import FormSerializer
from formhero.forms.models import Form
from formhero.forms.permission_classes import HostPermission


class CreateForm(CreateAPIView):

    URL_NAME = 'create-form'
    serializer_class = FormSerializer
    queryset = Form.objects.all()
    permission_classes = (HostPermission,)
