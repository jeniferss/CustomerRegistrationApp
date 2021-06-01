from django.shortcuts import render, redirect
from client.models import Client
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request):
	return render(request, 'login.html')

def logout_user(request):
	logout(request)
	return redirect('/')

@login_required(login_url='/login/')
def index(request):
	return render(request, 'index.html')

def submit_login(request):
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		usuario = authenticate(username=username, password=password)
		if usuario is not None:
			login(request, usuario)
			return redirect('/')
		else:
			messages.error(request, "Usuário Inválido! Logue com o administrador")

		return redirect('/')

@login_required(login_url='/login/')
def list_clients(request):
	client = Client.objects.all()
	dados = {'clients': client}
	return render(request, 'client_list.html', dados)

@login_required(login_url='/login/')
def clientes(request):
	return render(request, 'clients.html')

@login_required(login_url='/login/')
def submit_clientes(request):
	if request.POST:
		email = request.POST.get('email')
		cpf = request.POST.get('cpf')
		Client.objects.create(email=email, cpf=cpf)

	return redirect('/')
