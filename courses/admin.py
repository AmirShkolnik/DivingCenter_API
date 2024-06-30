from django.contrib import admin
from django.db import models
from django.utils.safestring import mark_safe
from .models import Course, Review
from tinymce.widgets import TinyMCE

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0
    readonly_fields = ('user', 'content', 'rating', 'created_at', 'updated_at')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'course_type', 'price', 'get_average_rating', 'created_at', 'updated_at')
    list_filter = ('course_type', 'price', 'created_at')
    search_fields = ('title', 'slug', 'description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ReviewInline]
    readonly_fields = ('image_preview',)

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'description':
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
                mce_attrs=self.get_tinymce_config()
            ))
        return super().formfield_for_dbfield(db_field, **kwargs)

    def get_tinymce_config(self):
        return {
            'theme': 'silver',
            'height': 500,
            'plugins': [
                'advlist autolink lists link image charmap print preview anchor',
                'searchreplace visualblocks code fullscreen',
                'insertdatetime media table paste code help wordcount'
            ],
            'toolbar': 'undo redo | formatselect | bold italic backcolor | \
                        alignleft aligncenter alignright alignjustify | \
                        bullist numlist outdent indent | removeformat | help'
        }

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="150" height="150" style="object-fit: cover;" />')
        return "No Image"
    image_preview.short_description = 'Image Preview'

    def get_average_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews:
            return sum(review.rating for review in reviews) / len(reviews)
        return 0
    get_average_rating.short_description = 'Avg Rating'

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'rating', 'created_at', 'updated_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('user__username', 'course__title', 'content')
    readonly_fields = ('created_at', 'updated_at')
