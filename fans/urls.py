from django.urls import path
from . import views

app_name = "fans"
urlpatterns = [
    path("register/", views.RegistrationView.as_view(), name="register"),
    path("login/", views.AuthLoginView.as_view(), name="login"),
    path("logout/", views.AuthLogoutView.as_view(), name="logout"),
    path("fan_list/", views.FanListView.as_view(), name="fan_list"),
]
