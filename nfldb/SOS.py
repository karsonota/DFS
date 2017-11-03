# -*- coding: utf-8 -*-
"""
Created on Wed Apr 06 19:11:37 2016

@author: Mwymer1
Edited by Alan
"""

import nfldb

'''teams = ['NE','NYJ','MIA','BUF','PIT','BAL','CLE','CIN','HOU','IND',
         'JAC','TEN','DEN','KC','SD','OAK',
         'DAL','WAS','NYG','PHI','MIN','GB','DET','CHI',
         'NO','TB','ATL','CAR','SF','SEA','ARI','STL'] '''
         
teams = ['NE']

for team in teams:
    db = nfldb.connect()
    q = nfldb.Query(db)
    q.game(season_year = 2015, season_type='Regular', team = team)
    #q.play(passing_cmp = 1)
    
    points_against = 0
    touchdowns_against = 0
    yards_against = 0
    for game in q.as_games():
        if game.away_team == team:
            other_team = game.home_team
        else:
            other_team = game.away_team
        q = nfldb.Query(db).drive(gsis_id = game.gsis_id)
        for p in q.drive(pos_team = other_team).play(passing_cmp = 1, passing_int = 0).as_plays():
            points_against = points_against + p.passing_yds*0.1 + p.passing_tds*6
            yards_against += p.passing_yds
        for td in q.drive(pos_team = other_team).play(passing_cmp = 1,passing_tds = 1).as_plays():
                touchdowns_against += 1
        #print points_against
    print yards_against
           
            
            
        

