from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Clearing existing data...'))
        
        # Delete existing data using Django ORM
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        
        self.stdout.write(self.style.SUCCESS('Existing data cleared!'))
        self.stdout.write(self.style.WARNING('Creating test data...'))
        
        # Create Teams
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Earth\'s Mightiest Heroes',
            total_points=0,
            member_count=0
        )
        
        team_dc = Team.objects.create(
            name='Team DC',
            description='Justice League Champions',
            total_points=0,
            member_count=0
        )
        
        self.stdout.write(self.style.SUCCESS(f'Created team: {team_marvel.name}'))
        self.stdout.write(self.style.SUCCESS(f'Created team: {team_dc.name}'))
        
        # Create Marvel Users
        marvel_users = [
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'password': 'stark123', 'team': 'Team Marvel'},
            {'name': 'Captain America', 'email': 'captainamerica@marvel.com', 'password': 'shield123', 'team': 'Team Marvel'},
            {'name': 'Thor', 'email': 'thor@marvel.com', 'password': 'asgard123', 'team': 'Team Marvel'},
            {'name': 'Black Widow', 'email': 'blackwidow@marvel.com', 'password': 'natasha123', 'team': 'Team Marvel'},
            {'name': 'Hulk', 'email': 'hulk@marvel.com', 'password': 'gamma123', 'team': 'Team Marvel'},
            {'name': 'Spider-Man', 'email': 'spiderman@marvel.com', 'password': 'web123', 'team': 'Team Marvel'},
        ]
        
        # Create DC Users
        dc_users = [
            {'name': 'Superman', 'email': 'superman@dc.com', 'password': 'krypton123', 'team': 'Team DC'},
            {'name': 'Batman', 'email': 'batman@dc.com', 'password': 'gotham123', 'team': 'Team DC'},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'password': 'themyscira123', 'team': 'Team DC'},
            {'name': 'Flash', 'email': 'flash@dc.com', 'password': 'speed123', 'team': 'Team DC'},
            {'name': 'Aquaman', 'email': 'aquaman@dc.com', 'password': 'atlantis123', 'team': 'Team DC'},
            {'name': 'Green Lantern', 'email': 'greenlantern@dc.com', 'password': 'willpower123', 'team': 'Team DC'},
        ]
        
        all_users = []
        
        # Insert Marvel users
        for user_data in marvel_users:
            user = User.objects.create(**user_data, total_points=0)
            all_users.append(user)
            self.stdout.write(self.style.SUCCESS(f'Created user: {user.name}'))
        
        # Insert DC users
        for user_data in dc_users:
            user = User.objects.create(**user_data, total_points=0)
            all_users.append(user)
            self.stdout.write(self.style.SUCCESS(f'Created user: {user.name}'))
        
        # Create Activities
        activity_types = ['Running', 'Cycling', 'Swimming', 'Weightlifting', 'Yoga', 'Boxing', 'CrossFit']
        
        for user in all_users:
            num_activities = random.randint(3, 8)
            for i in range(num_activities):
                activity_type = random.choice(activity_types)
                duration = random.randint(20, 90)
                distance = round(random.uniform(2.0, 15.0), 2) if activity_type in ['Running', 'Cycling', 'Swimming'] else None
                calories = duration * random.randint(8, 15)
                points = calories // 10
                
                activity = Activity.objects.create(
                    user_id=str(user._id),
                    user_name=user.name,
                    activity_type=activity_type,
                    duration=duration,
                    distance=distance,
                    calories=calories,
                    points=points,
                    date=datetime.now() - timedelta(days=random.randint(0, 30))
                )
                
                # Update user total points
                user.total_points += points
                user.save()
        
        self.stdout.write(self.style.SUCCESS(f'Created activities for all users'))
        
        # Update team statistics
        for team in [team_marvel, team_dc]:
            team_users = User.objects.filter(team=team.name)
            team.member_count = team_users.count()
            team.total_points = sum(user.total_points for user in team_users)
            team.save()
            self.stdout.write(self.style.SUCCESS(f'Updated team stats: {team.name}'))
        
        # Create Leaderboard entries
        all_users = User.objects.all().order_by('-total_points')
        for rank, user in enumerate(all_users, start=1):
            activities_count = Activity.objects.filter(user_id=str(user._id)).count()
            last_activity_obj = Activity.objects.filter(user_id=str(user._id)).order_by('-date').first()
            last_activity = last_activity_obj.date if last_activity_obj else None
            
            Leaderboard.objects.create(
                user_id=str(user._id),
                user_name=user.name,
                team=user.team,
                total_points=user.total_points,
                rank=rank,
                activities_count=activities_count,
                last_activity=last_activity
            )
        
        self.stdout.write(self.style.SUCCESS('Created leaderboard entries'))
        
        # Create Workouts
        workouts = [
            {
                'name': 'Super Soldier Training',
                'description': 'Captain America\'s intense full-body workout',
                'category': 'Strength',
                'difficulty': 'advanced',
                'duration': 60,
                'calories_estimate': 600,
                'points': 60,
                'equipment': ['Dumbbells', 'Pull-up bar', 'Resistance bands'],
                'instructions': ['Warm up 10 min', 'Push-ups 4x25', 'Pull-ups 4x15', 'Squats 4x20', 'Cool down']
            },
            {
                'name': 'Speed Force Sprint',
                'description': 'Flash-inspired HIIT cardio workout',
                'category': 'Cardio',
                'difficulty': 'intermediate',
                'duration': 30,
                'calories_estimate': 400,
                'points': 40,
                'equipment': ['Running shoes'],
                'instructions': ['Warm up 5 min', 'Sprint 30s', 'Walk 60s', 'Repeat 10x', 'Cool down']
            },
            {
                'name': 'Amazonian Warrior Training',
                'description': 'Wonder Woman\'s combat fitness routine',
                'category': 'Mixed Martial Arts',
                'difficulty': 'advanced',
                'duration': 45,
                'calories_estimate': 500,
                'points': 50,
                'equipment': ['Boxing gloves', 'Jump rope', 'Medicine ball'],
                'instructions': ['Jump rope 10 min', 'Shadow boxing 5 rounds', 'Medicine ball slams 4x15', 'Cool down']
            },
            {
                'name': 'Web-Slinger Flexibility',
                'description': 'Spider-Man inspired yoga and stretching',
                'category': 'Yoga',
                'difficulty': 'beginner',
                'duration': 30,
                'calories_estimate': 150,
                'points': 15,
                'equipment': ['Yoga mat'],
                'instructions': ['Sun salutations 5x', 'Warrior poses', 'Spinal twists', 'Savasana']
            },
            {
                'name': 'Atlantean Swim Workout',
                'description': 'Aquaman\'s ocean-ready swimming routine',
                'category': 'Swimming',
                'difficulty': 'intermediate',
                'duration': 45,
                'calories_estimate': 450,
                'points': 45,
                'equipment': ['Swimming pool', 'Goggles'],
                'instructions': ['Warm up 400m', 'Freestyle 10x100m', 'Backstroke 5x100m', 'Cool down 200m']
            },
            {
                'name': 'Gotham Rooftop Circuit',
                'description': 'Batman\'s stealth and agility training',
                'category': 'Circuit Training',
                'difficulty': 'advanced',
                'duration': 50,
                'calories_estimate': 550,
                'points': 55,
                'equipment': ['Pull-up bar', 'Box', 'Kettlebell'],
                'instructions': ['Burpees 4x20', 'Pull-ups 4x12', 'Box jumps 4x15', 'Kettlebell swings 4x20']
            },
        ]
        
        for workout_data in workouts:
            workout = Workout.objects.create(**workout_data)
            self.stdout.write(self.style.SUCCESS(f'Created workout: {workout.name}'))
        
        # Summary
        self.stdout.write(self.style.SUCCESS('\n=== Database Population Complete ==='))
        self.stdout.write(self.style.SUCCESS(f'Teams: {Team.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Users: {User.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Activities: {Activity.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Leaderboard entries: {Leaderboard.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Workouts: {Workout.objects.count()}'))
