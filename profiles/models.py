from django.db import models
from django.conf import settings
from django.urls import reverse
import re


class Profile(models.Model):
    """User profile model"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    payment_info = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s profile"
    
    def get_absolute_url(self):
        return reverse('profile-detail', kwargs={'pk': self.pk})


class YouTubeVideo(models.Model):
    """YouTube video model"""
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(max_length=255)
    url = models.URLField()
    youtube_id = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True)
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # Extract YouTube ID from URL
        pattern = r'(?:youtube\.com\/(?:[^\/]+\/.+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([^"&?\/\s]{11})'
        match = re.search(pattern, self.url)
        if match:
            self.youtube_id = match.group(1)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('video-detail', kwargs={'pk': self.pk})
    
    def get_embed_url(self):
        return f"https://www.youtube.com/embed/{self.youtube_id}" 