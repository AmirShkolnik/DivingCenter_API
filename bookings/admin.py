from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'date', 'time', 'created_at')
    list_filter = ('course', 'date', 'time')
    search_fields = ('user__username', 'course__title', 'additional_info')
    date_hierarchy = 'date'