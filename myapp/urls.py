from django.contrib import admin
from django.urls import path,include
from . import views
from myapp.views import index
from django.contrib.auth import views as auth_views
from .forms import LoginForm, SignupForm
app_name = "myapp"
urlpatterns = [
    path("", index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("all-items/", views.all_items, name="all-items"),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("about", views.about_us, name = "about_us"),
    path("search/", views.search, name='search')
]