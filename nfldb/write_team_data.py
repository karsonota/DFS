# -*- coding: utf-8 -*-
"""
Created on Sun May 07 19:18:13 2017

@author: Alan
outputs team statistics into a csv for a given year
"""

import nfldb
import csv
import team_stats as ts

teams = ['NE','NYJ','MIA','BUF','PIT','BAL','CLE','CIN','HOU','IND',
         'JAC','TEN','DEN','KC','SD','OAK',
         'DAL','WAS','NYG','PHI','MIN','GB','DET','CHI',
         'NO','TB','ATL','CAR','SF','SEA','ARI','STL'] 
years = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]

for year in years:
    with open('output/team_stats_'+str(year)+'.csv', 'wb') as csvfile:
        c = csv.writer(csvfile)
        c.writerow(['Team','Total Pass Yards','Total Pass TDs','Total Pass Att',
                    'Total Rush Yards','Total Rush TDs', 'Total Rush Att'])
        for team in teams:
            pYds = str(ts.team_passing_yds(year, team))
            pTds = str(ts.team_passing_tds(year, team))
            pAtt = str(ts.team_passing_att(year, team))
            rYds = str(ts.team_rushing_yds(year, team))
            rTds = str(ts.team_rushing_tds(year, team))
            rAtt = str(ts.team_rushing_att(year, team))
            c.writerow([team, pYds, pTds, pAtt, rYds, rTds, rAtt])
        csvfile.close()
        