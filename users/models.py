from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    """Custom user model with additional fields"""
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.username

class UserActivity(models.Model):
    """Model to track user activity and screen time"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='activities')
    date = models.DateField(default=timezone.now)
    time_spent = models.DurationField(default=timezone.timedelta)
    last_activity = models.DateTimeField(default=timezone.now)
    ad_impressions = models.PositiveIntegerField(default=0)
    ad_clicks = models.PositiveIntegerField(default=0)
    earnings = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    
    class Meta:
        verbose_name_plural = 'User Activities'
        unique_together = ['user', 'date']
    
    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.time_spent}" 