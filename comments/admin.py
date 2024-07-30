from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'post', 'created_at', 'updated_at', 'content')
    list_filter = ('created_at', 'updated_at', 'owner')
    search_fields = ('owner__username', 'content')
    raw_id_fields = ('owner', 'post')
    date_hierarchy = 'created_at'