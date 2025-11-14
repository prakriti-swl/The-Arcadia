from django.utils import timezone
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.views import View

from dashboard.forms import PostForm, CategoryForm, TagForm
from arcadia_app.models import Category, Post, Tag
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView

class DashboardView(TemplateView):
    template_name = "admin/dash_base.html"


class PublishedPost(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "admin/published_post.html"
    queryset = Post.objects.filter(published_at__isnull= False , status = "active" ).order_by("-published_at")

class CategoryView(ListView):
    model = Category
    context_object_name= "categories"
    template_name = "admin/categories.html"
    queryset = Category.objects.all()


class TagView(ListView):
    model = Tag
    context_object_name = "tags"
    template_name = "admin/tag.html"
    queryset = Tag.objects.all()



# for post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "admin/post_create.html"
    form_class = PostForm
    success_url = reverse_lazy("published-post")

    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return redirect("published-post")

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "admin/post_create.html"
    form_class = PostForm

    def get_success_url(self):
        post = self.get_object()
        if post.published_at:
            return reverse_lazy("published-post")
        else:
            return reverse_lazy("draft")
        

class DashPostDetailView(DetailView):
    model = Post
    template_name = "admin/dashpost_detail.html"
    context_object_name = "post"

    def get_queryset(self):
        queryset = Post.objects.filter(pk=self.kwargs["pk"], published_at__isnull = False)
        return queryset



# for tags

class TagCreateView(LoginRequiredMixin, CreateView):
    model = Tag
    template_name = "admin/post_create.html"
    form_class = TagForm
    success_url = reverse_lazy("tag")

    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TagDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        tag = Tag.objects.get(pk=pk)
        tag.delete()
        return redirect("tag")
    

class TagUpdateView(LoginRequiredMixin, UpdateView):
    model = Tag
    template_name = "admin/post_create.html"
    form_class = TagForm

    success_url = reverse_lazy("tag")
    


# for category
class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = "admin/post_create.html"
    form_class = CategoryForm
    success_url = reverse_lazy("category")

    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CategoryDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        category = Category.objects.get(pk=pk)
        category.delete()
        return redirect("category")
    
class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    template_name = "admin/post_create.html"
    form_class = CategoryForm

    success_url = reverse_lazy("category")
    
    



