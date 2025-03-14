from django.urls import path

from .views import RegisterView, UserLIstView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("users/", UserLIstView.as_view(), name="users"),
]
