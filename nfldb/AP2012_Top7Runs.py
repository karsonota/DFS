# -*- coding: utf-8 -*-
"""
Created on Sun May 07 16:37:32 2017

@author: Alan
nfldb w/ nflvid test
"""
import nfldb
import nflvid.vlc

db = nfldb.connect()
q = nfldb.Query(db)

q.game(season_year=2015, season_type='Regular')
q.player(full_name='Adrian Peterson').play(rushing_yds__ge=50)

nflvid.vlc.watch(db, q.as_plays(), '/m/nfl/coach/pbp')
