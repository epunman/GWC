from django.contrib import admin

# Register your models here.
from .models import Person, Boardgame, Collection

admin.site.register(Person)
admin.site.register(Boardgame)
admin.site.register(Collection)