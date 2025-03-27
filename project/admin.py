from django.contrib import admin

from project.models import Contributor, Project

admin.site.register(Project)
admin.site.register(Contributor)
