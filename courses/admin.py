from django.contrib import admin
from .models import Course, Review

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0
    readonly_fields = ('user', 'content', 'rating', 'created_at', 'updated_at')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'course_type', 'average_rating', 'created_at', 'updated_at')
    list_filter = ('course_type', 'created_at')
    search_fields = ('title', 'description')
    inlines = [ReviewInline]

    def average_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews:
            return sum(review.rating for review in reviews) / len(reviews)
        return 0
    average_rating.short_description = 'Avg Rating'

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'rating', 'created_at', 'updated_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('user__username', 'course__title', 'content')
    readonly_fields = ('created_at', 'updated_at')
