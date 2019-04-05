"""twitfa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls')),
    path('posts/', include('blog.urls')),
    path('', RedirectView.as_view(pattern_name='app_blog:home'),name='redirect_home' ),
    path('password-reset-confirm/<uidb64>/<token>/',RedirectView.as_view(pattern_name='app_users:password_reset_confirm'),
         name='password_reset_confirm'),
    path('password-reset/done/',RedirectView.as_view(pattern_name='app_users:password_reset_done'),
         name='password_reset_done'),
    path('password-reset',RedirectView.as_view(
        pattern_name='app_users:password_reset'),
        name='password_reset'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
