from django.contrib import admin
from .models import Profile, YouTubeVideo


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'updated_at']
    search_fields = ['user__username', 'user__email', 'bio']


class YouTubeVideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'profile', 'youtube_id', 'views', 'created_at']
    list_filter = ['created_at', 'profile']
    search_fields = ['title', 'description', 'youtube_id', 'profile__user__username']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(YouTubeVideo, YouTubeVideoAdmin) 