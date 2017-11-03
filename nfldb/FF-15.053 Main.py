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

year = 2013
position = 'TE'
limit = 60
sort_by = 'receiving_yds'

db = nfldb.connect()
q = nfldb.Query(db)
q.game(season_year = year, season_type='Regular')
q.player(position = position)

with open('output/top'+str(limit)+'_'+str(position)+'_'+str(year)+'.csv', 'wb') as csvfile:
    c = csv.writer(csvfile)
    c.writerow(['Player', 'Rec Yds', 'Rec Tar', 'Rec Tds', 'Rec YAC', 
                'Rush Yds', 'Rush Att',
                'Rush Tds', 'Pass Yds', 'Pass Tds', 'Pass Att', 'Fumbles', 'Interceptions',
                'Team Pass Yds', 'Team Pass Tds', 'Team Pass Att', 'Comp %', "Team Rush Yds",
                "Team Rush Tds", 'Team Rush Att',
                str(year+1) + ' FP'])
    for pp in q.sort(sort_by).limit(limit).as_aggregate():
        team = pp.player.team
        #next_year_FP = fantasy_points.fantasy_points(year + 1, pp.player)
        c.writerow([pp.player, pp.receiving_yds, pp.receiving_tar, pp.receiving_tds,
                    pp.receiving_yac_yds,
                    pp.rushing_yds, pp.rushing_att, pp.rushing_tds, pp.passing_yds,
                    pp.passing_tds, pp.passing_att, pp.fumbles_tot, pp.passing_int,
                    team_stats.team_passing_yds(year, team), 
                    team_stats.team_passing_tds(year, team),
                    team_stats.team_passing_att(year, team),
                    pp.receiving_rec/float(pp.receiving_tar+1),
                    team_stats.team_rushing_yds(year, team), 
                    team_stats.team_rushing_tds(year, team),
                    team_stats.team_rushing_att(year, team)])
                    #next_year_FP])
    csvfile.close()
    