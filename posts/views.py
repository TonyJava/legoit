from django.shortcuts import render
from django.views.generic import ListView

from .models import Post

class HomeView(ListView):
    model = Post
    template_name = "posts/post_list.jinja"
    paginate_by = 20
