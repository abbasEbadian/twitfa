from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from .models import Post
from django.contrib.auth.models import User
from .forms import PostForm
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib import messages
# Create your views here.


class PostsView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering=['-date']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['special'] = False
        return context

class SpecialPostsView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(user=user).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.kwargs.get('username')
        context['special'] = True
        return context

class NewPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/new_post.html'
    success_url =  reverse_lazy('app_blog:my_posts')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NewPostView, self).form_valid(form)


class EditPostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['content']
    template_name = 'blog/edit_post.html'
    success_url = reverse_lazy('app_blog:my_posts')
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.last_modified_date = timezone.now()
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/delete_post.html"
    success_url = reverse_lazy('app_blog:my_posts')
    def form_valid(self, form):
        messages.success(self.request, 'پست حذف شد.')
        return super().form_valid(form)


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        else:
            return False
