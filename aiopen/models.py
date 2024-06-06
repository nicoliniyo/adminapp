from django.utils import timezone

from django.contrib.auth.models import User
from django.db import models

from .constants import default_engine


# Create your models here.
class Task(models.Model):
    input_value = models.CharField(max_length=100)

    # Timestamp field with default value of current time
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # String field for engine
    engine = models.CharField(max_length=50, default=default_engine)  # Adjust max_length as needed

    def __str__(self):
        formatted_date = self.created_at.strftime("%Y/%m/%d %H:%M:%S")
        return f"{self.pk}, {self.input_value}, formatted_date, {self.created_by}, {self.engine}"
class Answer(models.Model):
    answer_value = models.TextField(blank=False)

    # Timestamp field with default value of current time
    created_at = models.DateTimeField(default=timezone.now)
    # created_by_user = models.ForeignKey(User, on_delete=models.CASCADE)
    # String field for engine
    engine = models.CharField(max_length=50, default=default_engine)  # Adjust max_length as needed
    # Foreign key to Task model
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        formatted_date = self.created_at.strftime("%Y/%m/%d %H:%M:%S")
        return f"{self.pk}, {self.answer_value[:15]}..., {formatted_date}, {self.engine}, {self.task.id}"


