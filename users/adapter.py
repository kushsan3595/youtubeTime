from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    """
    Custom adapter to simplify signup process and override email verification
    """
    
    def is_open_for_signup(self, request):
        """
        Allow signup for all users
        """
        return True
    
    def save_user(self, request, user, form, commit=True):
        """
        Save the user and auto-verify email
        """
        user = super().save_user(request, user, form, commit=False)
        user.is_active = True  # Make user active immediately
        if commit:
            user.save()
        return user 