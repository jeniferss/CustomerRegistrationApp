from django.views import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


class LoginView(View):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):

        data = {}

        try:
            username = request.POST.get('loginUsername')
            password = request.POST.get('loginPassword')

            assert username, 'O campo de nome de usuário deve estar preenchido'
            assert password, 'O campo da senha deve estar preenchido'

            user = authenticate(username=username, password=password)

            assert user, 'Usuário Inválido!'

            login(request, user)
            return HttpResponseRedirect('/')

        except Exception as error:
            data.update({'errors': [str(error)]})

        return render(request, self.template_name, data)
