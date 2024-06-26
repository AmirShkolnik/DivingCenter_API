from django.core.management.base import BaseCommand
from bookings.models import DivingCourse

class Command(BaseCommand):
    help = 'Creates initial diving courses'

    def handle(self, *args, **kwargs):
        courses = [
            {"name": "OW", "description": "Open Water: Entry-level scuba certification course."},
            {"name": "AOW", "description": "Advanced Open Water: The next step in your diving education."},
            {"name": "RD", "description": "Rescue Diver: Learn to prevent and manage problems in the water."},
        ]

        for course in courses:
            DivingCourse.objects.get_or_create(name=course['name'], defaults={'description': course['description']})

        self.stdout.write(self.style.SUCCESS('Successfully created diving courses'))