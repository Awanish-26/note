from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ['created_on',]
    prepopulated_fields = {'slug': ('title',)}
