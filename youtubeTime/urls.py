from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from users.views import SignupView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/signup/', SignupView.as_view(), name='account_signup'),  # Override allauth signup
    path('accounts/', include('allauth.urls')),
    path('profiles/', include('profiles.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 