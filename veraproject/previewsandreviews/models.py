from django.db import models

class preres(models.Model):
	headlininglink = models.CharField(max_length=200)
	details = models.CharField(max_length=1000)

