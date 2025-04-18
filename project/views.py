from django.contrib.auth import get_user_model
from rest_framework import status, viewsets
from rest_framework.exceptions import NotFound, PermissionDenied, ValidationError
from rest_framework.permissions import IsAuthenticated

from project.models import Comment, Contributor, Issue, Project
from project.permissions import IsOwnerOrReadOnly
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
    permission_classes = [IsOwnerOrReadOnly]

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
        except (Project.DoesNotExist, User.DoesNotExist):
            raise NotFound("Project or User not found")

        # Vérification que l'utilisateur est l'auteur du projet
        if project.author != self.request.user:
            raise PermissionDenied("You are not authorized to perform this action.")

        # Vérification que l'utilisateur n'est pas déjà contributeur
        if Contributor.objects.filter(project=project, user=user).exists():
            raise ValidationError({"detail": "This user is already a contributor."}, code=status.HTTP_400_BAD_REQUEST)

        serializer.save(project=project, user=user)


class IssueViewset(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = IssueSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)


class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)
