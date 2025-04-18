from django.shortcuts import get_object_or_404
from rest_framework import permissions

from project.models import Project


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    allows the author to make changes.
    """

    message = "You are not authorized to perform this action."

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user


class IsContributor(permissions.BasePermission):
    """
    Allows contributors to access
    """

    message = "You are not authorized to perform this action."

    def has_permission(self, request, view):
        project_id = view.kwargs.get("project_pk") if view.basename == "project-issues" else view.kwargs.get("pk")

        if view.basename == "projects" and view.action == "list":
            return request.user.is_authenticated

        if project_id is None:
            return False

        project = get_object_or_404(Project, pk=project_id)

        has_contributor = project.contributors.filter(user=request.user).exists()

        return has_contributor
