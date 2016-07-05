from django.conf.urls import include, url
from django.contrib import admin
from .views import HomeView, RegisterView, LoginView, ProfileView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(HomeView.as_view()), name="home"),
    url(r'^register/$', RegisterView.as_view(), name="register"),
    url(r'^profile/$', login_required(ProfileView.as_view()), name="profile"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^logout$', 'apps.inicio.views.LogOut', name='logout'),
]