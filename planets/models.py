from django.db import models
# Create your models here.
class Planet(models.Model):
	name = models.CharField(max_length=150)
	climate = models.CharField(max_length=50,default=None)
	terrain  = models.CharField(max_length=50,default=None)
	

	def __str__(self):
		return self.name