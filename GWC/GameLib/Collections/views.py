from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView
from .models import Person, Boardgame, Collection
# Create your views here.
#function based view

# def person(request):	
# 	return render(request, "person.html", {})

# def boardgame(request):	
# 	return render(request, "boardgame.html", {})

# def collection(request):	
# 	return render(request, "collection.html", {})

def person_listview(request):
	template_name = 'collections/person_list.html'
	queryset = Person.objects.all()
	context = {
		"object_list": queryset
	}
	return render(request, template_name, context)

class PersonListView(ListView):
	template_name = 'collections/person_list.html'

	def get_queryset(self):
		slug = self.kwargs.get("slug")
		if slug:
			queryset = Person.objects.filter(
					Q(LastName__iexact=slug) |
					Q(LastName__icontains=slug)
				)
		else:
			queryset = Person.objects.all()
		return queryset

def boardgame_listview(request):
	template_name = 'collections/boardgame_list.html'
	queryset = Boardgame.objects.all()
	context = {
		"object_list": queryset
	}
	return render(request, template_name, context)

class BoardgameListView(ListView):
	template_name = 'collections/boardgame_list.html'

	def get_queryset(self):
		slug = self.kwargs.get("slug")
		if slug:
			queryset = Boardgame.objects.filter(
					Q(Name__iexact=slug) |
					Q(Name__icontains=slug)
				)
		else:
			queryset = Boardgame.objects.all()
		return queryset

def collection_listview(request):
	template_name = 'collections/collection_list.html'
	queryset = Collection.objects.all()
	context = {
		"object_list": queryset
	}
	return render(request, template_name, context)

class CollectionListView(ListView):
	template_name = 'collections/collection_list.html'

	def get_queryset(self):
		slug = self.kwargs.get("slug")
		if slug:
			queryset = Collection.objects.filter(
					Q(Person__LastName__iexact=slug) |
					Q(Person__LastName__icontains=slug) |
					Q(Boardgame__Name__iexact=slug) |
					Q(Boardgame__Name__icontains=slug) |
					Q(RFIDTag__iexact=slug) |
					Q(RFIDTag__icontains=slug)
				)
		else:
			queryset = Collection.objects.all()
		return queryset