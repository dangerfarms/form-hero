from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView


class APIRootView(APIView):
    URL_NAME = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({}, headers={
            'X-Build': getattr(settings, 'BUILD', 'Unknown'),
            'X-Version': getattr(settings, 'VERSION', 'Unknown'),
        })
