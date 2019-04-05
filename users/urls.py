from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'app_users'
urlpatterns = [
    #path('', views.PostsView.as_view(), name='home'),
    path('login/', LoginView.as_view(
        template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(
        template_name='users/logout.html'), name='logout'),
    path('register/',views.UserRegisterView.as_view(), name='register'),
    path('profile/', views.ProfileView.as_view(), name = 'profile'),
    path('profile_edit/', views.profile_edit, name = 'profile_edit'),
]
