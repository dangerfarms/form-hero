from rest_framework import serializers
from formhero.forms.models import Form


class FormSerializer(serializers.ModelSerializer):

    class Meta:
        model = Form
        fields = ('app', 'name', 'handler', 'config', )
