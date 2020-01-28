from django.contrib import admin

# Register your models here.
from core.models import *

Models = [Categoria, Evento]

admin.site.register(Models)
