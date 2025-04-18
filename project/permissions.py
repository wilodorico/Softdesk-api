from django.shortcuts import get_object_or_404
from rest_framework import permissions

from project.models import Project


def get_project_id_from_kwargs(view):
    """
    Helper function to get the project ID from the view's kwargs.
    """
    if "project_pk" in view.kwargs:
        return view.kwargs.get("project_pk")
    return view.kwargs.get("pk")


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Allows the author to make changes.
    """

    message = "You are not authorized to perform this action."

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if view.basename == "project-contributors":
            project_id = get_project_id_from_kwargs(view)
            if project_id is None:
                return False

            project = get_object_or_404(Project, pk=project_id)
            has_author = project.author == request.user
            return has_author

        return obj.author == request.user


class IsContributor(permissions.BasePermission):
    """
    Allows contributors to access
    """

    message = "You are not authorized to perform this action."

    def has_permission(self, request, view):
        project_id = get_project_id_from_kwargs(view)

        if view.basename == "projects" and view.action == "list":
            return request.user.is_authenticated

        if project_id is None:
            return False

        project = get_object_or_404(Project, pk=project_id)
        has_contributor = project.contributors.filter(user=request.user).exists()

        return has_contributor
