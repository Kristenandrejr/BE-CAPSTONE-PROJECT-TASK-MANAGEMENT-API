from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Custom User model
class User(AbstractUser):
    email = models.EmailField(unique=True)

# Task model
class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    ]

    CATEGORY_CHOICES = [
        ('Work', 'Work'),
        ('Personal', 'Personal'),
        ('Other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    completed_at = models.DateTimeField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Other')
    recurring = models.BooleanField(default=False)
    recurrence_interval = models.CharField(max_length=50, blank=True, null=True, help_text="E.g., daily, weekly")

    def save(self, *args, **kwargs):
        if self.status == 'Completed' and not self.completed_at:
            self.completed_at = timezone.now()
        elif self.status == 'Pending':
            self.completed_at = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

# Task History model
class TaskHistory(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='history')
    status = models.CharField(max_length=10, choices=Task.STATUS_CHOICES)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.task.title} - {self.status} at {self.updated_at}"
