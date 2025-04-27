from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserActivity


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets


class UserActivityAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'time_spent', 'ad_impressions', 'ad_clicks', 'earnings']
    list_filter = ['date', 'user']
    search_fields = ['user__username', 'user__email']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserActivity, UserActivityAdmin) 