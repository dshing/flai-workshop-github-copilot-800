from djongo import models


class User(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    team = models.CharField(max_length=100, null=True, blank=True)
    total_points = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name


class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    total_points = models.IntegerField(default=0)
    member_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name


class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    user_id = models.CharField(max_length=24)
    user_name = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    distance = models.FloatField(null=True, blank=True)  # in km
    calories = models.IntegerField()
    points = models.IntegerField(default=0)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'activities'
        ordering = ['-date']

    def __str__(self):
        return f"{self.user_name} - {self.activity_type}"


class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    user_id = models.CharField(max_length=24)
    user_name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    total_points = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    activities_count = models.IntegerField(default=0)
    last_activity = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'leaderboard'
        ordering = ['-total_points']

    def __str__(self):
        return f"{self.rank}. {self.user_name} - {self.total_points} points"


class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=20)  # beginner, intermediate, advanced
    duration = models.IntegerField()  # in minutes
    calories_estimate = models.IntegerField()
    points = models.IntegerField(default=0)
    equipment = models.JSONField(default=list)
    instructions = models.JSONField(default=list)

    class Meta:
        db_table = 'workouts'

    def __str__(self):
        return self.name
