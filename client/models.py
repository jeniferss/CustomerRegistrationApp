from django.db import models


class Client(models.Model):
	email= models.CharField(max_length=500)
	cpf = models.CharField(max_length=11)

	class Meta:
		db_table = 'client'

	def __str__(self):
		return self.cpf
