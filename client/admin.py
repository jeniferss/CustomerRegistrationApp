from django.contrib import admin
from client.models import Client

class ClientAdmin(admin.ModelAdmin):
	list_display = ('email', 'cpf')


admin.site.register(Client, ClientAdmin)
