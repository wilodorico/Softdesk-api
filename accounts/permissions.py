from rest_framework import permissions


class IsSelfOrAdminOrReadOnly(permissions.BasePermission):
    """Allow access to the user itself or admin for all methods, and read-only for others."""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj == request.user or request.user.is_superuser
