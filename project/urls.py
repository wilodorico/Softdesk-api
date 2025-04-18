from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from project.views import CommentViewset, ContributorViewset, IssueViewset, ProjectViewset

router = DefaultRouter()
router.register(r"projects", ProjectViewset)
router.register(r"comments", CommentViewset)

# Nested router
project_router = routers.NestedSimpleRouter(router, r"projects", lookup="project")
project_router.register(r"contributors", ContributorViewset, basename="project-contributors")
project_router.register(r"issues", IssueViewset, basename="project-issues")


urlpatterns = [
    path("", include(router.urls)),
    path("", include(project_router.urls)),
]
