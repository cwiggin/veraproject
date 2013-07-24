from django.http import HttpResponse
from django.shortcuts import render
from veraproject.templates import home.html

def home(request):
	return render(request, 'home.html', template_values)