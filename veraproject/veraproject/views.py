from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	template_values = {}
	return render(request, 'home.html', template_values)