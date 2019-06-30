from django.contrib import admin
from . models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
	"""	Represent admin field configuration for post model"""
	list_display = ('author', 'title', 'date_created', 'date_published')

admin.site.register(Post, PostAdmin)