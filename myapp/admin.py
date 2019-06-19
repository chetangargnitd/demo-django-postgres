from django.contrib import admin

from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
	readonly_fields = ('created',)
	list_display = ['title', 'likes', 'stars', 'created']

admin.site.register(Post, PostAdmin)