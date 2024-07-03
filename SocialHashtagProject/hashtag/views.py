from django.shortcuts import render, get_object_or_404
from hashtag.models import Post
from taggit.models import Tag
# Create your views here.




def PostListView(request,tag_slug=None):
    post_list = Post.objects.all()
    tag = None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        post_list=post_list.filter(tags__in=[tag])


    return render(request, 'hashtag/post_list.html', {'post_list': post_list, 'tag': tag})


def post_detail_view(request,year,month,day,post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    
    return render(request, 'hashtag/post_detail.html', {'post': post})
