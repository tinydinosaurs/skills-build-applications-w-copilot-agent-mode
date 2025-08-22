# Users, Teams, Activities, Leaderboard, Workouts models
from djongo import models

class Team(models.Model):
	id = models.ObjectIdField(primary_key=True, default=None, editable=False)
	name = models.CharField(max_length=100, unique=True)
	description = models.TextField(blank=True)
	def __str__(self):
		return self.name

class User(models.Model):
	id = models.ObjectIdField(primary_key=True, default=None, editable=False)
	name = models.CharField(max_length=100)
	email = models.EmailField(unique=True)
	team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
	def __str__(self):
		return self.name

class Activity(models.Model):
	id = models.ObjectIdField(primary_key=True, default=None, editable=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
	type = models.CharField(max_length=50)
	duration = models.IntegerField()  # minutes
	calories = models.IntegerField()
	date = models.DateField()
	def __str__(self):
		return f"{self.type} - {self.user.name}"

class Workout(models.Model):
	id = models.ObjectIdField(primary_key=True, default=None, editable=False)
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	suggested_for = models.ManyToManyField(Team, related_name='workouts')
	def __str__(self):
		return self.name

class Leaderboard(models.Model):
	id = models.ObjectIdField(primary_key=True, default=None, editable=False)
	team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboard')
	points = models.IntegerField(default=0)
	rank = models.IntegerField(default=0)
	def __str__(self):
		return f"{self.team.name} - {self.points} pts"
