from django.urls import include, path
from rest_framework.routers import DefaultRouter

from project.views import ProjectViewset

router = DefaultRouter()
router.register(r"projects", ProjectViewset)

urlpatterns = [
    path("", include(router.urls)),
]
