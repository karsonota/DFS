# -*- coding: utf-8 -*-
"""
Created on Wed Apr 06 13:40:38 2016

@author: Mwymer1

"""

import nfldb

def team_passing_att(season_year, team):

    db = nfldb.connect()
    q = nfldb.Query(db)
    q.game(season_year= season_year, season_type='Regular', team= team)
    q.play(passing_att=1)
    count = 0
    
    for pass_att in q.drive(pos_team= team).as_plays():
        count+=1
        
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
    count = 0
    
    for td in q.drive(pos_team= team).as_plays():
        count+= 1

    return count
    
def team_rushing_att(season_year, team):

    db = nfldb.connect()
    q = nfldb.Query(db)
    q.game(season_year= season_year, season_type='Regular', team= team)
    q.play(rushing_att=1)
    count = 0
    
    for rush_att in q.drive(pos_team= team).as_plays():
        count+=1
        
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
    count = 0
    
    for td in q.drive(pos_team= team).as_plays():
        count+= 1

    return count

