import uuid

from django.db import models


class Courses(models.Model):
    PROGRAM_TYPES = [
        ('new_driver_full_program', 'New driver full program'),
        ('hour_lesson', 'Lessons by the hour'),
        ('road_test_preparation', 'Road test preparation'),
        ('refresher_driver_training', 'Refresher driver training')
    ]

    TITLES = [
        ('sat_class', 'Saturday Class'),
        ('day_class', 'Day Class'),
        ('evening_class', 'Evening Class'),
        ('sat_sun_class', 'Sat. & San. Class'),
        ('christmas_break_class', 'Christmas Break Class')
    ]

    STATUS = [
        ('online', 'Online'),
        ('in_person', 'In Person')
    ]

    title = models.CharField(choices=TITLES, null=True)
    status = models.CharField(choices=STATUS, null=True, default='in_person')
    description = models.TextField(null=True, blank=True)
    cost = models.IntegerField(null=True)
    date_start = models.DateField(null=True)
    spaces_remaining = models.IntegerField(null=True)
    type_program = models.CharField(choices=PROGRAM_TYPES, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title
