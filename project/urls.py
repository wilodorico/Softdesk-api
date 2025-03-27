from django.urls import include, path
from rest_framework.routers import DefaultRouter

from project.views import ContributorViewset, IssueViewset, ProjectViewset

router = DefaultRouter()
router.register(r"projects", ProjectViewset)
router.register(r"contributors", ContributorViewset)
router.register(r"issues", IssueViewset)

urlpatterns = [
    path("", include(router.urls)),
]
