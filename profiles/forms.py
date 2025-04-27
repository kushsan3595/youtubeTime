from django import forms
from .models import Profile, YouTubeVideo


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar', 'payment_info']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'payment_info': 'Payment Information (PayPal email etc.)',
        }


class YouTubeVideoForm(forms.ModelForm):
    class Meta:
        model = YouTubeVideo
        fields = ['title', 'url', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'url': forms.URLInput(attrs={
                'placeholder': 'https://www.youtube.com/watch?v=...',
            }),
        }
        help_texts = {
            'url': 'Enter the full YouTube video URL',
        } 