from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            name="Test User",
            email="test@example.com",
            password="testpass123",
            team="Team Marvel",
            total_points=100
        )

    def test_user_creation(self):
        self.assertEqual(self.user.name, "Test User")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.team, "Team Marvel")
        self.assertEqual(self.user.total_points, 100)

    def test_user_str(self):
        self.assertEqual(str(self.user), "Test User")


class TeamModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(
            name="Team Marvel",
            description="Marvel superheroes",
            total_points=500,
            member_count=5
        )

    def test_team_creation(self):
        self.assertEqual(self.team.name, "Team Marvel")
        self.assertEqual(self.team.description, "Marvel superheroes")
        self.assertEqual(self.team.total_points, 500)
        self.assertEqual(self.team.member_count, 5)

    def test_team_str(self):
        self.assertEqual(str(self.team), "Team Marvel")


class ActivityModelTest(TestCase):
    def setUp(self):
        self.activity = Activity.objects.create(
            user_id="507f1f77bcf86cd799439011",
            user_name="Test User",
            activity_type="Running",
            duration=30,
            distance=5.0,
            calories=300,
            points=50,
            date=datetime.now()
        )

    def test_activity_creation(self):
        self.assertEqual(self.activity.user_name, "Test User")
        self.assertEqual(self.activity.activity_type, "Running")
        self.assertEqual(self.activity.duration, 30)
        self.assertEqual(self.activity.calories, 300)


class UserAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'name': 'API Test User',
            'email': 'api@test.com',
            'password': 'testpass123',
            'team': 'Team Marvel',
            'total_points': 0
        }

    def test_create_user(self):
        response = self.client.post('/api/users/', self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().name, 'API Test User')

    def test_get_users(self):
        User.objects.create(**self.user_data)
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class TeamAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.team_data = {
            'name': 'Team Marvel',
            'description': 'Marvel superheroes',
            'total_points': 0,
            'member_count': 0
        }

    def test_create_team(self):
        response = self.client.post('/api/teams/', self.team_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 1)

    def test_get_teams(self):
        Team.objects.create(**self.team_data)
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ActivityAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.activity_data = {
            'user_id': '507f1f77bcf86cd799439011',
            'user_name': 'Test User',
            'activity_type': 'Running',
            'duration': 30,
            'distance': 5.0,
            'calories': 300,
            'points': 50,
            'date': datetime.now().isoformat()
        }

    def test_create_activity(self):
        response = self.client.post('/api/activities/', self.activity_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_activities(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LeaderboardAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_leaderboard(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class WorkoutAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.workout_data = {
            'name': 'Morning Run',
            'description': 'A refreshing morning run',
            'category': 'Cardio',
            'difficulty': 'beginner',
            'duration': 30,
            'calories_estimate': 300,
            'points': 50,
            'equipment': ['Running shoes'],
            'instructions': ['Warm up', 'Run', 'Cool down']
        }

    def test_create_workout(self):
        response = self.client.post('/api/workouts/', self.workout_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_workouts(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
