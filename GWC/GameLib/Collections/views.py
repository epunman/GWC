from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .models import Person
# Create your views here.
#function based view

def person(request):	
	return render(request, "person.html", {})

def boardgame(request):	
	return render(request, "boardgame.html", {})

def collection(request):	
	return render(request, "collection.html", {})

# class PersonView(View):
# 	def get(self, request, *args, **kwargs):
# 		#print(kwargs)
# 		context = {}
# 		return render(request, "person.html", context)

def person_listview(request):
	template_name = 'collections/person_list.html'
	queryset = Person.objects.all()
	context = {
		"object_list": queryset
	}
	return render(request, template_name, context)