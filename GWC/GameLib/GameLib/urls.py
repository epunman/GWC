"""GameLib URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from django.contrib.auth.views import LoginView, LogoutView

from Collections.views import (
    PersonListView,
    PersonDetailView,
    PersonCreateView,
    BoardgameListView,
    BoardgameDetailView,
    BoardgameCreateView,
    CollectionListView,
    CollectionDetailView,
    CollectionCreateView,
    CheckoutListView,
    CheckoutDetailView,
    CheckoutCreateView,

)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^person/$', PersonListView.as_view()),
    url(r'^person/(?P<slug>\w+)$', PersonListView.as_view()),
    url(r'^persondetail/(?P<pk>\w+)$', PersonDetailView.as_view()),
    url(r'^personadd/$', PersonCreateView.as_view()),
    url(r'^boardgame/$', BoardgameListView.as_view()),
    url(r'^boardgame/(?P<slug>\w+)$', BoardgameListView.as_view()),
    url(r'^boardgamedetail/(?P<pk>\w+)$', BoardgameDetailView.as_view()),
    url(r'^boardgameadd/$', BoardgameCreateView.as_view()),
    url(r'^collection/$', CollectionListView.as_view()),
    url(r'^collection/(?P<slug>\w+)$', CollectionListView.as_view()),
    url(r'^collectiondetail/(?P<pk>\w+)$', CollectionDetailView.as_view()),
    url(r'^collectionadd/$', CollectionCreateView.as_view()),
    url(r'^checkout/$', CheckoutListView.as_view()),
    #url(r'^checkout/(?P<slug>\w+)$', CheckoutListView.as_view()),
    url(r'^checkoutdetail/(?P<pk>\w+)$', CheckoutDetailView.as_view()),
    url(r'^checkoutadd/$', CheckoutCreateView.as_view()),
    #url(r'^checkoutadd/(?P<slug>\w+)$', CheckoutCreateView.as_view()),
]
