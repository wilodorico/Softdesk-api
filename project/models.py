from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Project(models.Model):
    class ProjectType(models.TextChoices):
        BACKEND = "Back-end"
        FRONTEND = "Front-end"
        iOS = "iOS"
        ANDROID = "Android"

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    project_type = models.CharField(max_length=25, choices=ProjectType.choices, default=ProjectType.BACKEND)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
