from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField

class Course(models.Model):
    COURSE_TYPES = [
        ('OW', 'Open Water'),
        ('AOW', 'Advanced Open Water'),
        ('RD', 'Rescue Diver'),
    ]
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100, blank=True)
    description = HTMLField()
    course_type = models.CharField(max_length=3, choices=COURSE_TYPES)
    image = CloudinaryField('image', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        
        # Ensure uniqueness of slug
        original_slug = self.slug
        count = 1
        while Course.objects.filter(slug=self.slug).exists():
            self.slug = f"{original_slug}-{count}"
            count += 1
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('course', 'user')

    def __str__(self):
        return f"{self.user.username}'s review for {self.course.title}"