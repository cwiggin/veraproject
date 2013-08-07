from django.db import models

class Shows(models.Model):
	name = models.CharField(max_length=200)
	date = models.DateTimeField()
	ticketurl = models.CharField(max_length=1000)

