from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    COURSE_TYPES = [
        ('OW', 'Open Water'),
        ('AOW', 'Advanced Open Water'),
        ('RD', 'Rescue Diver'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    course_type = models.CharField(max_length=3, choices=COURSE_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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