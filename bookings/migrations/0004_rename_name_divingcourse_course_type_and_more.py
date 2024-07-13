from django.db import migrations, models

def remove_duplicates(apps, schema_editor):
    Booking = apps.get_model('bookings', 'Booking')
    duplicates = Booking.objects.values('course', 'date', 'time').annotate(count=models.Count('id')).filter(count__gt=1)
    for duplicate in duplicates:
        bookings = Booking.objects.filter(course=duplicate['course'], date=duplicate['date'], time=duplicate['time'])
        bookings.exclude(id=bookings.first().id).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_alter_divingcourse_name'),
    ]

    operations = [
        migrations.RunPython(remove_duplicates),
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together={('course', 'date', 'time')},
        ),
    ]
