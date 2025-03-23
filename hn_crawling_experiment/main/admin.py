from django.contrib import admin

# Register your models here.
from main.models import StoryData
from .models import Post

admin.site.register(StoryData)
admin.site.register(Post)
