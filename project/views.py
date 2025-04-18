from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.exceptions import NotFound, PermissionDenied, ValidationError
from rest_framework.permissions import IsAuthenticated

from project.models import Comment, Contributor, Issue, Project
from project.permissions import IsAuthorOrReadOnly
from project.serializers import (
    CommentSerializer,
    ContributorSerializer,
    IssueSerializer,
    ProjectCreateSerializer,
    ProjectDetailSerializer,
)

User = get_user_model()


class ProjectViewset(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [IsAuthorOrReadOnly]

    def get_serializer_class(self):
        if self.action == "create":
            return ProjectCreateSerializer
        return ProjectDetailSerializer

    def perform_create(self, serializer):
        user = self.request.user
        project = serializer.save(author=user)
        Contributor.objects.create(user=user, project=project)


class ContributorViewset(viewsets.ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        project_id = self.kwargs.get("project_pk")
        return Contributor.objects.filter(project_id=project_id)

    def perform_create(self, serializer):
        project_id = self.kwargs.get("project_pk")
        user_to_add = serializer.validated_data.get("user")

        try:
            project = Project.objects.get(pk=project_id)
            user = User.objects.get(pk=user_to_add.id)
        except Project.DoesNotExist:
            raise NotFound("Project not found")
        except User.DoesNotExist:
            raise NotFound("User not found")

        # Check if the user is the author of the project
        if project.author != self.request.user:
            raise PermissionDenied("You are not authorized to perform this action.")

        # Check if the user is already a contributor
        if Contributor.objects.filter(project=project, user=user).exists():
            raise ValidationError({"detail": "This user is already a contributor."}, code=status.HTTP_400_BAD_REQUEST)

        serializer.save(project=project, user=user)


class IssueViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthorOrReadOnly]
    serializer_class = IssueSerializer

    def get_queryset(self):
        project_id = self.kwargs.get("project_pk")
        return Issue.objects.filter(project_id=project_id)

    def perform_create(self, serializer):
        user = self.request.user
        project = get_object_or_404(Project, pk=self.kwargs.get("project_pk"))
        serializer.save(author=user, project=project)


class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)
