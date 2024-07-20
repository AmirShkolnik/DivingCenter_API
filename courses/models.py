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
    PRICE_CHOICES = [
        (2000, '2000 $'),
        (5000, '5000 $'),
        (8000, '8000 $'),
        (12000, '12000 $'),
        (15000, '15000 $'),
    ]
    title = models.CharField(max_length=100, blank=False, null=False)
    slug = models.SlugField(unique=True, max_length=100, blank=True)
    excerpt = models.TextField(max_length=200, blank=False, null=False)
    description = HTMLField(blank=False, null=False)
    course_type = models.CharField(
        max_length=3, choices=COURSE_TYPES, blank=False, null=False
    )
    image = CloudinaryField('image', blank=False, null=False)
    price = models.IntegerField(
        choices=PRICE_CHOICES, default=2000, blank=False, null=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)

    def generate_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Course.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def __str__(self):
        return self.title


class Review(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='reviews'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('course', 'user')

    def __str__(self):
        return f"{self.user.username}'s review for {self.course.title}"
