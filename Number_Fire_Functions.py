# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 18:02:41 2017

@author: Alan
Read in NumberFires full player table and split into multiple sheets as desired
"""

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

col_head = ['Player', 'FP', 'Cost', 'Value', 'C/A', 'PYDS', 'PTDS','INTS','RUATT','RUYDS','RUTDS','REREC','REYDS','RETDS','RETGTS']
dk_df = pd.read_excel('C:\\Users\\Alan\\Documents\\Fantasy\\Football\\DFS\\10292017\\FD_ALL_POS_PROJ.xlsx', sheetname='Sheet1', names=col_head)

dk_write_df = []
player = []
position = []
matchup = []
time = []
for i in dk_df.index:
    if 'GTD' in dk_df['Player'][i]:
        dk_df['Player'][i] = dk_df['Player'][i].replace('GTD','')
        curr_array = dk_df['Player'][i].split()
        player.append(curr_array[0]+' '+curr_array[1])
        position.append(curr_array[2])
        matchup.append(curr_array[3]+' @ '+curr_array[5])
        time.append(curr_array[6]+' '+curr_array[7])
        continue
    curr_array = dk_df['Player'][i].split()
    player.append(curr_array[0]+' '+curr_array[1])
    position.append(curr_array[2])
    matchup.append(curr_array[3]+' @ '+curr_array[5][:-3])
    time.append(curr_array[5][-3:]+' '+curr_array[6])
    
del dk_df['Player']
columns = [player, position, matchup, time]
new_head = ['Player', 'Position', 'Matchup', 'Game Time']
for idx, val in enumerate(new_head):
    dk_df.insert(loc=idx, column=val, value=columns[idx])
    
dk_df_qb = dk_df[dk_df['Position'] == 'QB']
dk_df_wr = dk_df[dk_df['Position'] == 'WR']
dk_df_rb = dk_df[dk_df['Position'] == 'RB']
dk_df_te = dk_df[dk_df['Position'] == 'TE']
dk_df_def = dk_df[dk_df['Position'] == 'D/ST']
writer = ExcelWriter('C:\\Users\\Alan\\Documents\\Fantasy\\Football\\DFS\\10292017\\FD_ALL_POS_PROJ_PROCESSED.xlsx')
dk_df.to_excel(writer,'DK Projections',index=False)
dk_df_qb.to_excel(writer,'DK QB',index=False)
dk_df_wr.to_excel(writer,'DK WR',index=False)
dk_df_rb.to_excel(writer,'DK RB',index=False)
dk_df_te.to_excel(writer,'DK TE',index=False)
dk_df_def.to_excel(writer,'DK DEF',index=False)
writer.save()