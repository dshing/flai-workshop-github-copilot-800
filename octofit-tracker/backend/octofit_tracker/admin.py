from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'team', 'total_points', 'created_at')
    list_filter = ('team', 'created_at')
    search_fields = ('name', 'email')
    ordering = ('-total_points',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_points', 'member_count', 'created_at')
    search_fields = ('name',)
    ordering = ('-total_points',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'activity_type', 'duration', 'calories', 'points', 'date')
    list_filter = ('activity_type', 'date')
    search_fields = ('user_name', 'activity_type')
    ordering = ('-date',)


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('rank', 'user_name', 'team', 'total_points', 'activities_count')
    list_filter = ('team',)
    search_fields = ('user_name',)
    ordering = ('rank',)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'difficulty', 'duration', 'calories_estimate', 'points')
    list_filter = ('category', 'difficulty')
    search_fields = ('name', 'category')
    ordering = ('name',)
