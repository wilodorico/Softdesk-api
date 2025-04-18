from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    allows the author to make changes.
    """

    message = "You are not authorized to perform this action."

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user
