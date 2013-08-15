from django.db import models

class preres(models.Model):
	bandnamelink = models.CharField(max_length=1000)
	reviewerblurb = models.CharField(max_length=200)
