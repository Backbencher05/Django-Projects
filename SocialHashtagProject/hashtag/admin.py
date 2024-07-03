from django.contrib import admin
from hashtag.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'body','click_count', 'publish', 'created', 'updated', 'status', 'tags']
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Post,PostAdmin)