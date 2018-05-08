import random
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.
#function based view

def home(request):	
	return render(request, "home.html", {})

def person(request):	
	return render(request, "person.html", {})

def boardgame(request):	
	return render(request, "boardgame.html", {})

def collection(request):	
	return render(request, "collection.html", {})