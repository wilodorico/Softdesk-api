from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from project.views import CommentViewset, ContributorViewset, IssueViewset, ProjectViewset

router = DefaultRouter()
router.register(r"projects", ProjectViewset, basename="projects")

# Nested router
project_router = routers.NestedSimpleRouter(router, r"projects", lookup="project")
project_router.register(r"contributors", ContributorViewset, basename="project-contributors")
project_router.register(r"issues", IssueViewset, basename="project-issues")

issue_router = routers.NestedSimpleRouter(project_router, r"issues", lookup="issue")
issue_router.register(r"comments", CommentViewset, basename="issue-comments")


urlpatterns = [
    path("", include(router.urls)),
    path("", include(project_router.urls)),
    path("", include(issue_router.urls)),
]
