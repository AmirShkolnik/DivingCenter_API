from django.db import models
from django.contrib.auth.models import User

class DivingCourse(models.Model):
    COURSE_CHOICES = [
        ('OW', 'Open Water'),
        ('AOW', 'Advanced Open Water'),
        ('RD', 'Rescue Diver'),
    ]
    name = models.CharField(max_length=3, choices=COURSE_CHOICES, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.get_name_display()
        

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    course = models.ForeignKey(DivingCourse, on_delete=models.CASCADE, null=True, blank=True)
    additional_info = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.name if self.course else 'No course'} on {self.date} at {self.time}"