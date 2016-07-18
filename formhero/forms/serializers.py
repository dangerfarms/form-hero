from rest_framework import serializers
from formhero.forms.models import Form

class MessageSerializer(serializers.ModelSerializer):


    class Meta:
        model = Form
        fields = (

        )