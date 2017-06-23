from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q, Count

from . import team_maker

def index(request):
	context = {
		"q1": Team.objects.filter(league__name="Atlantic Soccer Conference"),
		'q2': Player.objects.filter(curr_team__location="Boston", curr_team__team_name="Penguins"),
		'q3': Player.objects.filter(curr_team__league__name="International Collegiate Baseball Conference"),
		'q4': Player.objects.filter(curr_team__league__name="American Conference of Amateur Football").filter(last_name="Lopez"),
		'q5': Player.objects.filter(curr_team__league__sport__contains="football"),
		'q6': Team.objects.filter(curr_players__first_name="Sophia"),
		'q7': League.objects.filter(teams__curr_players__first_name="Sophia"),
		'q8': Player.objects.filter(last_name="Flores").exclude(curr_team__team_name="Roughriders"),
		'q9': Team.objects.filter(all_players__first_name="Samuel", all_players__last_name="Evans"),
		'q10': Player.objects.filter(all_teams__location="Manitoba", all_teams__team_name="Tiger-Cats"),
		'q11': Player.objects.filter(all_teams__location="Wichita", all_teams__team_name="Vikings").exclude(curr_team__location="Wichita", curr_team__team_name="Vikings"),
		'q12': Team.objects.filter(all_players__first_name="Jacob", all_players__last_name="Gray").exclude(location="Oregon", team_name="Colts"),
		'q13': Player.objects.filter(all_teams__league__name="Atlantic Federation of Amateur Baseball Players", first_name="Joshua"),
		'q14': Team.objects.annotate(num_players=Count('all_players')).filter(num_players__gte=12),
		'q15': Player.objects.annotate(num_teams=Count('all_teams')).order_by('num_teams'),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
