from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'created_at', 'updated_at', 'image_filter')
    search_fields = ('title', 'content', 'owner__username')
    list_filter = ('created_at', 'updated_at', 'owner', 'image_filter')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'image', 'image_filter')
        }),
        ('Owner Info', {
            'fields': ('owner',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )