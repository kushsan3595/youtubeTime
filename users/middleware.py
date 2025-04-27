from django.utils import timezone
from datetime import timedelta
import datetime
from .models import UserActivity


class UserActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Process the request
        if request.user.is_authenticated:
            current_time = timezone.now()
            today = timezone.now().date()
            
            # Get or create today's activity record
            activity, created = UserActivity.objects.get_or_create(
                user=request.user,
                date=today,
            )
            
            # If not a fresh session, calculate time spent
            if not created and activity.last_activity:
                # Only add time if last activity was within the last 5 minutes
                time_diff = current_time - activity.last_activity
                if time_diff < timedelta(minutes=5):
                    activity.time_spent += time_diff
            
            # Update last activity time
            activity.last_activity = current_time
            activity.save()
            
        response = self.get_response(request)
        return response 