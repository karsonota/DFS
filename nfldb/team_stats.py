# -*- coding: utf-8 -*-
"""
Created on Wed Apr 06 13:40:38 2016

@author: Mwymer1
Edited AW
"""

import nfldb

def team_passing_att(season_year, team):
    db = nfldb.connect()
    q = nfldb.Query(db)
    q.game(season_year= season_year, season_type='Regular', team= team)
    q.play(passing_att=1)
    count = len(q.drive(pos_team= team).as_plays())
    return count
    
def team_passing_yds(season_year, team):
    db = nfldb.connect()
    q = nfldb.Query(db)
    q.game(season_year= season_year, season_type='Regular', team= team)
    q.play(passing_att=1)
    count = 0
    
    for pass_att in q.drive(pos_team= team).as_plays():
        count+= pass_att.passing_yds
        
    return count

def team_passing_tds(season_year, team):
    db = nfldb.connect()
    q = nfldb.Query(db)
    q.game(season_year= season_year, season_type='Regular', team= team)
    q.play(passing_tds=1)
    count = len(q.drive(pos_team= team).as_plays())
    return count
    
def team_rushing_att(season_year, team):
    db = nfldb.connect()
    q = nfldb.Query(db)
    q.game(season_year= season_year, season_type='Regular', team= team)
    q.play(rushing_att=1)
    count = len(q.drive(pos_team= team).as_plays())
    return count
    
def team_rushing_yds(season_year, team):
    db = nfldb.connect()
    q = nfldb.Query(db)
    q.game(season_year= season_year, season_type='Regular', team= team)
    q.play(rushing_att=1)
    count = 0
    
    for rush_att in q.drive(pos_team= team).as_plays():
        count+= rush_att.rushing_yds
        
    return count

def team_rushing_tds(season_year, team):
    db = nfldb.connect()
    q = nfldb.Query(db)
    q.game(season_year= season_year, season_type='Regular', team= team)
    q.play(rushing_tds=1)
    count = len(q.drive(pos_team= team).as_plays())

    return count

def get_all_team_gsis_ids(season_year, team):
    db = nfldb.connect()
    q = nfldb.Query(db)
    q.game(season_year= season_year, season_type='Regular', team= team)
    gsis_ids = []
    for game in q.as_games():
        gsis_ids.append(game.gsis_id)
        
    return gsis_ids

def team_rushing_yds_all(season_year, team):
    db = nfldb.connect()
    game_ids = get_all_team_gsis_ids(season_year, team)
    count = 0
    for game_id in game_ids:
        q = nfldb.Query(db)
        q.game(gsis_id=game_id)
        game = q.as_games()
        if game[0].away_team == team:
            opp_team = game[0].home_team
        else:
            opp_team = game[0].away_team
        q.play(rushing_att=1)
        for play in q.drive(pos_team=opp_team).as_plays():
            count+= play.rushing_yds
            
    return count

def team_rushing_tds_all(season_year, team):
    db = nfldb.connect()
    game_ids = get_all_team_gsis_ids(season_year, team)
    count = 0
    for game_id in game_ids:
        q = nfldb.Query(db)
        q.game(gsis_id=game_id)
        game = q.as_games()
        if game[0].away_team == team:
            opp_team = game[0].home_team
        else:
            opp_team = game[0].away_team
        q.play(rushing_tds=1)
        plays = q.drive(pos_team=opp_team).as_plays()
        count+= len(plays)
            
    return count
            
def team_passing_yds_all(season_year, team):
    db = nfldb.connect()
    game_ids = get_all_team_gsis_ids(season_year, team)
    count = 0
    for game_id in game_ids:
        q = nfldb.Query(db)
        q.game(gsis_id=game_id)
        game = q.as_games()
        if game[0].away_team == team:
            opp_team = game[0].home_team
        else:
            opp_team = game[0].away_team
        q.play(passing_att=1)
        for play in q.drive(pos_team=opp_team).as_plays():
            count+= play.passing_yds
            
    return count

def team_passing_tds_all(season_year, team):
    db = nfldb.connect()
    game_ids = get_all_team_gsis_ids(season_year, team)
    count = 0
    for game_id in game_ids:
        q = nfldb.Query(db)
        q.game(gsis_id=game_id)
        game = q.as_games()
        if game[0].away_team == team:
            opp_team = game[0].home_team
        else:
            opp_team = game[0].away_team
        q.play(passing_tds=1)
        plays = q.drive(pos_team=opp_team).as_plays()
        count+= len(plays)
            
    return count