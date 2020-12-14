from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
@login_required
def home(request):
    context = {
        'posts': Post.objects.all(), #lay tat ca object Post truyen vao key posts
    }
    return render(request, 'blog/layout/base.html',context) # gui HTTPP request cho home.html truyen vao context de show ra views



def model_canvas(request):
    return render(request, 'blog/threejs/canvas.html')


def model_periodic(request):
    return render(request, 'blog/threejs/periodic.html',{'title': "Periodic table"})



class PostListView(ListView):
    model = Post
    template_name = 'blog/post/article.html' #chon duong link cho listview modelname/view_listtype.html
    context_object_name = 'posts' #goi list view tu context  cua home
    ordering = ['-date_posted'] #sap xep thu tu post tu ngay moi nhat
    paginate_by = 12


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/post/user_posts.html' #chon duong link cho listview modelname/view_listtype.html
    context_object_name = 'posts' #goi list view tu context  cua home
    paginate_by = 7

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']
    template_name = 'blog/post/post_form.html'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']
    template_name = 'blog/post/post_form.html'
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            False
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post/post_confirm_delete.html'
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            False

