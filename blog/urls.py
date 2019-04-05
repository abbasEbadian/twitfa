from django.urls import path
from . import views

app_name = 'app_blog'
urlpatterns = [
    path('user/<str:username>/', views.SpecialPostsView.as_view(), name='user_posts'),
    path('', views.PostsView.as_view(), name='home'),
    path('post/new',views.NewPostView.as_view(), name='new_post'),
    path('post/edit/<int:pk>',views.EditPostView.as_view(), name='edit_post'),
    path('post/delete/<int:pk>',views.PostDeleteView.as_view(), name='delete_post'),



]
