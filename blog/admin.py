from django.contrib import admin

from blog.models import Category, Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'category', 'created_at')
    search_fields = ['id', 'name', 'content', 'status']
    list_filter = ['status', 'category', 'created_at']

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
