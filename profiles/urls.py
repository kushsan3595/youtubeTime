from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.ProfileDetailView.as_view(), name='profile-detail'),
    path('<int:pk>/edit/', views.ProfileUpdateView.as_view(), name='profile-update'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('videos/new/', views.YouTubeVideoCreateView.as_view(), name='video-create'),
    path('videos/<int:pk>/', views.YouTubeVideoDetailView.as_view(), name='video-detail'),
    path('videos/<int:pk>/edit/', views.YouTubeVideoUpdateView.as_view(), name='video-update'),
    path('videos/<int:pk>/delete/', views.YouTubeVideoDeleteView.as_view(), name='video-delete'),
    path('ad-click/', views.record_ad_click, name='ad-click'),
] 