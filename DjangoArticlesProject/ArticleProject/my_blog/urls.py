from django.urls import path
from . import views
urlpatterns = [
    # we are giving name , so that if we are using paricular name we can directly call it using name 
    path('',views.landing_page, name= "landing_page"),
    path('posts',views.posts, name="post_page" ),
    path('posts/<slug:slug>',views.post_detail, name="detail_posts_page"),
    
]