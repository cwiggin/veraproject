from django.http import HttpResponse
from django.shortcuts import render
from shows.models import Shows

def home(request):
	shows = Shows.objects.all()

	print shows[0].name

	print shows[0].date

	template_values = {
		"shows": shows,
	}
	return render(request, 'shows.html', template_values)