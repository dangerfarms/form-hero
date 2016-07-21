from rest_framework.permissions import BasePermission
from formhero.apps.models import App


class HostPermission(BasePermission):
    def has_permission(self, request, view):
        hosts = App.objects.values_list('host_list').get(pk=request.data['app'])[0]
        thishost = request.get_host()
        return (thishost in hosts)
