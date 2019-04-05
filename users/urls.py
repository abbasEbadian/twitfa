from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'app_users'
urlpatterns = [
    #path('', views.PostsView.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(
        template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='users/logout.html'), name='logout'),
    path('register/',views.UserRegisterView.as_view(), name='register'),
    path('profile/', views.ProfileView.as_view(), name = 'profile'),
    path('profile_edit/', views.profile_edit, name = 'profile_edit'),
    path('password-reset', auth_views.PasswordResetView.as_view(
        template_name='users/password_reset_view.html',
    ),name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm_view.html'
    ), name='password_reset_confirm'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done_view.html'
    ), name='password_reset_done'),
        path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(
            template_name='users/password_reset_complete_view.html'
        ), name='password_reset_complete'),
]
