import math
import random
import csv
import re

#load players
players = []
with open('players.csv', newline='') as csvfile:
     reader = csv.reader(csvfile, delimiter=',')
     for row in reader:
         players.append(row)

#special rounding where X.YZ has a YZ% chance of being X+1 and a 1-YZ% chance of being X
def weightedround(x):
    adjust_floor = math.floor(x)
    adjust_ceiling = adjust_floor + 1
    roll = random.uniform(adjust_floor,adjust_ceiling)
    if roll < x:
        result = adjust_ceiling
    else:
        result = adjust_floor
    return result

#get rosters and other gameplan options
away_att = [1,2]
away_mid = [3,4,5]
away_def = [6,7,8]
away_keep = [9]
away_keepdepth = [3,3,3,2,2,1]
away_pk = 0
home_att = [10,11,12]
home_mid = [13,14]
home_def = [15,16,17]
home_keep = [18]
home_pk = 2
home_keepdepth = [3,2,2,2,1,1]

away_roster = []
away_stats = []
home_roster = []
home_stats = []

away_score = 0
home_score = 0

for i in away_att:
    index = int(players[i][0])
    position = players[i][1]
    name = players[i][2]
    traits = players[i][8]
    POS = round(int(players[i][12])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][13])-int(players[i][12])),2)
    REA = round(int(players[i][14])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][15])-int(players[i][14])),2)
    HAN = round(int(players[i][16])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][17])-int(players[i][16])),2)
    MAR = round(int(players[i][18])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][19])-int(players[i][18])),2)
    TAC = round(int(players[i][20])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][21])-int(players[i][20])),2)
    PAS = round(int(players[i][22])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][23])-int(players[i][22])),2)
    DRI = round(int(players[i][24])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][25])-int(players[i][24])),2)
    OFF = round(int(players[i][26])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][27])-int(players[i][26])),2)
    VIS = round(int(players[i][28])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][29])-int(players[i][28])),2)
    FIN = round(int(players[i][30])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][31])-int(players[i][30])),2)
    ACC = round(int(players[i][32])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][33])-int(players[i][32])),2)
    AGG = int(players[i][34])
    away_roster.append([index,position,name,traits,POS,REA,HAN,MAR,TAC,PAS,DRI,OFF,VIS,FIN,ACC,AGG])
                        ##0     1       2      3    4   5   6   7   8   9   10  11  12  13  14  15
    away_stats.append([index,position,name,0,0,0,0,0,0,0,0,0,0])
                       ##0     1       2   3 goal attempt, 4 goal on target, 5 goal made, 6 pass attempt, 7 pass made, 8 tackle attempt, 9 tackle made, 10 interceptions, 11 shots against, 12 shots allowed 
for i in away_mid:
    index = int(players[i][0])
    position = players[i][1]
    name = players[i][2]
    traits = players[i][8]
    POS = round(int(players[i][12])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][13])-int(players[i][12])),2)
    REA = round(int(players[i][14])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][15])-int(players[i][14])),2)
    HAN = round(int(players[i][16])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][17])-int(players[i][16])),2)
    MAR = round(int(players[i][18])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][19])-int(players[i][18])),2)
    TAC = round(int(players[i][20])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][21])-int(players[i][20])),2)
    PAS = round(int(players[i][22])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][23])-int(players[i][22])),2)
    DRI = round(int(players[i][24])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][25])-int(players[i][24])),2)
    OFF = round(int(players[i][26])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][27])-int(players[i][26])),2)
    VIS = round(int(players[i][28])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][29])-int(players[i][28])),2)
    FIN = round(int(players[i][30])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][31])-int(players[i][30])),2)
    ACC = round(int(players[i][32])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][33])-int(players[i][32])),2)
    AGG = int(players[i][34])
    away_roster.append([index,position,name,traits,POS,REA,HAN,MAR,TAC,PAS,DRI,OFF,VIS,FIN,ACC,AGG])
    away_stats.append([index,position,name,0,0,0,0,0,0,0,0,0,0])
                       ##0     1       2   3 goal attempt, 4 goal on target, 5 goal made, 6 pass attempt, 7 pass made, 8 tackle attempt, 9 tackle made, 10 interceptions, 11 shots against, 12 shots allowed 
for i in away_def:
    index = int(players[i][0])
    position = players[i][1]
    name = players[i][2]
    traits = players[i][8]
    POS = round(int(players[i][12])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][13])-int(players[i][12])),2)
    REA = round(int(players[i][14])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][15])-int(players[i][14])),2)
    HAN = round(int(players[i][16])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][17])-int(players[i][16])),2)
    MAR = round(int(players[i][18])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][19])-int(players[i][18])),2)
    TAC = round(int(players[i][20])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][21])-int(players[i][20])),2)
    PAS = round(int(players[i][22])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][23])-int(players[i][22])),2)
    DRI = round(int(players[i][24])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][25])-int(players[i][24])),2)
    OFF = round(int(players[i][26])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][27])-int(players[i][26])),2)
    VIS = round(int(players[i][28])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][29])-int(players[i][28])),2)
    FIN = round(int(players[i][30])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][31])-int(players[i][30])),2)
    ACC = round(int(players[i][32])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][33])-int(players[i][32])),2)
    AGG = int(players[i][34])
    away_roster.append([index,position,name,traits,POS,REA,HAN,MAR,TAC,PAS,DRI,OFF,VIS,FIN,ACC,AGG])
    away_stats.append([index,position,name,0,0,0,0,0,0,0,0,0,0])
                       ##0     1       2   3 goal attempt, 4 goal on target, 5 goal made, 6 pass attempt, 7 pass made, 8 tackle attempt, 9 tackle made, 10 interceptions, 11 shots against, 12 shots allowed 
for i in away_keep:
    index = int(players[i][0])
    position = players[i][1]
    name = players[i][2]
    traits = players[i][8]
    POS = round(int(players[i][12])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][13])-int(players[i][12])),2)
    REA = round(int(players[i][14])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][15])-int(players[i][14])),2)
    HAN = round(int(players[i][16])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][17])-int(players[i][16])),2)
    MAR = round(int(players[i][18])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][19])-int(players[i][18])),2)
    TAC = round(int(players[i][20])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][21])-int(players[i][20])),2)
    PAS = round(int(players[i][22])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][23])-int(players[i][22])),2)
    DRI = round(int(players[i][24])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][25])-int(players[i][24])),2)
    OFF = round(int(players[i][26])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][27])-int(players[i][26])),2)
    VIS = round(int(players[i][28])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][29])-int(players[i][28])),2)
    FIN = round(int(players[i][30])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][31])-int(players[i][30])),2)
    ACC = round(int(players[i][32])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][33])-int(players[i][32])),2)
    AGG = int(players[i][34])
    away_roster.append([index,position,name,traits,POS,REA,HAN,MAR,TAC,PAS,DRI,OFF,VIS,FIN,ACC,AGG])
    away_stats.append([index,position,name,0,0,0,0,0,0,0,0,0,0])
                       ##0     1       2   3 goal attempt, 4 goal on target, 5 goal made, 6 pass attempt, 7 pass made, 8 tackle attempt, 9 tackle made, 10 interceptions, 11 shots against, 12 shots allowed 
for i in home_att:
    index = int(players[i][0])
    position = players[i][1]
    name = players[i][2]
    traits = players[i][8]
    POS = round(int(players[i][12])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][13])-int(players[i][12])),2)
    REA = round(int(players[i][14])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][15])-int(players[i][14])),2)
    HAN = round(int(players[i][16])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][17])-int(players[i][16])),2)
    MAR = round(int(players[i][18])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][19])-int(players[i][18])),2)
    TAC = round(int(players[i][20])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][21])-int(players[i][20])),2)
    PAS = round(int(players[i][22])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][23])-int(players[i][22])),2)
    DRI = round(int(players[i][24])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][25])-int(players[i][24])),2)
    OFF = round(int(players[i][26])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][27])-int(players[i][26])),2)
    VIS = round(int(players[i][28])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][29])-int(players[i][28])),2)
    FIN = round(int(players[i][30])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][31])-int(players[i][30])),2)
    ACC = round(int(players[i][32])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][33])-int(players[i][32])),2)
    AGG = int(players[i][34])
    home_roster.append([index,position,name,traits,POS,REA,HAN,MAR,TAC,PAS,DRI,OFF,VIS,FIN,ACC,AGG])
    home_stats.append([index,position,name,0,0,0,0,0,0,0,0,0,0])
                       ##0     1       2   3 goal attempt, 4 goal on target, 5 goal made, 6 pass attempt, 7 pass made, 8 tackle attempt, 9 tackle made, 10 interceptions, 11 shots against, 12 shots allowed 
for i in home_mid:
    index = int(players[i][0])
    position = players[i][1]
    name = players[i][2]
    traits = players[i][8]
    POS = round(int(players[i][12])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][13])-int(players[i][12])),2)
    REA = round(int(players[i][14])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][15])-int(players[i][14])),2)
    HAN = round(int(players[i][16])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][17])-int(players[i][16])),2)
    MAR = round(int(players[i][18])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][19])-int(players[i][18])),2)
    TAC = round(int(players[i][20])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][21])-int(players[i][20])),2)
    PAS = round(int(players[i][22])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][23])-int(players[i][22])),2)
    DRI = round(int(players[i][24])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][25])-int(players[i][24])),2)
    OFF = round(int(players[i][26])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][27])-int(players[i][26])),2)
    VIS = round(int(players[i][28])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][29])-int(players[i][28])),2)
    FIN = round(int(players[i][30])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][31])-int(players[i][30])),2)
    ACC = round(int(players[i][32])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][33])-int(players[i][32])),2)
    AGG = int(players[i][34])
    home_roster.append([index,position,name,traits,POS,REA,HAN,MAR,TAC,PAS,DRI,OFF,VIS,FIN,ACC,AGG])
    home_stats.append([index,position,name,0,0,0,0,0,0,0,0,0,0])
                       ##0     1       2   3 goal attempt, 4 goal on target, 5 goal made, 6 pass attempt, 7 pass made, 8 tackle attempt, 9 tackle made, 10 interceptions, 11 shots against, 12 shots allowed 
for i in home_def:
    index = int(players[i][0])
    position = players[i][1]
    name = players[i][2]
    traits = players[i][8]
    POS = round(int(players[i][12])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][13])-int(players[i][12])),2)
    REA = round(int(players[i][14])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][15])-int(players[i][14])),2)
    HAN = round(int(players[i][16])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][17])-int(players[i][16])),2)
    MAR = round(int(players[i][18])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][19])-int(players[i][18])),2)
    TAC = round(int(players[i][20])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][21])-int(players[i][20])),2)
    PAS = round(int(players[i][22])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][23])-int(players[i][22])),2)
    DRI = round(int(players[i][24])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][25])-int(players[i][24])),2)
    OFF = round(int(players[i][26])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][27])-int(players[i][26])),2)
    VIS = round(int(players[i][28])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][29])-int(players[i][28])),2)
    FIN = round(int(players[i][30])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][31])-int(players[i][30])),2)
    ACC = round(int(players[i][32])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][33])-int(players[i][32])),2)
    AGG = int(players[i][34])
    home_roster.append([index,position,name,traits,POS,REA,HAN,MAR,TAC,PAS,DRI,OFF,VIS,FIN,ACC,AGG])
    home_stats.append([index,position,name,0,0,0,0,0,0,0,0,0,0])
                       ##0     1       2   3 goal attempt, 4 goal on target, 5 goal made, 6 pass attempt, 7 pass made, 8 tackle attempt, 9 tackle made, 10 interceptions, 11 shots against, 12 shots allowed 
for i in home_keep:
    index = int(players[i][0])
    position = players[i][1]
    name = players[i][2]
    traits = players[i][8]
    POS = round(int(players[i][12])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][13])-int(players[i][12])),2)
    REA = round(int(players[i][14])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][15])-int(players[i][14])),2)
    HAN = round(int(players[i][16])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][17])-int(players[i][16])),2)
    MAR = round(int(players[i][18])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][19])-int(players[i][18])),2)
    TAC = round(int(players[i][20])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][21])-int(players[i][20])),2)
    PAS = round(int(players[i][22])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][23])-int(players[i][22])),2)
    DRI = round(int(players[i][24])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][25])-int(players[i][24])),2)
    OFF = round(int(players[i][26])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][27])-int(players[i][26])),2)
    VIS = round(int(players[i][28])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][29])-int(players[i][28])),2)
    FIN = round(int(players[i][30])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][31])-int(players[i][30])),2)
    ACC = round(int(players[i][32])+random.gauss(0,0.25)+random.gauss(0.15,0.05)*(int(players[i][33])-int(players[i][32])),2)
    AGG = int(players[i][34])
    home_roster.append([index,position,name,traits,POS,REA,HAN,MAR,TAC,PAS,DRI,OFF,VIS,FIN,ACC,AGG])
                        ##0     1       2      3    4   5   6   7   8   9   10  11  12  13  14  15
    home_stats.append([index,position,name,0,0,0,0,0,0,0,0,0,0])
                       ##0     1       2   3 goal attempt, 4 goal on target, 5 goal made, 6 pass attempt, 7 pass made, 8 tackle attempt, 9 tackle made, 10 interceptions, 11 shots against, 12 shots allowed  
print(away_roster)
print(home_roster)

#roll extra time
extra_time = round(max(random.gauss(150,45),0))
time = 2700 + extra_time
leadershipbonus = 0
print("The first half will be 45 minutes and feature",extra_time // 60,"minutes and",extra_time % 60,"seconds of extra time")

#leadership
def leadership():
    global leadershipbonus
    global offense
    global possession
    if offense == "Home":
        if "Leadership" in home_roster[possession][3]:
            leadershipbonus = 1
            print(home_roster[possession][2],"looks like a real captain out there.")
    elif offense == "Away":
        if "Leadership" in away_roster[possession][3]:
            leadershipbonus = 1
            print(away_roster[possession][2],"looks like a real captain out there.")

#get kickoff possession
def kickoff(x):
    global possession
    global depth
    global offense
    global time
    depth = 2
    if x == "Home":
        i = 0
        while i < len(home_roster):
            x = home_roster[i][0]
            if x == home_mid[0]:
                possession = i
                i += 1
            else:
                i += 1
        if time - extra_time <= 0:
            minutes = str((time - extra_time) // 60)
            seconds = str(-1*(time - extra_time) % 60)
            timelist = [minutes,":",seconds.zfill(2)]
        else:
            minutes = str((time - extra_time) // 60)
            seconds = str((time - extra_time) % 60)
            timelist = [minutes,":",seconds.zfill(2)]
        print("".join(timelist)," And there's the kickoff, with",home_roster[possession][2],"takes possession")
    elif x == "Away":
        i = 0
        while i < len(away_roster):
            x = away_roster[i][0]
            if x == away_mid[0]:
                possession = i
                i += 1
            else:
                i += 1
        if time - extra_time <= 0:
            minutes = str((time - extra_time) // 60)
            seconds = str(-1*(time - extra_time) % 60)
            timelist = [minutes,":",seconds.zfill(2)]
        else:
            minutes = str((time - extra_time) // 60)
            seconds = str((time - extra_time) % 60)
            timelist = [minutes,":",seconds.zfill(2)]
        print("".join(timelist)," And there's the kickoff, with",away_roster[possession][2],"takes possession")

#Determining who's guarding who
def marking():
    global possession
    global offense
    global marking_off
    global marking_def
    global depth
    global time
    away_att2 = away_att[:]
    away_mid2 = away_mid[:]
    away_def2 = away_def[:]
    home_att2 = home_att[:]
    home_mid2 = home_mid[:]
    home_def2 = home_def[:]
    marking_off = []
    marking_def = []
    if offense == "Home":
        i = 0
        while i < len(home_att2):
            q = home_att2[i]
            t = 0
            while t < len(home_roster):
                y = home_roster[t][0]
                if y == q:
                    r = t
                    t += 1
                else:
                    t += 1
            marking_off.append(r)
            try:
                z = random.choice(away_def2)
                away_def2.remove(z)
            except:
                z = random.choice(away_mid2)
                away_mid2.remove(z)
            t = 0
            while t < len(away_roster):
                y = away_roster[t][0]
                if y == z:
                    s = t
                    t += 1
                else:
                    t += 1
            marking_def.append(s)
            i += 1
        i = 0
        while i < len(home_mid2):
            q = home_mid2[i]
            t = 0
            while t < len(home_roster):
                y = home_roster[t][0]
                if y == q:
                    r = t
                    t += 1
                else:
                    t += 1
            marking_off.append(r)
            try:
                try:
                    z = random.choice(away_def2)
                    away_def2.remove(z)
                except:
                    z = random.choice(away_mid2)
                    away_mid2.remove(z)
            except:
                z = random.choice(away_att2)
                away_att2.remove(z)
            t = 0
            while t < len(away_roster):
                y = away_roster[t][0]
                if y == z:
                    s = t
                    t += 1
                else:
                    t += 1
            marking_def.append(s)
            i += 1
        i = 0
        while i < len(home_def2):
            q = home_def2[i]
            t = 0
            while t < len(home_roster):
                y = home_roster[t][0]
                if y == q:
                    r = t
                    t += 1
                else:
                    t += 1
            marking_off.append(r)
            try:
                z = random.choice(away_mid2)
                away_mid2.remove(z)
            except:
                z = random.choice(away_att2)
                away_att2.remove(z)
            t = 0
            while t < len(away_roster):
                y = away_roster[t][0]
                if y == z:
                    s = t
                    t += 1
                else:
                    t += 1
            marking_def.append(s)
            i += 1
    elif offense == "Away":
        i = 0
        while i < len(away_att2):
            q = away_att2[i]
            t = 0
            while t < len(away_roster):
                y = away_roster[t][0]
                if y == q:
                    r = t
                    t += 1
                else:
                    t += 1
            marking_off.append(r)
            try:
                z = random.choice(home_def2)
                home_def2.remove(z)
            except:
                z = random.choice(away_mid2)
                home_mid2.remove(z)
            t = 0
            while t < len(home_roster):
                y = home_roster[t][0]
                if y == z:
                    s = t
                    t += 1
                else:
                    t += 1
            marking_def.append(s)
            i += 1
        i = 0
        while i < len(away_mid2):
            q = away_mid2[i]
            t = 0
            while t < len(away_roster):
                y = away_roster[t][0]
                if y == q:
                    r = t
                    t += 1
                else:
                    t += 1
            marking_off.append(r)
            try:
                try:
                    z = random.choice(home_def2)
                    home_def2.remove(z)
                except:
                    z = random.choice(home_mid2)
                    home_mid2.remove(z)
            except:
                z = random.choice(home_att2)
                home_att2.remove(z)
            t = 0
            while t < len(home_roster):
                y = home_roster[t][0]
                if y == z:
                    s = t
                    t += 1
                else:
                    t += 1
            marking_def.append(s)
            i += 1
        i = 0
        while i < len(away_def2):
            q = away_def2[i]
            t = 0
            while t < len(away_roster):
                y = away_roster[t][0]
                if y == q:
                    r = t
                    t += 1
                else:
                    t += 1
            marking_off.append(r)
            try:
                z = random.choice(home_mid2)
                home_mid2.remove(z)
            except:
                z = random.choice(home_att2)
                home_att2.remove(z)
            t = 0
            while t < len(home_roster):
                y = home_roster[t][0]
                if y == z:
                    s = t
                    t += 1
                else:
                    t += 1
            marking_def.append(s)
            i += 1

#if they'll take a shot
def takeshot(x):
    global offense
    global possession
    global depth
    global time
    take_roll = random.randint(1,60 - x*10 + 10*depth)
    if offense == "Home":
        y = home_roster[possession][15]
        if "Selfish" in home_roster[possession][3]:
            take_roll -= 5
        if take_roll > y:
            result = False
        elif take_roll <= y:
            result = True
            home_stats[possession][3] += 1
    elif offense == "Away":
        y = away_roster[possession][15]
        if "Selfish" in away_roster[possession][3]:
            take_roll -= 5
        if take_roll > y:
            result = False
        elif take_roll <= y:
            result = True
            away_stats[possession][3] += 1
    return result

#is shot on target
def ontarget():
    global offense
    global possession
    global depth
    global marking_off
    global marking_def
    global time
    marking()
    z = marking_off.index(possession)
    rst = marking_def[z]
    if offense == "Home":
        if "Long Range" in home_roster[possession][3] and depth > 1:
            print("Long Range activated")
            target_roll = random.randint(1,10 + (depth-1) * 10)
        else:
            target_roll = random.randint(1,10 + depth * 10)
        y = weightedround(home_roster[possession][14])
        if "Sweeper" in away_roster[rst][3]:
            sweeper_roll = random.randint(1,20)
            if sweeper_roll == 1:
                print("Oh and",away_roster[rst][2],"gets in front of that shot!")
                target_roll = 30
        if target_roll > y:
            result = False
        elif target_roll <= y:
            result = True
            home_stats[possession][4] += 1
    elif offense == "Away":
        if "Long Range" in away_roster[possession][3] and depth > 1:
            print("Long Range activated")
            target_roll = random.randint(1,10 + (depth-1) * 10)
        else:
            target_roll = random.randint(1,10 + depth * 10)
        y = weightedround(away_roster[possession][14])
        if "Sweeper" in home_roster[rst][3]:
            sweeper_roll = random.randint(1,20)
            if sweeper_roll == 1:
                print("Oh and",home_roster[rst][2],"gets in front of that shot!")
                target_roll = 30
        if target_roll > y:
            result = False
        elif target_roll <= y:
            result = True
            away_stats[possession][4] += 1
    time -= weightedround(random.gauss(6,1))
    print(target_roll,y)
    return result

#is it good
def goal(x):
    global offense
    global possession
    global depth
    global time
    global leadershipbonus
    global marking_off
    global marking_def
    global away_score
    global home_score
    global time
    z = marking_off.index(possession)
    rst = marking_def[z]
    if time - extra_time <= 0:
        minutes = str((time - extra_time) // 60)
        seconds = str(-1*(time - extra_time) % 60)
        timelist = [minutes,":",seconds.zfill(2)]
    else:
        minutes = str((time - extra_time) // 60)
        seconds = str((time - extra_time) % 60)
        timelist = [minutes,":",seconds.zfill(2)]
    if x == 1:
        if offense == "Home":
            if "Howitzer" in home_roster[possession][3]:
                howitzercheck = 1
                print("Howitzer activated")
            else:
                howitzercheck = 0
            if "Disruptor" in away_roster[rst][3]:
                disroll = random.randint(1,5)
                if disroll == 5:
                    disruptorcheck = 2
                    print("Great defense by",away_roster[rst][2],"to impact that shot.")
                else:
                    disruptorcheck = 0
            else:
                disruptorcheck = 0
            away_stats[8][11] +=1
            shot_roll = random.randint(0,20)+weightedround(random.gauss(home_roster[possession][13]-disruptorcheck,0.25))+leadershipbonus
            leadershipbonus = 0
            if "Sixth Sense" in away_roster[8][3]:
                thisroll = random.randint(1,5)
                if thisroll == 1:
                    print("Well played by the keeper")
                    a = max(random.randint(0,30),weightedround(random.gauss(away_roster[8][4],0.25)))
                    b = max(random.randint(0,30),weightedround(random.gauss(away_roster[8][4],0.25)))
                    if a > b:
                        position_roll = a
                    else:
                        position_roll = b
                else:
                    position_roll = max(random.randint(0,30),weightedround(random.gauss(away_roster[8][4],0.25)))
            else:
                position_roll = max(random.randint(0,30),weightedround(random.gauss(away_roster[8][4],0.25)))  
            keeper_roll = position_roll+weightedround(random.gauss(away_roster[8][5]-howitzercheck,0.25))
            if "Curveball" in home_roster[possession][3]:
                keeper_roll -= 2
                print("Wow, look at the curve on that shot!")
            if shot_roll > keeper_roll:
                result = True
                away_stats[8][12] +=1
                home_stats[possession][5] +=1
                home_score += 1
                print("".join(timelist)," AND IT GETS PAST THE KEEPER!",home_roster[possession][2],"scores! The score is now","-".join([str(away_score),str(home_score)]))
                time -= weightedround(random.gauss(60,10))
            else:
                result = False
                print("And the keeper stops it!")
            
        elif offense == "Away":
            if "Howitzer" in away_roster[possession][3]:
                howitzercheck = 1
                print("Howitzer activated")
            else:
                howitzercheck = 0
            if "Disruptor" in home_roster[rst][3]:
                disroll = random.randint(1,5)
                if disroll == 5:
                    disruptorcheck = 2
                    print("Great defense by",home_roster[rst][2],"to impact that shot.")
                else:
                    disruptorcheck = 0
            else:
                disruptorcheck = 0
            home_stats[8][11] +=1
            shot_roll = random.randint(0,20)+weightedround(random.gauss(away_roster[possession][13]-disruptorcheck,0.25))+leadershipbonus
            leadershipbonus = 0
            if "Sixth Sense" in home_roster[8][3]:
                thisroll = random.randint(1,5)
                if thisroll == 1:
                    print("Well played by the keeper")
                    a = max(random.randint(0,30),weightedround(random.gauss(home_roster[8][4],0.25)))
                    b = max(random.randint(0,30),weightedround(random.gauss(home_roster[8][4],0.25)))
                    if a > b:
                        position_roll = a
                    else:
                        position_roll = b
                else:
                    position_roll = max(random.randint(0,30),weightedround(random.gauss(home_roster[8][4],0.25)))
            else:
                position_roll = max(random.randint(0,30),weightedround(random.gauss(home_roster[8][4],0.25)))  
            keeper_roll = position_roll+weightedround(random.gauss(home_roster[8][5]-howitzercheck,0.25))
            if "Curveball" in away_roster[possession][3]:
                keeper_roll -= 2
                print("Wow, look at the curve on that shot!")
            if shot_roll > keeper_roll:
                result = True
                home_stats[8][12] +=1
                away_stats[possession][5] +=1
                away_score += 1
                print("".join(timelist)," AND IT GETS PAST THE KEEPER!",away_roster[possession][2],"scores! The score is now","-".join([str(away_score),str(home_score)]))
                time -= weightedround(random.gauss(60,10))
            else:
                result = False
                print("And the keeper stops it!")
        print("shot:",shot_roll,"keep:",keeper_roll)
        return result
    elif x == 2:
        if offense == "Home":
            if "Howitzer" in home_roster[possession][3]:
                howitzercheck = 2
                print("Howitzer activated")
            else:
                howitzercheck = 0
            away_stats[8][11] +=1
            shot_roll = random.randint(0,20)+weightedround(random.gauss(home_roster[possession][13],0.25))+leadershipbonus
            leadershipbonus = 0
            keeper_roll = random.randint(0,20)+weightedround(random.gauss(away_roster[8][5]-howitzercheck,0.25))
            if "Curveball" in home_roster[possession][3]:
                keeper_roll -= 2
                print("Wow, look at the curve on that shot!")
            if shot_roll > keeper_roll:
                result = True
                away_stats[8][12] +=1
                home_stats[possession][5] +=1
                home_score += 1
                print("".join(timelist)," AND IT GETS PAST THE KEEPER!",home_roster[possession][2],"scores! The score is now","-".join([str(away_score),str(home_score)]))
                time -= weightedround(random.gauss(60,10))
            else:
                result = False
                print("And the keeper stops it!")
            
        elif offense == "Away":
            if "Howitzer" in away_roster[possession][3]:
                howitzercheck = 2
                print("Howitzer activated")
            else:
                howitzercheck = 0
            home_stats[8][11] +=1
            shot_roll = random.randint(0,20)+weightedround(random.gauss(away_roster[possession][13],0.25))  
            keeper_roll = random.randint(0,20)+weightedround(random.gauss(home_roster[8][5]-howitzercheck,0.25))
            if "Curveball" in away_roster[possession][3]:
                keeper_roll -= 2
                print("Wow, look at the curve on that shot!")
            if shot_roll > keeper_roll:
                result = True
                home_stats[8][12] +=1
                away_stats[possession][5] +=1
                away_score += 1
                print("".join(timelist)," AND IT GETS PAST THE KEEPER!",away_roster[possession][2],"scores! The score is now","-".join([str(away_score),str(home_score)]))
                time -= weightedround(random.gauss(60,10))
            else:
                result = False
                print("And the keeper stops it!")
        print("shot:",shot_roll,"keep:",keeper_roll)
        return result

#Does the keeper catch the shot or does it reflect
def handling():
    global possession
    global offense
    global marking_off
    global marking_def
    global depth
    global time
    if offense == "Home":
        if "Sticky Hands" in away_roster[8][3]:
            print("Sticky Hands activated")
            handling_roll = random.randint(0,25)
        else:
            handling_roll = random.randint(0,30)
        handle = weightedround(random.gauss(away_roster[8][6],0.25))
        print("Handle:",handle,"Handling Roll",handling_roll)
        if handling_roll <= handle:
            result = True
        else:
            result = False
    elif offense == "Away":
        if "Sticky Hands" in home_roster[8][3]:
            print("Sticky Hands activated")
            handling_roll = random.randint(0,25)
        else:
            handling_roll = random.randint(0,30)
        handle = weightedround(random.gauss(home_roster[8][6],0.25))
        print("Handle:",handle,"Handling Roll",handling_roll)
        if handling_roll <= handle:
            result = True
        else:
            result = False
    return result

#bounce
def bounce():
    global offense
    global depth
    global possession
    bounce_roll = random.randint(1,3)
    if bounce_roll == 1:
        if offense == "Home":
            if "Puncher" in away_roster[8][3]:
                punch_roll = random.randint(1,2)
                if punch_roll == 1:
                    depth = 2
                    print("And",away_roster[8][2],"punches that ball upfield!")
                    possession = random.randint(0,7)
                else:
                    print("But it bounces away")
                    depth = 1
                    ii = home_att.index(random.choice(home_att))
                    possession = ii
            else:
                print("But it bounces away")
                depth = 1
                ii = home_att.index(random.choice(home_att))
                possession = ii
            print("The ball is collected by",home_roster[possession][2])
        elif offense == "Away":
            if "Puncher" in home_roster[8][3]:
                punch_roll = random.randint(1,2)
                if punch_roll == 1:
                    depth = 2
                    print("And",home_roster[8][2],"punches that ball upfield!")
                    possession = random.randint(0,7)
                else:
                    print("But it bounces away")
                    depth = 1
                    ii = away_att.index(random.choice(away_att))
                    possession = ii
            else:
                print("But it bounces away")
                depth = 1
                ii = home_att.index(random.choice(home_att))
                possession = ii
            print("The ball is collected by",away_roster[possession][2])
    else:
        if offense == "Home":
            if "Puncher" in away_roster[8][3]:
                punch_roll = random.randint(1,2)
                if punch_roll == 1:
                    depth = 2
                    print("And",away_roster[8][2],"punches that ball upfield!")
                    possession = random.randint(0,7)
                    offense = "Away"
                else:
                    ii = away_def.index(random.choice(away_def))
                    possession = ii
                    offense = "Away"
                    depth = 3
                print("The ball is collected by",home_roster[possession][2])
        elif offense == "Away":
            if "Puncher" in home_roster[8][3]:
                punch_roll = random.randint(1,2)
                if punch_roll == 1:
                    depth = 2
                    print("And",home_roster[8][2],"punches that ball upfield!")
                    possession = random.randint(0,7)
                    offense = "Home"
                else:
                    ii = home_def.index(random.choice(home_def))
                    possession = ii
                    offense = "Home"
                    depth = 3
                print("The ball is collected by",home_roster[possession][2])

#fouls
def foul():
    global possession
    global offense
    global depth
    global marking_off
    global marking_def
    global time
    z = marking_off.index(possession)
    y = marking_def[z]
    foul_roll = random.randint(1,100)
    if offense == "Home":
        if "Trash Talker" in home_roster[possession][3]:
            foul_roll -= 1
        if "Trash Talker" in away_roster[y][3]:
            foul_roll -= 1
    elif offense == "Away":
        if "Trash Talker" in away_roster[possession][3]:
            foul_roll -= 1
        if "Trash Talker" in home_roster[y][3]:
            foul_roll -= 1
    if foul_roll < 6:
        off_def_roll = random.randint(1,3)
        if offense == "Home":
            if "Trash Talker" in home_roster[possession][3]:
                trash_roll = random.randint(1,5)
                if trash_roll == 1:
                    print("Oh, he better watch his mouth.")
                    off_def_roll -= 1
            if "Trash Talker" in away_roster[y][3]:
                trash_roll = random.randint(1,5)
                if trash_roll == 1:
                    print("Oh, he better watch his mouth.")
                    off_def_roll += 1
        elif offense == "Away":
            if "Trash Talker" in away_roster[possession][3]:
                trash_roll = random.randint(1,5)
                if trash_roll == 1:
                    print("Oh, he better watch his mouth.")
                    off_def_roll -= 1
            if "Trash Talker" in home_roster[y][3]:
                trash_roll = random.randint(1,5)
                if trash_roll == 1:
                    print("Oh, he better watch his mouth.")
                    off_def_roll += 1
        if off_def_roll <= 1:
            side = 1
        else:
            side = 2
        if offense == "Home":
            if side == 1:
                print("Offensive penalty!")
                offense = "Away"
                possession = 5
                result = 1
            else:
                print("Defensive penalty!")
                result = 2
        elif offense == "Away":
            if side == 1:
                print("Offensive penalty!")
                offense = "Home"
                possession = 5
                result = 1
            else:
                print("Defensive penalty!")
                result = 2
    else:
        result = 0
    return result


#dribble and tackle function
def dribble():
    global possession
    global offense
    global depth
    global leadershipbonus
    global marking_off
    global marking_def
    global time
    z = marking_off.index(possession)
    y = marking_def[z]
    time -= weightedround(random.gauss(5,1.5))
    if offense == "Home":
        away_stats[y][8] += 1
        if "Flashy" in home_roster[possession][3]:
            print("Flashy activated")
            dribble_roll = max(random.randint(0,20),10)+weightedround(random.gauss(home_roster[possession][10],0.75))+leadershipbonus
            leadershipbonus = 0
        else:
            dribble_roll = max(random.randint(0,20),10)+weightedround(random.gauss(home_roster[possession][10],0.25))+leadershipbonus
            leadershipbonus = 0
        if "Lockdown" in away_roster[y][3]:
            print("Lockdown activated")
            tackle_roll = random.randint(5,20)+weightedround(random.gauss(away_roster[y][5],0.25))
        else:
            tackle_roll = random.randint(0,20)+weightedround(random.gauss(away_roster[y][5],0.25))
        if dribble_roll >= tackle_roll:
            result = True
        else:
            print(away_roster[y][2],"on the tackle and steals the ball from",home_roster[possession][2])
            result = False
            away_stats[y][9] +=1
            offense = "Away"
            possession = y
    elif offense == "Away":
        home_stats[y][8] += 1
        if "Flashy" in away_roster[possession][3]:
            print("Flashy activated")
            dribble_roll = max(random.randint(0,20),10)+weightedround(random.gauss(away_roster[possession][10],0.75))+leadershipbonus
            leadershipbonus = 0
        else:
            dribble_roll = max(random.randint(0,20),10)+weightedround(random.gauss(away_roster[possession][10],0.25))+leadershipbonus
            leadershipbonus = 0
        if "Lockdown" in home_roster[y][3]:
            print("Lockdown activated")
            tackle_roll = random.randint(5,20)+weightedround(random.gauss(home_roster[y][5],0.25))
        else:
            tackle_roll = random.randint(0,20)+weightedround(random.gauss(home_roster[y][5],0.25))
        if dribble_roll >= tackle_roll:
            result = True
        else:
            print(home_roster[y][2],"on the tackle and steals the ball from",away_roster[possession][2])
            result = False
            home_stats[y][9] +=1
            offense = "Home"
            possession = y
    return result

#passing
def passattempt():
    global possession
    global offense
    global depth
    global leadershipbonus
    global marking_off
    global marking_def
    global time
    time -= weightedround(random.gauss(8,1.5))
    if offense == "Home":
        if "Tactician" in home_roster[possession][3]:
            vision_roll = random.randint(1,30)
            print("Tactician activated")
        else:
            vision_roll = random.randint(1,40)
        vision_stat = home_roster[possession][12]
        if vision_roll <= vision_stat:
            i = 0
            vision_bucket = []
            while i < len(marking_off):
                y = home_roster[i][11]
                z = away_roster[i][7]
                score = int(y) - int(z)
                vision_bucket.append(score)
                i += 1
            max_index = vision_bucket.index(max(vision_bucket))
            q = marking_off[max_index]
            r = q
        else:
            if depth == 3:
                x = random.choice([3,3,2,2])
                depth = x
            elif depth == 2:
                x = random.choice([3,2,2,2,1,1])
                depth = x
            elif depth == 1:
                x = random.choice([2,2,1,1])
                depth = x
            if depth == 3:
                q = random.choice(home_def)
            elif depth == 2:
                q = random.choice(home_mid)
            elif depth == 1:
                q = random.choice(home_att)
        home_stats[possession][6] += 1
        if depth < 1:
            if depth == 3:
                roll = random.randint(0,2)
                if roll == 0:
                    depth = 3
                else:
                    depth = 2
            elif depth == 2:
                roll = random.randint(0,2)
                if roll > 0:
                    pass
                elif roll == 0:
                    depth = 1
        elif depth == 1:
            roll = random.randint(0,2)
            if roll == 0:
                depth = 2
            else:
                depth = 1
        i = 0
        while i < len(home_roster):
            z = home_roster[i][0]
            if z == q:
                r = i
                i += 1
            else:
                i += 1
        z = marking_off.index(r)
        y = marking_def[z]
        pass_roll = random.randint(-10,10)+weightedround(random.gauss(home_roster[possession][9]-10,0.25))+leadershipbonus
        leadershipbonus = 0
        if "Quick" in home_roster[z][3]:
            quick_roll = random.randint(1,5)
            if quick_roll == 1:
                a = random.randint(10,20)+weightedround(random.gauss(home_roster[z][11],0.25))
                b = random.randint(10,20)+weightedround(random.gauss(home_roster[z][11],0.25))
                if a > b:
                    off_roll = a
                else:
                    off_roll = b
            else:
                off_roll = random.randint(10,20)+weightedround(random.gauss(home_roster[z][11],0.25))
        else:
            off_roll = random.randint(10,20)+weightedround(random.gauss(home_roster[z][11],0.25))
        if "Shadow" in away_roster[y][3]:
            thief_roll = random.randint(1,5)
            if thief_roll == 5:
                print("Shadow activated")
                marking_roll = random.randint(10,20)+weightedround(random.gauss(away_roster[y][7],0.25))
            else:
                marking_roll = random.randint(0,20)+weightedround(random.gauss(away_roster[y][7],0.25))
        else:
            marking_roll = random.randint(0,20)+weightedround(random.gauss(away_roster[y][7],0.25))
        pass_score = pass_roll + off_roll - marking_roll
        if "Creative" in home_roster[possession][3]:
            if pass_score > 0:
                print("What a great pass.")
                pass_score += 5
        if pass_score < -20:
            result = 1
        elif -20 <= pass_score <= 0:
            result = 2
            away_stats[y][10] += 1
            possession = y
            offense = "Away"
        elif 0 < pass_score < 20:
            result = 3
            home_stats[possession][7] += 1
            leadership()
            possession = z
        elif pass_score >= 20:
            result = 4
            print("Killer pass by",home_roster[possession][2])
            home_stats[possession][7] += 1
            leadership()
            possession = z
    elif offense == "Away":
        if "Tactician" in away_roster[possession][3]:
            vision_roll = random.randint(1,30)
            print("Tactician activated")
        else:
            vision_roll = random.randint(1,40)
        vision_stat = away_roster[possession][12]
        if vision_roll <= vision_stat:
            i = 0
            vision_bucket = []
            while i < len(marking_off):
                y = away_roster[i][11]
                z = home_roster[i][7]
                score = int(y) - int(z)
                vision_bucket.append(score)
                i += 1
            max_index = vision_bucket.index(max(vision_bucket))
            q = marking_off[max_index]
            r = q
        else:
            if depth == 3:
                x = random.choice([3,3,2,2])
                depth = x
            elif depth == 2:
                x = random.choice([3,2,2,2,1,1])
                depth = x
            elif depth == 1:
                x = random.choice([2,2,1,1])
                depth = x
            if depth == 3:
                q = random.choice(away_def)
            elif depth == 2:
                q = random.choice(away_mid)
            elif depth == 1:
                q = random.choice(away_att)
        away_stats[possession][6] += 1
        if depth < 1:
            if depth == 3:
                roll = random.randint(0,2)
                if roll == 0:
                    depth = 3
                else:
                    depth = 2
            elif depth == 2:
                roll = random.randint(0,2)
                if roll > 0:
                    pass
                elif roll == 0:
                    depth = 1
        elif depth == 1:
            roll = random.randint(0,2)
            if roll == 0:
                depth = 2
            else:
                depth = 1
        i = 0
        while i < len(away_roster):
            z = away_roster[i][0]
            if z == q:
                r = i
                i += 1
            else:
                i += 1
        z = marking_off.index(r)
        y = marking_def[z]
        pass_roll = random.randint(-10,10)+weightedround(random.gauss(away_roster[possession][9]-10,0.25))+leadershipbonus
        leadershipbonus = 0
        if "Quick" in away_roster[z][3]:
            quick_roll = random.randint(1,5)
            if quick_roll == 1:
                a = random.randint(10,20)+weightedround(random.gauss(away_roster[z][11],0.25))
                b = random.randint(10,20)+weightedround(random.gauss(away_roster[z][11],0.25))
                if a > b:
                    off_roll = a
                else:
                    off_roll = b
            else:
                off_roll = random.randint(10,20)+weightedround(random.gauss(away_roster[z][11],0.25))
        else:
            off_roll = random.randint(10,20)+weightedround(random.gauss(away_roster[z][11],0.25))
        if "Shadow" in home_roster[y][3]:
            thief_roll = random.randint(1,5)
            if thief_roll == 5:
                print("Shadow activated")
                marking_roll = random.randint(10,20)+weightedround(random.gauss(home_roster[y][7],0.25))
            else:
                marking_roll = random.randint(0,20)+weightedround(random.gauss(home_roster[y][7],0.25))
        else:
            marking_roll = random.randint(0,20)+weightedround(random.gauss(home_roster[y][7],0.25))
        pass_score = pass_roll + off_roll - marking_roll
        if "Creative" in away_roster[possession][3]:
            if pass_score > 0:
                print("What a great pass.")
                pass_score += 5
        if pass_score < -20:
            result = 1
        elif -20 <= pass_score <= 0:
            result = 2
            home_stats[y][10] += 1
            possession = y
            offense = "Home"
        elif 0 < pass_score < 20:
            result = 3
            away_stats[possession][7] +=1
            leadership()
            possession = z
        elif pass_score >= 20:
            result = 4
            print("Killer pass by",away_roster[possession][2])
            away_stats[possession][7] +=1
            leadership()
            possession = z

#change possession macro
def changepossession(x):
    global possession
    global offense
    global depth
    global time
    if x == 1: ##Shots off target//Keeper catches
        i = 0
        if offense == "Away":
            offense = "Home"
            while i < len(home_roster):
                x = home_roster[i][0]
                if x == home_keep[0]:
                    possession = i
                    keeper = i
                    i += 1
                else:
                    i += 1
            if "Distributor" in home_roster[keeper][3]:
                distributor_bonus = 1
            else:
                distributor_bonus = 0
            t = random.choice(home_keepdepth)
            if t == 3: #return to defense
                q = random.choice(home_def)
                i = 0
                while i < len(home_roster):
                    z = home_roster[i][0]
                    if z == q:
                        possession = i
                        i += 1
                    else:
                        i += 1
                depth = 3
                print("Keeper",home_roster[keeper][2],"rolls the ball to his defender",home_roster[possession][2])
            elif t == 2: #return to midfield
                z = random.randint(1+distributor_bonus,4)
                if z > 2:
                    q = random.choice(home_mid)
                    i = 0
                    while i < len(home_roster):
                        z = home_roster[i][0]
                        if z == q:
                            possession = i
                            i += 1
                        else:
                            i += 1
                    depth = 2
                    print("Keeper",home_roster[keeper][2],"boots the ball into the midfield where it's collected by",home_roster[possession][2])
                else:
                    q = random.choice(away_mid)
                    i = 0
                    while i < len(away_roster):
                        z = away_roster[i][0]
                        if z == q:
                            possession = i
                            i += 1
                        else:
                            i += 1
                    depth = 2
                    offense = "Away"
                    print("Keeper",home_roster[keeper][2],"boots the ball into the midfield, but it's stolen by",away_roster[possession][2])
            elif t == 1: #push on the attack
                z = random.randint(1+distributor_bonus,4)
                if z == 4:
                    q = random.choice(home_att)
                    i = 0
                    while i < len(home_roster):
                        z = home_roster[i][0]
                        if z == q:
                            possession = i
                            i += 1
                        else:
                            i += 1
                    depth = 1
                    print("Keeper",home_roster[keeper][2],"pushes the ball deep into the attack and it connects to",home_roster[possession][2])
                else:
                    q = random.choice(away_def)
                    i = 0
                    while i < len(away_roster):
                        z = away_roster[i][0]
                        if z == q:
                            possession = i
                            i += 1
                        else:
                            i += 1
                    depth = 3
                    offense = "Away"
                    print("Keeper",home_roster[keeper][2],"launches the ball over his teammates where it's easily collected by",away_roster[possession][2])
        elif offense == "Home":
            offense = "Away"
            while i < len(away_roster):
                x = away_roster[i][0]
                if x == away_keep[0]:
                    possession = i
                    keeper = i
                    i += 1
                else:
                    i += 1
            if "Distributor" in away_roster[keeper][3]:
                distributor_bonus = 1
            else:
                distributor_bonus = 0
            t = random.choice(away_keepdepth)
            if t == 3: #return to defense
                q = random.choice(away_def)
                i = 0
                while i < len(away_roster):
                    z = away_roster[i][0]
                    if z == q:
                        possession = i
                        i += 1
                    else:
                        i += 1
                depth = 3
                print("Keeper",away_roster[keeper][2],"rolls the ball to his defender",away_roster[possession][2])
            elif t == 2: #return to midfield
                z = random.randint(1+distributor_bonus,4)
                if z > 2:
                    q = random.choice(away_mid)
                    i = 0
                    while i < len(away_roster):
                        z = away_roster[i][0]
                        if z == q:
                            possession = i
                            i += 1
                        else:
                            i += 1
                    depth = 2
                    print("Keeper",away_roster[keeper][2],"boots the ball into the midfield where it's collected by",away_roster[possession][2])
                else:
                    q = random.choice(home_mid)
                    i = 0
                    while i < len(home_roster):
                        z = home_roster[i][0]
                        if z == q:
                            possession = i
                            i += 1
                        else:
                            i += 1
                    depth = 2
                    offense = "Home"
                    print("Keeper",away_roster[keeper][2],"boots the ball into the midfield, but it's stolen by",home_roster[possession][2])
            elif t == 1: #push on the attack
                z = random.randint(1+distributor_bonus,4)
                if z == 4:
                    q = random.choice(away_att)
                    i = 0
                    while i < len(away_roster):
                        z = away_roster[i][0]
                        if z == q:
                            possession = i
                            i += 1
                        else:
                            i += 1
                    depth = 1
                    print("Keeper",away_roster[keeper][2],"pushes the ball deep into the attack and it connects to",away_roster[possession][2])
                else:
                    q = random.choice(home_def)
                    i = 0
                    while i < len(home_roster):
                        z = home_roster[i][0]
                        if z == q:
                            possession = i
                            i += 1
                        else:
                            i += 1
                    depth = 3
                    offense = "Home"
                    print("Keeper",away_roster[keeper][2],"launches the ball over his teammates where it's easily collected by",home_roster[possession][2])

kickoff_flag = True
offense = "Away"
half = 0
game = True
leadershipbonus = 0
while game == True:
    while time > 0:
        while kickoff_flag == True:
            print("KICKOFF")
            if offense == "Away":
                kickoff("Away")
            elif offense == "Home":
                kickoff("Home")
            kickoff_flag = False
        time -= weightedround(random.gauss(10,2.5))
        leadership()
        shotdepth = 5 - depth
        if takeshot(shotdepth) == True:
            if ontarget() == True:
                if offense == "Home":
                    print("Shot taken by",home_roster[possession][2]," and it's on target.")
                    z = goal(1)
                    if z == True:
                        kickoff_flag = True
                        offense  = "Away"
                        continue
                    elif z == False:
                        t = handling()
                        if t == True:
                            print("The keeper holds on!")
                            changepossession(1)
                            continue
                        else:
                            bounce()
                            continue
                elif offense == "Away":
                    print("Shot taken by",away_roster[possession][2]," and it's on target.")
                    z = goal(1)
                    if z == True:
                        kickoff_flag = True
                        offense = "Home"
                        continue
                    elif z == False:
                        t = handling()
                        if t == True:
                            print("The keeper holds on!")
                            changepossession(1)
                            continue
                        else:
                            bounce()
                            continue
            else:
                if offense == "Home":
                    print("Shot taken by",home_roster[possession][2]," but it's off-target.")
                    changepossession(1)
                elif offense == "Away":
                    print("Shot taken by",away_roster[possession][2]," but it's off-target.")
                    changepossession(1)
        marking()
        dribble()
        zz = passattempt()
        if zz == 1:
            print("And the pass sails into the stands. That'll be the keeper's ball.")
            changepossession(1)
            leadership()
        elif zz == 4:
            shotdepth = 4 - depth
            if takeshot(shotdepth) == True:
                if ontarget() == True:
                    if offense == "Home":
                        print("Shot taken by",home_roster[possession][2]," and it's on target.")
                        z = goal(1)
                        if z == True:
                            kickoff_flag = True
                            offense  = "Away"
                            continue
                        elif z == False:
                            t = handling()
                            if t == True:
                                print("The keeper holds on!")
                                changepossession(1)
                                continue
                            else:
                                print("But it bounces away")
                                bounce()
                                continue
                    elif offense == "Away":
                        print("Shot taken by",away_roster[possession][2]," and it's on target.")
                        z = goal (1)
                        if z == True:
                            kickoff_flag = True
                            offense = "Home"
                            continue
                        elif z == False:
                            t = handling()
                        if t == True:
                            print("The keeper holds on!")
                            changepossession(1)
                            continue
                        else:
                            bounce()
                            continue
                else:
                    if offense == "Home":
                        print("Shot taken by",home_roster[possession][2]," but it's off-target.")
                        changepossession(1)
                    elif offense == "Away":
                        print("Shot taken by",away_roster[possession][2]," but it's off-target.")
                        changepossession(1)
        fouling = foul()
        if fouling == 2:
            if depth == 2 or depth == 3:
                print("And the penalty will result in a freekick.")
                freekick_roll = takeshot(4)
                if freekick_roll == True:
                    if ontarget() == True:
                        if offense == "Home":
                            print("Shot taken by",home_roster[possession][2]," and it's on target.")
                            z = goal(1)
                            if z == True:
                                kickoff_flag = True
                                offense  = "Away"
                                continue
                            elif z == False:
                                t = handling()
                                if t == True:
                                    print("The keeper holds on!")
                                    changepossession(1)
                                    continue
                                else:
                                    bounce()
                                    continue
                        elif offense == "Away":
                            print("Shot taken by",away_roster[possession][2]," and it's on target.")
                            z = goal(1)
                            if z == True:
                                kickoff_flag = True
                                offense = "Home"
                                continue
                            elif z == False:
                                t = handling()
                        if t == True:
                            print("The keeper holds on!")
                            changepossession(1)
                            continue
                        else:
                            bounce()
                            continue
                else:
                    if offense == "Home":
                        print("Shot taken by",home_roster[possession][2]," but it's off-target.")
                        changepossession(1)
                    elif offense == "Away":
                        print("Shot taken by",away_roster[possession][2]," but it's off-target.")
                        changepossession(1)
            elif depth == 1:
                print("And that's a penalty kick!")
                if offense == "Home":
                    possession = home_pk
                elif offense == "Away":
                    possession = away_pk
                if offense == "Home":
                    print("Shot taken by",home_roster[possession][2]," and it's on target.")
                    z = goal(2)
                    if z == True:
                        kickoff_flag = True
                        offense  = "Away"
                        continue
                    elif z == False:
                        t = handling()
                        if t == True:
                            print("The keeper holds on!")
                            changepossession(1)
                            continue
                        else:
                            bounce()
                            continue
                elif offense == "Away":
                    print("Shot taken by",away_roster[possession][2]," and it's on target.")
                    z = goal(2)
                    if z == True:
                        kickoff_flag = True
                        offense = "Home"
                        continue
                    elif z == False:
                        t = handling()
                        if t == True:
                            print("The keeper holds on!")
                            changepossession(1)
                            continue
                        else:
                            bounce()
                            continue
    else:
        if half == 0:
            print("And that's half time! The score is","-".join([str(away_score),str(home_score)]))
            half = 1
            extra_time = round(max(random.gauss(150,45),0))
            time = 2700 + extra_time
            print("The second half will be 45 minutes and feature",extra_time // 60,"minutes and",extra_time % 60,"seconds of extra time")
            kickoff_flag = True
            marking()
            offense = "Home"
            continue
        elif half == 1:
            game = False
else:
    print("And that's the end of the game! The final score is","-".join([str(away_score),str(home_score)]))

filename ="gamedata.csv"
with open(filename, "w") as output:
        writer = csv.writer(output, lineterminator="\n")
        writer.writerows([["Index"]+["Position"]+["Name"]+["GA"]+["GT"]+["GM"]+["PA"]+["PM"]+["TA"]+["TM"]+["INT"]+["SAg"]+["SAl"]])
        writer.writerows(away_stats)
        writer.writerows(home_stats)
