from django.contrib import admin
from .models import *


# Register your models here.
class PostsAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_text', 'created_date', 'published_date']
    list_filter = ['title', 'created_date', 'published_date', 'published_date']

admin.site.register(Post, PostsAdmin)
