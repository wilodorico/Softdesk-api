from django.contrib import admin

from project.models import Comment, Contributor, Issue, Project

admin.site.register(Project)
admin.site.register(Contributor)
admin.site.register(Issue)
admin.site.register(Comment)
