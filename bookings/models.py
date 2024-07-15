from django.db import models
from django.contrib.auth.models import User
from courses.models import Course

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    additional_info = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        course_name = self.course.title if self.course else 'No course'
        return f"{self.user.username} - {course_name} on {self.date} at {self.time}"