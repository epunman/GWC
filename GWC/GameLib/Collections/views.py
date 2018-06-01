from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Person, Boardgame, Collection, Checkout
from .forms import PersonCreateForm, BoardgameCreateForm, CollectionCreateForm, CheckoutCreateForm

def person_listview(request):
	template_name = 'collections/person_list.html'
	queryset = Person.objects.all()
	context = {
		"object_list": queryset
	}
	return render(request, template_name, context)

class PersonListView(LoginRequiredMixin, ListView):
	template_name = 'collections/person_list.html'

	def get_queryset(self):
		slug = self.kwargs.get("slug")
		if slug:
			queryset = Person.objects.filter(
					Q(LastName__iexact=slug) |
					Q(LastName__icontains=slug) |
					Q(FirstName__iexact=slug) |
					Q(FirstName__icontains=slug)
				)
		else:
			queryset = Person.objects.all()
		return queryset

class PersonDetailView(LoginRequiredMixin, DetailView):
	queryset = Person.objects.all()
	template_name = 'collections/person_detail.html'
	def get_context_data(self, *args, **kwargs):
		context = super(PersonDetailView, self).get_context_data(*args, **kwargs)
		return context

class PersonCreateView(LoginRequiredMixin, CreateView):
	form_class = PersonCreateForm
	template_name = 'collections/person_form.html'
	success_url = '/person'

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.AuthUser = self.request.user
		#instance.save()
		return super(PersonCreateView, self).form_valid(form)


def boardgame_listview(request):
	template_name = 'collections/boardgame_list.html'
	queryset = Boardgame.objects.all()
	context = {
		"object_list": queryset
	}
	return render(request, template_name, context)

class BoardgameListView(LoginRequiredMixin, ListView):
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

class BoardgameDetailView(LoginRequiredMixin, DetailView):
	queryset = Boardgame.objects.all()
	template_name = 'collections/boardgame_detail.html'
	def get_context_data(self, *args, **kwargs):
		context = super(BoardgameDetailView, self).get_context_data(*args, **kwargs)
		return context

class BoardgameCreateView(LoginRequiredMixin, CreateView):
	form_class = BoardgameCreateForm
	template_name = 'collections/boardgame_form.html'
	success_url = '/boardgame'




def collection_listview(request):
	template_name = 'collections/collection_list.html'
	queryset = Collection.objects.all()
	context = {
		"object_list": queryset
	}
	return render(request, template_name, context)

class CollectionListView(LoginRequiredMixin, ListView):
	template_name = 'collections/collection_list.html'

	def get_queryset(self):
		slug = self.kwargs.get("slug")
		if slug:
			queryset = Collection.objects.filter(
					Q(Person__LastName__iexact=slug) |
					Q(Person__LastName__icontains=slug) |
					Q(Boardgame__Name__iexact=slug) |
					Q(Boardgame__Name__icontains=slug)
				)
		else:
			queryset = Collection.objects.all()
		return queryset

class CollectionDetailView(LoginRequiredMixin, DetailView):
	queryset = Collection.objects.all()
	template_name = 'collections/collection_detail.html'
	def get_context_data(self, *args, **kwargs):
		context = super(CollectionDetailView, self).get_context_data(*args, **kwargs)
		return context

class CollectionCreateView(LoginRequiredMixin, CreateView):
	form_class = CollectionCreateForm
	template_name = 'collections/collection_form.html'
	success_url = '/collection'




def checkout_listview(request):
	template_name = 'collections/checkout_list.html'
	queryset = Checkout.objects.all()
	context = {
		"object_list": queryset
	}
	return render(request, template_name, context)

class CheckoutListView(LoginRequiredMixin, ListView):
	template_name = 'collections/checkout_list.html'

	def get_queryset(self):
		slug = self.kwargs.get("slug")
		if slug:
			queryset = Checkout.objects.filter(
					Q(Attendee__LastName__iexact=slug) |
					Q(Attendee__LastName__icontains=slug) |
					Q(BoardgameFromCollection__Name__iexact=slug) |
					Q(BoardgameFromCollection__Name__icontains=slug) |
					Q(BoardgameFromCollection__id__iexact=slug)
				)
		else:
			queryset = Checkout.objects.all()
		return queryset

class CheckoutDetailView(LoginRequiredMixin, DetailView):
	queryset = Checkout.objects.all()
	template_name = 'collections/checkout_detail.html'
	def get_context_data(self, *args, **kwargs):
		context = super(CheckoutDetailView, self).get_context_data(*args, **kwargs)
		return context

class CheckoutCreateView(LoginRequiredMixin, CreateView):
	form_class = CheckoutCreateForm
	template_name = 'collections/checkout_form.html'
	success_url = '/checkout'