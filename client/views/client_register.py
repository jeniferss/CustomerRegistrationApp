from django.views import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from client.models import Client
from django.contrib.auth.mixins import LoginRequiredMixin


class ClientRegisterView(LoginRequiredMixin, View):
    template_name = 'clientRegister.html'
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):

        data = {}

        try:
            client_email = request.POST.get('registerClientEmail')
            client_document = request.POST.get('registerClientDocument')

            assert client_email, 'O campo de email deve estar preenchido'
            assert client_document, 'O campo de documento deve estar preenchido'

            Client.objects.create(email=client_email, cpf=client_document)

            return HttpResponseRedirect('/')

        except Exception as error:
            data.update({'errors': [str(error)]})

        return render(request, self.template_name, data)
