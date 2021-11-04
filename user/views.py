from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from user.models import User,Post
from user.forms import UserForm,PostForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,CreateView
# Create your views here.


class UserView(TemplateView):
    template_name = 'user/user_basic.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(updated_at__lte=timezone.now()).order_by('-updated_at')

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'user/post_detail.html'
    form_class = UserForm
    model = Post

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'user/post_detail.html'
    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'user/post_draft_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(updated_at__isnull=True).order_by('updated_at')


@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)
