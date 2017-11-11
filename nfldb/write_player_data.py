# -*- coding: utf-8 -*-
"""
Spyder Editor
Created on Wed Apr 06 13:02:04 2016
@author: Mwymer1
edited by Alan
"""

import nfldb
import csv
import team_stats
#import fantasy_points

years = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
positions = {'TE': {'limit':24, 'sort_by':'receiving_yds'},
             'WR': {'limit':60, 'sort_by':'receiving_yds'},
             'RB': {'limit':60, 'sort_by':'rushing_yds'},
             'QB': {'limit':24, 'sort_by':'passing_yds'}}

for position, value in positions.items():
    limit = value['limit']
    sort_by = value['sort_by']
    for year in years:
        db = nfldb.connect()
        q = nfldb.Query(db)
        q.game(season_year = year, season_type='Regular')
        q.player(position = position)
        
        with open('output/player/'+str(position)+'/'+str(year)+'_top'+str(limit)+'.csv', 'wb') as csvfile:
            c = csv.writer(csvfile)
            c.writerow(['Player', 'Rec Yds', 'Rec Tar', 'Rec Tds', 'Rec YAC', 'Rec %',
                        'Rush Yds', 'Rush Att',
                        'Rush Tds', 'Pass Yds', 'Pass Tds', 'Pass Att', 'Fumbles', 'Interceptions',
                        'Team Passing Yds', 'Team Passing Tds', 'Team Passing Att',
                        'Team Rushing Yds', 'Team Rushing Tds', 'Team Rushing Att'])
            for pp in q.sort(sort_by).limit(limit).as_aggregate():
                team = pp.player.team
                #next_year_FP = fantasy_points.fantasy_points(year + 1, pp.player)
                c.writerow([pp.player, pp.receiving_yds, pp.receiving_tar, pp.receiving_tds,
                            pp.receiving_yac_yds, pp.receiving_rec/float(pp.receiving_tar+1),
                            pp.rushing_yds, pp.rushing_att, pp.rushing_tds, pp.passing_yds,
                            pp.passing_tds, pp.passing_att, pp.fumbles_tot, pp.passing_int,
                            team_stats.team_passing_yds(year, team), 
                            team_stats.team_passing_tds(year, team),
                            team_stats.team_passing_att(year, team),
                            team_stats.team_rushing_yds(year, team), 
                            team_stats.team_rushing_tds(year, team),
                            team_stats.team_rushing_att(year, team)])
                            #next_year_FP])
            csvfile.close()
    