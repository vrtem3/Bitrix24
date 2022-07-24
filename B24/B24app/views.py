from django.urls import reverse_lazy
from django.shortcuts import render
from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Author, Category, Post, Comment
from .filters import PostFilter
from .forms import PostForm


class PostList(ListView):
    model = Post
    ordering = '-date_create'
    template_name = 'blog.html'
    context_object_name = 'post_list'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    ordering = 'post_title'
    template_name = 'post.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_form.html'


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_form.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')