from django.contrib import admin
from .models import Post

# The PostAdmin class inherits from ModelAdmin, and defines a list_display, list_filter,
# search_fields, and prepopulated_fields
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'author', 'created_on', 'category',)
    list_filter = ("status", "author", "created_on", 'category',)
    search_fields = ['title', 'content', 'category',]
    prepopulated_fields = {'slug': ('title',)}

    # Add an action to mark posts as published
    def make_published(self, request, queryset):
        rows_updated = queryset.update(status='1')
        if rows_updated == 1:
            message_bit = "1 post was"
        else:
            message_bit = f"{rows_updated} posts were"
        self.message_user(request, f"{message_bit} successfully published!")
    make_published.short_description = "Set selected posts to published"

    # Add an action to mark posts as drafts
    def make_draft(self, request, queryset):
        rows_updated = queryset.update(status='0')
        if rows_updated == 1:
            message_bit = "1 post was"
        else:
            message_bit = f"{rows_updated} posts were"
        self.message_user(request, f"{message_bit} successfully marked as drafts.")
    make_draft.short_description = "Set selected posts to draft"

    # Add a save and continue editing button on the edit form
    save_on_top = True
    save_as = True
    actions = ['make_published', 'make_draft']

    # Add an action to mark posts as disabled
    def make_disabled(self, request, queryset):
        rows_updated = queryset.update(status='3')
        if rows_updated == 1:
            message_bit = "1 post was"
        else:
            message_bit = f"{rows_updated} posts were"
        self.message_user(request, f"{message_bit} successfully marked as disabled.")
        make_disabled.short_description = "Set selected posts as disabled"

    # Add a save and continue editing button on the edit form
    save_on_top = True
    save_as = True
    actions = ['make_published', 'make_draft', 'make_disabled']
#class CategoryAdmin(admin.ModelAdmin):
#    list_display = ('title', 'slug', 'description', 'status_cat', 'updated_on')
#    list_filter = ("title", "slug", "description", "status_cat", "updated_on")
#    search_fields = ['title', 'description']
#    prepopulated_fields = {'slug': ('title',)}


# Registering the Post model with the PostAdmin class.
admin.site.register(Post, PostAdmin)
# admin.site.register(Category, CategoryAdmin)
