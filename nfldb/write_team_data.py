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
years = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]

for year in years:
    if year == 2016:
        teams = ['LA' if x=='STL' else x for x in teams]
    elif year == 2017:
        teams = ['LAC' if x=='SD' else x for x in teams]
    with open('output/team/team_off_stats_'+str(year)+'.csv', 'wb') as csvfile:
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
        
for year in years:
    if year == 2016:
        teams = ['LA' if x=='STL' else x for x in teams]
    elif year == 2017:
        teams = ['LAC' if x=='SD' else x for x in teams]
    with open('output/team/team_def_stats_'+str(year)+'.csv', 'wb') as csvfile:
        c = csv.writer(csvfile)
        c.writerow(['Team', 'Total Pass Yards Allowed', 'Total Pass TDs Allowed',
                    'Total Rush Yards Allowed', 'Total Rush TDs Allowed'])
        for team in teams:
            pYdsA = str(ts.team_passing_yds_all(year, team))
            pTdsA = str(ts.team_passing_tds_all(year, team))
            rYdsA = str(ts.team_rushing_yds_all(year, team))
            rTdsA = str(ts.team_rushing_tds_all(year, team))
            c.writerow([team, pYdsA, pTdsA, rYdsA, rTdsA])
        csvfile.close()