from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import (
    UserSerializer, 
    TeamSerializer, 
    ActivitySerializer, 
    LeaderboardSerializer, 
    WorkoutSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'])
    def by_team(self, request):
        """Get users by team"""
        team = request.query_params.get('team', None)
        if team:
            users = User.objects.filter(team=team)
            serializer = self.get_serializer(users, many=True)
            return Response(serializer.data)
        return Response({'error': 'Team parameter required'}, status=status.HTTP_400_BAD_REQUEST)


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    @action(detail=True, methods=['get'])
    def members(self, request, pk=None):
        """Get team members"""
        team = self.get_object()
        users = User.objects.filter(team=team.name)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    @action(detail=False, methods=['get'])
    def by_user(self, request):
        """Get activities by user"""
        user_id = request.query_params.get('user_id', None)
        if user_id:
            activities = Activity.objects.filter(user_id=user_id)
            serializer = self.get_serializer(activities, many=True)
            return Response(serializer.data)
        return Response({'error': 'user_id parameter required'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def recent(self, request):
        """Get recent activities"""
        limit = int(request.query_params.get('limit', 10))
        activities = Activity.objects.all()[:limit]
        serializer = self.get_serializer(activities, many=True)
        return Response(serializer.data)


class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

    @action(detail=False, methods=['get'])
    def top(self, request):
        """Get top users"""
        limit = int(request.query_params.get('limit', 10))
        leaders = Leaderboard.objects.all()[:limit]
        serializer = self.get_serializer(leaders, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_team(self, request):
        """Get leaderboard by team"""
        team = request.query_params.get('team', None)
        if team:
            leaders = Leaderboard.objects.filter(team=team)
            serializer = self.get_serializer(leaders, many=True)
            return Response(serializer.data)
        return Response({'error': 'team parameter required'}, status=status.HTTP_400_BAD_REQUEST)


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    @action(detail=False, methods=['get'])
    def by_category(self, request):
        """Get workouts by category"""
        category = request.query_params.get('category', None)
        if category:
            workouts = Workout.objects.filter(category=category)
            serializer = self.get_serializer(workouts, many=True)
            return Response(serializer.data)
        return Response({'error': 'category parameter required'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def by_difficulty(self, request):
        """Get workouts by difficulty"""
        difficulty = request.query_params.get('difficulty', None)
        if difficulty:
            workouts = Workout.objects.filter(difficulty=difficulty)
            serializer = self.get_serializer(workouts, many=True)
            return Response(serializer.data)
        return Response({'error': 'difficulty parameter required'}, status=status.HTTP_400_BAD_REQUEST)
