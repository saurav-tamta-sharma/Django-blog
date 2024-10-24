from django.contrib import admin
from .models import Post
# Register your models here.


@admin.register(Post)  # Registering the Post model
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')  # Fields to display in the list view
    search_fields = ('title',)  # Fields to search within the admin panel
