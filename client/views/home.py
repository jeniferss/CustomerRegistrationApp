from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, View):
    template_name = 'index.html'
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
