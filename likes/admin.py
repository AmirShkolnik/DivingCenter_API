from django.contrib import admin
from .models import Like

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'post', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('owner__username', 'post__title')
    date_hierarchy = 'created_at'

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('owner', 'post')