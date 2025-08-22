from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
	help = 'Populate the octofit_db database with test data'

	def handle(self, *args, **options):
		# Clear existing data in correct order
		for activity in Activity.objects.all():
			if activity.pk:
				activity.delete()
		for leaderboard in Leaderboard.objects.all():
			if leaderboard.pk:
				leaderboard.delete()
		# Delete users one by one to avoid unhashable error
		for user in User.objects.all():
			if user.pk:
				user.delete()
		# Clear ManyToMany relationships for workouts
		for workout in Workout.objects.all():
			workout.suggested_for.clear()
		for workout in Workout.objects.all():
			if workout.pk:
				workout.delete()
		for team in Team.objects.all():
			if team.pk:
				team.delete()

		# Create Teams
		marvel = Team.objects.create(name="Marvel", description="Marvel Superheroes")
		dc = Team.objects.create(name="DC", description="DC Superheroes")

		# Create Users
		users = [
			User(name="Spider-Man", email="spiderman@marvel.com", team=marvel),
			User(name="Iron Man", email="ironman@marvel.com", team=marvel),
			User(name="Wonder Woman", email="wonderwoman@dc.com", team=dc),
			User(name="Batman", email="batman@dc.com", team=dc),
		]
		for user in users:
			user.save()

		# Create Activities
		Activity.objects.create(user=users[0], type="Running", duration=30, calories=300, date=date.today())
		Activity.objects.create(user=users[1], type="Cycling", duration=45, calories=400, date=date.today())
		Activity.objects.create(user=users[2], type="Swimming", duration=60, calories=500, date=date.today())
		Activity.objects.create(user=users[3], type="Yoga", duration=50, calories=200, date=date.today())

		# Create Workouts
		workout1 = Workout.objects.create(name="Cardio Blast", description="High intensity cardio workout")
		workout2 = Workout.objects.create(name="Strength Training", description="Build muscle strength")
		workout1.suggested_for.add(marvel, dc)
		workout2.suggested_for.add(marvel, dc)

		# Create Leaderboard
		Leaderboard.objects.create(team=marvel, points=700, rank=1)
		Leaderboard.objects.create(team=dc, points=600, rank=2)

		self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
