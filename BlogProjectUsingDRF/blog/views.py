from django.shortcuts import render
from django.views.generic import TemplateView, ListView
import datetime
from blog.models import Post
# Create your views here.
def homepage(request):
    return render(request, 'blog/base.html')


class PostListView(ListView):
    model = Post




