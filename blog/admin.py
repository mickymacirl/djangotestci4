from django.contrib import admin
from .models import Post

# The PostAdmin class inherits from ModelAdmin, and defines a list_display, list_filter,
# search_fields, and prepopulated_fields
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

# Registering the Post model with the PostAdmin class.
admin.site.register(Post, PostAdmin)