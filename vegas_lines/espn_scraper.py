# -*- coding: utf-8 -*-
"""
Created on Sat Nov 04 12:13:48 2017

@author: Alan
Scrape espn.com/nfl/lines for weekly over unders and spread
"""
from bs4 import BeautifulSoup
import urllib2
import csv

year = '2017'

#Team matching dictionary -- TO IMPLEMENT LATER --
teams = {'Buffalo':'BUF', 'NY Jets':'NYJ', 'Atlanta':'ATL', 'Carolina':'CAR',
         'Indianapolis':'IND', 'Houston':'HOU','Cincinatti':'CIN',
         'Jacksonville':'JAC', 'Tampa Bay':'TB','New Orleans':'NO',
         'LA Rams':'LAR','NY Giants':'NYG', 'Denver':'DEN',
         'Philadelphia':'PHL', 'Baltimore':'BAL','Tennessee':'TEN',
         'Arizona':'ARI','San Francisco':'SF','Washington':'WAS',
         'Seattle':'SEA','Kansas City':'KC','Dallas':'DAL',
         'Oakland':'OAK','Miami':'MIA','Detroit':'DET','Green Bay':'GB'}

#Spreadsheet Headers
headers = ['Home Team', 'Away Team', 'Home Spread', 'O/U', 'Day', 'Date', 'Time']

#URL
nfl_lines_page = 'http://www.espn.com/nfl/lines'

# return html to the page
page = urllib2.urlopen(nfl_lines_page)

#parse using BeautifulSoup and store
soup = BeautifulSoup(page, 'html.parser')

#find week
header_line = soup.find(class_="h2")
start_week = header_line.text.find('Week')
week = header_line.text[start_week:36].encode('utf-8')

#pull out useful rows
table = soup.find(id="my-teams-table")
rows = soup.find_all(class_=["stathead","oddrow","evenrow"])

#configure csv file
csvfile = open('output/'+str(week)+'lines.csv', 'wb')
c = csv.writer(csvfile)
c.writerow(headers)

#loop over rows and write to csv
for i, row in enumerate(rows):
    if row['class'] == [u'stathead']:
        cur_stathead = i
        ou = []
        spread = []
        e_row = row.text.encode('utf-8')
        hyphen_ind = e_row.find('-')
        teams = e_row[:hyphen_ind].split(' at ') # home team is index 0 and away team is index 1
        pm_ind = e_row.find('PM')
        time_date = e_row[hyphen_ind+1:pm_ind].split(',') #[0]=day, [1]=date, [2]=time
    else:
        if (i-cur_stathead) == 7:
            avg_ou = sum(ou)/len(ou)
            avg_spread = sum(spread)/len(spread)
            c.writerow([teams[0],teams[1],avg_spread,avg_ou,time_date[0],
                        time_date[1],time_date[2]])
            continue
        table_values = row.find_all('td')
        if not table_values:
            break
        ou_ind = table_values[5].text.find('O/U')
        ou.append(float(table_values[5].text[:ou_ind].encode('utf-8')))
        sign = table_values[2].text[0]
        if sign == '-':
            spread.append(float(table_values[2].text.split('+')[0]))
        else:
            spread.append(float(table_values[2].text.split('-')[0]))
        
            
csvfile.close()
            
        
        
        
        
        