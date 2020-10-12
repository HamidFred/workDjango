from django.db import models

class Table(models.Model):
	isActive = models.BooleanField(default=False)
	age = models.IntegerField()
	name = models.CharField(max_length=200)
	email = models.EmailField()
	phone = models.CharField(max_length=100)
	def get_absolute_url(self):
		from django.urls import reverse
		return reverse('detail',args=[self.id])