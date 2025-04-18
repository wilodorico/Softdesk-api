from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from project.views import CommentViewset, ContributorViewset, IssueViewset, ProjectViewset

router = DefaultRouter()
router.register(r"projects", ProjectViewset)
router.register(r"issues", IssueViewset)
router.register(r"comments", CommentViewset)

# Router imbriqué pour les contributeurs
project_router = routers.NestedSimpleRouter(router, r"projects", lookup="project")
project_router.register(r"contributors", ContributorViewset, basename="project-contributors")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(project_router.urls)),
]
