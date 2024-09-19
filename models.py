from enum import unique

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates  # מאפשר ולידציה אוטומטית על שדות מסוימים בעת השמירה

db = SQLAlchemy()


class Player(db.Model):
    # __tablename__ = 'player'
    id = db.Column(db.Integer, primary_key=True)
    playerName = db.Column(db.String(80), unique=True, nullable=False)
    position = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    games = db.Column(db.Integer, nullable=False)
    gamesStarted = db.Column(db.Integer, nullable=False)
    minutesPg = db.Column(db.Integer, nullable=False)
    fieldGoals = db.Column(db.Integer, nullable=False)
    fieldAttempts = db.Column(db.Integer, nullable=False)
    fieldPercent = db.Column(db.Integer, nullable=False)
    threeFg = db.Column(db.Integer, nullable=False)
    threeAttempts = db.Column(db.Integer, nullable=False)
    threePercent = db.Column(db.Integer, nullable=False)
    twoFg = db.Column(db.Integer, nullable=False)
    twoAttempts = db.Column(db.Integer, nullable=False)
    twoPercent = db.Column(db.Integer, nullable=False)
    effectFgPercent = db.Column(db.Integer, nullable=False)
    ft = db.Column(db.Integer, nullable=False)
    ftAttempts = db.Column(db.Integer, nullable=False)
    ftPercent = db.Column(db.Integer, nullable=False)
    offensiveRb = db.Column(db.Integer, nullable=False)
    defensiveRb = db.Column(db.Integer, nullable=False)
    totalRb = db.Column(db.Integer, nullable=False)
    assists = db.Column(db.Integer, nullable=False)
    steals = db.Column(db.Integer, nullable=False)
    blocks = db.Column(db.Integer, nullable=False)
    turnovers = db.Column(db.Integer, nullable=False)
    personalFouls = db.Column(db.Integer, nullable=False)
    points = db.Column(db.Integer, nullable=False)
    team = db.Column(db.String(80), unique=True, nullable=False)
    season = db.Column(db.Integer, nullable=False)
    playerId = db.Column(db.String(80), unique=True, nullable=False)


    def __repr__(self):
        # מתודת ייצוג שתאפשר הדפסת אובייקטים של המשתמש בצורה קריאה
        return f'<Player {self.player_name}{self.team}{self.position}{self.season}\
                         {self.points}{self.games}{self.two_percent}{self.three_percent}\
                         {self.art}{self.ppg_ratio}>'


class Team(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(80), unique=True, nullable=False)
    player_c = db.Column(db.Integer, nullable=False)
    player_pf = db.Column(db.Integer, nullable=False)
    player_sf = db.Column(db.Integer, nullable=False)
    player_sg = db.Column(db.Integer, nullable=False)
    player_pg = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return (f'<User {self.team_name}\
                {self.player_c}{str(self.player_pf)}\
                {self.player_sf}{self.player_sg}{self.player_pg}>')

    @validates('player_c', 'player_pf', 'player_sf', 'player_sg', 'player_pg')
    def validate_num_of_players(self, playey_c_key, player_c,\
                                     player_pf_key, player_pf,\
                                     player_sf_key, player_sf,\
                                     player_sg_key, player_sg,\
                                     player_pg_key, player_pg):
        print(f"key is {player_c_key}, {player_pf_key}, {player_sf_key}, {player_sg_key}, {player_pg_key}")
        print(f"player id is {player_c}, {player_pf}, {player_sf}, {player_sg}, {player_pg}")
        assert type(player_c) == int, "The player_c must be confirm"
        assert type(player_pf) == int, "The player_pf must be confirm"
        assert type(player_sf) == int, "The player_sf must be confirm"
        assert type(player_sg) == int, "The player_sf must be confirm"
        assert type(player_pg) == int, "The player_pg must be confirm"
        return player_c, player_pf, player_sf, player_sg, player_pg
