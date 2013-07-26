from django.http import HttpResponse
from django.shortcuts import render
from shows.models import Shows
from zinnia.models.entry import Entry

def home(request):
	shows = Shows.objects.all()
	blogs = Entry.objects.all()

	print blogs[0]

	print shows[0].name

	print shows[0].date

	template_values = {}
	template_values["shows"] = shows
	template_values["blogs"] = blogs

	return render(request, 'home.html', template_values)