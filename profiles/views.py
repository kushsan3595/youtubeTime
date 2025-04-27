from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Profile, YouTubeVideo
from .forms import ProfileForm, YouTubeVideoForm
from users.models import UserActivity
from django.utils import timezone
from decimal import Decimal


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'
    context_object_name = 'profile'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        videos = YouTubeVideo.objects.filter(profile=self.object).order_by('-created_at')
        context['videos'] = videos
        
        # Calculate total views
        total_views = sum(video.views for video in videos)
        context['total_views'] = total_views
        
        return context


class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profiles/profile_form.html'
    
    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user
    
    def form_valid(self, form):
        messages.success(self.request, 'Your profile has been updated!')
        return super().form_valid(form)


class YouTubeVideoCreateView(LoginRequiredMixin, CreateView):
    model = YouTubeVideo
    form_class = YouTubeVideoForm
    template_name = 'profiles/video_form.html'
    
    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        messages.success(self.request, 'Your YouTube video has been added!')
        return super().form_valid(form)


class YouTubeVideoDetailView(DetailView):
    model = YouTubeVideo
    template_name = 'profiles/video_detail.html'
    context_object_name = 'video'
    
    def get(self, request, *args, **kwargs):
        video = self.get_object()
        video.views += 1
        video.save()
        
        # Record ad impression
        if request.user.is_authenticated:
            today = timezone.now().date()
            activity, _ = UserActivity.objects.get_or_create(
                user=request.user,
                date=today,
            )
            activity.ad_impressions += 1
            # Calculate earnings (simple model: $0.001 per impression)
            # Convert float to Decimal to avoid type mismatch
            activity.earnings += Decimal('0.001')
            activity.save()
            
        return super().get(request, *args, **kwargs)


class YouTubeVideoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = YouTubeVideo
    form_class = YouTubeVideoForm
    template_name = 'profiles/video_form.html'
    
    def test_func(self):
        video = self.get_object()
        return self.request.user == video.profile.user
    
    def form_valid(self, form):
        messages.success(self.request, 'Your YouTube video has been updated!')
        return super().form_valid(form)


class YouTubeVideoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = YouTubeVideo
    template_name = 'profiles/video_confirm_delete.html'
    success_url = reverse_lazy('profile-detail')
    
    def test_func(self):
        video = self.get_object()
        return self.request.user == video.profile.user
    
    def get_success_url(self):
        return reverse_lazy('profile-detail', kwargs={'pk': self.request.user.profile.pk})
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Your YouTube video has been deleted!')
        return super().delete(request, *args, **kwargs)


def dashboard(request):
    """Dashboard view showing user's screen time and earnings"""
    if not request.user.is_authenticated:
        return redirect('account_login')
    
    # Get user's activity data
    activities = UserActivity.objects.filter(user=request.user).order_by('-date')
    total_time = sum((a.time_spent for a in activities), timezone.timedelta())
    total_earnings = sum(a.earnings for a in activities)
    
    context = {
        'activities': activities[:30],  # Last 30 days
        'total_time': total_time,
        'total_earnings': total_earnings,
    }
    
    return render(request, 'profiles/dashboard.html', context)


@require_POST
@csrf_exempt
def record_ad_click(request):
    """Record when a user clicks on an ad"""
    if request.user.is_authenticated:
        today = timezone.now().date()
        activity, _ = UserActivity.objects.get_or_create(
            user=request.user,
            date=today,
        )
        activity.ad_clicks += 1
        # Calculate earnings (simple model: $0.01 per click)
        # Convert float to Decimal to avoid type mismatch
        activity.earnings += Decimal('0.01')
        activity.save()
        return JsonResponse({'status': 'success', 'message': 'Ad click recorded'})
    return JsonResponse({'status': 'error', 'message': 'User not authenticated'}, status=401) 