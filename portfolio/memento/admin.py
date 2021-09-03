from django.contrib import admin

from .models import *
from django.apps import apps

for model in apps.get_app_config('memento').models.values():
    admin.site.register(model)
