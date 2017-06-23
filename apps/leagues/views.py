from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q

from . import team_maker

def index(request):

	context = {
		"q1": League.objects.filter(sport="Baseball"),
		'q2': League.objects.filter(sport__contains="hockey"),
		'q3': League.objects.filter(sport__contains="hockey"),
		'q4': League.objects.exclude(sport__contains = "football"),
		'q5': League.objects.filter(name__contains = "Conference"),
		'q6': League.objects.filter(name__contains = "Atlantic"),
		'q7': Team.objects.filter(location__contains = "Dallas"),
		'q8': Team.objects.filter(team_name__contains = "Raptors"),
		'q9': Team.objects.filter(location__contains = "City"),
		'q10': Team.objects.filter(team_name__startswith = "T"),
		'q11': Team.objects.order_by('location'),
		'q12': Team.objects.order_by('team_name').reverse(),
		'q13': Player.objects.filter(last_name = "Cooper"),
		'q14': Player.objects.filter(first_name = "Joshua"),
		'q15': Player.objects.filter(last_name = "Cooper").exclude(first_name = "Joshua"),
		'q16': Player.objects.filter(Q(first_name = "Alexander") | Q(first_name = "Wyatt")),
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
