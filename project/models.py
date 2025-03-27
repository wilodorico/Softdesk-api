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

    def __str__(self):
        return self.name


class Contributor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    joined_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "project")  # A user can only be a contributor to a project once

    def __str__(self):
        return f"{self.user} - {self.project}"
