from urllib import request
from models import Team
from flask import jsonify, request
import requests
from flask import Flask
app = Flask(__name__)

@app.route('/api/players/<string:position>', defaults={"season": None}, methods=['GET'])
def get_data():

    data = request.get_json()
    player_name = data.get("playerName")

    # verible for me
    art = 0
    ppg_ratio = 0
    average_for_the_season = 0
    points_per_games = 0
    team = data.get("team")
    position = data.get("position")
    if app.route.defaults != None:
        season_query = app.route.defaults.query
        if data.get("season") == season_query:
            season = data.get("season")
    else:
        season = data.get("season")
    points = data.get("points")
    games = data.get("games")
    two_percent = data.get("twoPercent")
    three_percent = data.get("threePercent")

    if data.get("playerName") == player_name:
        art = data.get("assists") / data.get("turnovers")

    if data.get("PlayerName") == player_name:
        points_per_games = data.get("Points") + data.get("Points")

    # find the average_for_the_season
    # count the points for this position
    count_points = 0
    # count the times of this position exist
    count_times = 0
    if data.get("position") == position:
        count_points += data.get("points")
        count_times += 1
    average_for_the_season = count_points / count_times

    if data.get("playerName") == player_name:
        ppg_ratio = points_per_games / average_for_the_season
    the_all_players = jsonify({"player_name": player_name, "team": team, "position": position, "season": season,
                    "points": points, "games": games, "two_percent": two_percent, "three_percent": three_percent,
                    "art": art, "ppg_ratio": ppg_ratio})
    return the_all_players

def __repr__(self):
    return requests.get(
        'https://documenter.getpostman.com/view/24232555/2s93shzpR3#358b5496-a459-4e05-9f9d-e924633454fb').content


@app.route('/api/teams/<string:name_team>,'
                           '<int:player_c>,'
                           '<int:player_pf>'
                           '<int:player_sf>,'
                           '<int:player_sg>'
                           '<int:player_pg>'
                            ,methods=['POST'],)
def create_team():
    data = request.get_json()
    name_team = Team.query["name_team"]
    player_c = Team.query["player_c"]
    player_pf = Team.query["player_pf"]
    player_sf = Team.query["player_sf"]
    player_sg = Team.query["player_sg"]
    player_pg = Team.query["player_pg"]
    team = Team.query




























