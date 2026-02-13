from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId


class ObjectIdField(serializers.Field):
    """Custom field to convert ObjectId to string"""
    def to_representation(self, value):
        return str(value)
    
    def to_internal_value(self, data):
        try:
            return ObjectId(data)
        except Exception:
            raise serializers.ValidationError('Invalid ObjectId')


class UserSerializer(serializers.ModelSerializer):
    id = ObjectIdField(source='_id', read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'team', 'total_points', 'created_at', 'updated_at']
        extra_kwargs = {
            'password': {'write_only': True},
            '_id': {'read_only': True}
        }

    def create(self, validated_data):
        # Hash password before saving in production
        return User.objects.create(**validated_data)


class TeamSerializer(serializers.ModelSerializer):
    id = ObjectIdField(source='_id', read_only=True)
    
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'total_points', 'member_count', 'created_at', 'updated_at']
        extra_kwargs = {
            '_id': {'read_only': True}
        }


class ActivitySerializer(serializers.ModelSerializer):
    id = ObjectIdField(source='_id', read_only=True)
    
    class Meta:
        model = Activity
        fields = ['id', 'user_id', 'user_name', 'activity_type', 'duration', 'distance', 
                  'calories', 'points', 'date', 'created_at']
        extra_kwargs = {
            '_id': {'read_only': True}
        }


class LeaderboardSerializer(serializers.ModelSerializer):
    id = ObjectIdField(source='_id', read_only=True)
    
    class Meta:
        model = Leaderboard
        fields = ['id', 'user_id', 'user_name', 'team', 'total_points', 'rank', 
                  'activities_count', 'last_activity']
        extra_kwargs = {
            '_id': {'read_only': True}
        }


class WorkoutSerializer(serializers.ModelSerializer):
    id = ObjectIdField(source='_id', read_only=True)
    
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'category', 'difficulty', 'duration', 
                  'calories_estimate', 'points', 'equipment', 'instructions']
        extra_kwargs = {
            '_id': {'read_only': True}
        }
