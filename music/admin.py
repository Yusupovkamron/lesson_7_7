from django.contrib import admin

from .models import Artist, Albom, Songs, Country

admin.site.register([Artist, Albom, Songs, Country])