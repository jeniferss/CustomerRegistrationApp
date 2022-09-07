from django.views import View
from django.shortcuts import render
from client.models import Client
from django.contrib.auth.mixins import LoginRequiredMixin


class ClientListView(LoginRequiredMixin, View):
    template_name = 'clientList.html'
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        clients = Client.objects.all()
        return render(request, self.template_name, {'clients': clients})
