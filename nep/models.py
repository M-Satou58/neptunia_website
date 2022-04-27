from django.db import models

# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	email = models.EmailField()
	created_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.username