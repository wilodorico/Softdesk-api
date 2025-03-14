from django.urls import path

from .views import RegisterView, UserDetailView, UserLIstView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("users/", UserLIstView.as_view(), name="users"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
]
