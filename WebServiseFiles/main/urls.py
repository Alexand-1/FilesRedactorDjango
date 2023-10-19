from django.urls import path
from . import views
from allauth.account.views import LoginView, SignupView, LogoutView

urlpatterns = [
    path('',views.index),
    path('home/', views.home, name= 'home'),
    path('accounts/login/', LoginView.as_view(), name='account_login'),
    path('accounts/signup/', SignupView.as_view(), name='account_signup'),
    path('logout/', LogoutView.as_view(), name='account_logout'),


]
