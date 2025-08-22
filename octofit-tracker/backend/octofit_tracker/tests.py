from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
	def setUp(self):
		self.team = Team.objects.create(name="Marvel", description="Marvel Superheroes")
		self.user = User.objects.create(name="Spider-Man", email="spiderman@marvel.com", team=self.team)
		self.workout = Workout.objects.create(name="Cardio", description="Cardio workout")
		self.workout.suggested_for.add(self.team)
		self.activity = Activity.objects.create(user=self.user, type="Running", duration=30, calories=300, date="2025-08-22")
		self.leaderboard = Leaderboard.objects.create(team=self.team, points=100, rank=1)

	def test_user_creation(self):
		self.assertEqual(self.user.name, "Spider-Man")
		self.assertEqual(self.user.team.name, "Marvel")

	def test_team_creation(self):
		self.assertEqual(self.team.name, "Marvel")

	def test_activity_creation(self):
		self.assertEqual(self.activity.type, "Running")

	def test_workout_creation(self):
		self.assertEqual(self.workout.name, "Cardio")

	def test_leaderboard_creation(self):
		self.assertEqual(self.leaderboard.points, 100)
