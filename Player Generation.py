import math
import random
import csv
import re

players_to_gen = 350
firstname = []
lastname = []
players = []
base = []
countries = ["USA","CAN","MEX","CRC"]
position_base = [1,1,2,3,3,4,5,5,6]
att_skill = ["Long Range","Howitzer","Curveball","Selfish"]
mid_skill = ["Flashy","Tactician","Creative","Quick"]
def_skill = ["Shadow","Lockdown","Sweeper","Disruptor","Contrattacco"]
gk_skill = ["Distributor","Sixth Sense","Sticky Hands","Puncher"]
gen_skill = ["Trash Talker","Leadership"]
with open('player_gen.csv', newline='',encoding="utf-8") as csvfile:
     reader = csv.reader(csvfile, delimiter=',')
     for row in reader:
         base.append(row)


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

def weightedroundhalf(x):
    halfround = round(x*2)/2
    if halfround < x:
        adjust_floor = halfround
        adjust_ceiling = halfround + 0.5
        roll = random.uniform(adjust_floor,adjust_ceiling)
        if roll < x:
            result = adjust_ceiling
        else:
            result = adjust_floor
    else:
        adjust_ceiling = halfround
        adjust_floor = halfround - 0.5
        roll = random.uniform(adjust_floor,adjust_ceiling)
        if roll < x:
            result = adjust_ceiling
        else:
            result = adjust_floor
    return result

print(base)

i = 0
while i < players_to_gen:
    #position
    x = random.choice(position_base)
    position = base[x][0]
    
    #physicals
    ht = weightedround(random.gauss(74,2))
    if x == 6: #gk height boost
        ht += 4
    height = str(ht // 12)+"-"+str(ht % 12)
    weight = weightedround(random.gauss(200,10))

    #country
    country = random.choice(countries)
    cities_file = "cities_"+country+".csv"
    cities = []
    with open(cities_file, newline='',encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            cities.append(row)
    city = random.choice(cities)

    #name
    firstname = []
    lastname = []
    first_file = "first_"+country+".csv"
    with open(first_file, newline='',encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
             firstname.append(row)

    last_file = "last_"+country+".csv"
    with open(last_file, newline='',encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
             lastname.append(row)

    first_name = random.choice(firstname)
    last_name = random.choice(lastname)
    name = ' '.join(first_name + last_name)
    
    #skill
    skillroll = random.randint(1,20)
    if skillroll <= 8:
        skillroll2 = random.randint(1,20)
        if skillroll2 == 20:
            twoskills = True
        else:
            twoskills = False
        if x == 1: #ST
            if skillroll <= 5:
                skill = random.choice(att_skill)
            elif 5 < skillroll <= 7:
                skill = random.choice(mid_skill)
            else:
                skill = random.choice(gen_skill)
            if twoskills == True:
                flip = random.randint(1,2)
                if flip == 1:
                    skill_two = random.choice(att_skill)
                    while skill == skill_two:
                        skill_two = random.choice(att_skill)
                else:
                    skill_two = random.choice(mid_skill)
                    while skill == skill_two:
                        skill_two = random.choice(mid_skill)
                skillbucket = [skill,skill_two]
                skill = skillbucket
        elif x == 2: #AM
            if skillroll <= 3:
                skill = random.choice(att_skill)
            elif 3 < skillroll <= 7:
                skill = random.choice(mid_skill)
            else:
                skill = random.choice(gen_skill)
            if twoskills == True:
                flip = random.randint(1,2)
                if flip == 1:
                    skill_two = random.choice(att_skill)
                    while skill == skill_two:
                        skill_two = random.choice(att_skill)
                else:
                    skill_two = random.choice(mid_skill)
                    while skill == skill_two:
                        skill_two = random.choice(mid_skill)
                skillbucket = [skill,skill_two]
                skill = skillbucket
        elif x == 3: #MF
            if 1 <= skillroll <= 2:
                skill = random.choice(att_skill)
            elif 2 < skillroll <= 5:
                skill = random.choice(mid_skill)
            elif 5 < skillroll <= 7:
                skill = random.choice(def_skill)
            else:
                skill = random.choice(gen_skill)
            if twoskills == True:
                flip = random.randint(1,3)
                if flip == 1:
                    skill_two = random.choice(att_skill)
                    while skill == skill_two:
                        skill_two = random.choice(att_skill)
                elif flip == 2:
                    skill_two = random.choice(mid_skill)
                    while skill == skill_two:
                        skill_two = random.choice(mid_skill)
                else:
                    skill_two = random.choice(def_skill)
                    while skill == skill_two:
                        skill_two = random.choice(def_skill)
                skillbucket = [skill,skill_two]
                skill = skillbucket
        elif x == 4: #DM
            if skillroll <= 3:
                skill = random.choice(def_skill)
            elif 3 < skillroll <= 7:
                skill = random.choice(mid_skill)
            else:
                skill = random.choice(gen_skill)
            if twoskills == True:
                flip = random.randint(1,2)
                if flip == 1:
                    skill_two = random.choice(def_skill)
                    while skill == skill_two:
                        skill_two = random.choice(def_skill)
                else:
                    skill_two = random.choice(mid_skill)
                    while skill == skill_two:
                        skill_two = random.choice(mid_skill)
                skillbucket = [skill,skill_two]
                skill = skillbucket
        elif x == 5: #DB
            if skillroll <= 5:
                skill = random.choice(def_skill)
            elif 5 < skillroll <= 7:
                skill = random.choice(mid_skill)
            else:
                skill = random.choice(gen_skill)
            if twoskills == True:
                flip = random.randint(1,2)
                if flip == 1:
                    skill_two = random.choice(def_skill)
                    while skill == skill_two:
                        skill_two = random.choice(def_skill)
                else:
                    skill_two = random.choice(mid_skill)
                    while skill == skill_two:
                        skill_two = random.choice(mid_skill)
                skillbucket = [skill,skill_two]
                skill = skillbucket
        elif x == 6: #GK
            skill = random.choice(gk_skill)
            if twoskills == True:
                skill_two = random.choice(gk_skill)
                while skill == skill_two:
                    skill_two = random.choice(gk_skill)
                skillbucket = [skill,skill_two]
                skill = skillbucket

    else:
        skill = ""

    #potential
    potential_roll = random.randint(1,100)
    if potential_roll <= 5:
        potential = 1.0
    elif 5 < potential_roll < 15:
        potential = 1.5
    elif 15 <= potential_roll < 25:
        potential = 2.0
    elif 25 <= potential_roll < 35:
        potential = 2.5
    elif 35 <= potential_roll < 50:
        potential = 3.0
    elif 50 <= potential_roll < 70:
        potential = 3.5
    elif 70 <= potential_roll < 80:
        potential = 4.0
    elif 80 <= potential_roll < 87:
        potential = 4.5
    elif 87 <= potential_roll < 94:
        potential = 5.0
    elif 94 <= potential_roll < 99:
        potential = 5.5
    elif 99 <= potential_roll:
        potential = 6.0
    pot = potential
    pos_p = max(weightedround(random.gauss(float(base[x][1])*pot,float(base[x][2]))),0)
    rea_p = max(weightedround(random.gauss(float(base[x][3])*pot,float(base[x][4]))),0)
    han_p = max(weightedround(random.gauss(float(base[x][5])*pot,float(base[x][6]))),0)
    mar_p = max(weightedround(random.gauss(float(base[x][7])*pot,float(base[x][8]))),0)
    tac_p = max(weightedround(random.gauss(float(base[x][9])*pot,float(base[x][10]))),0)
    pas_p = max(weightedround(random.gauss(float(base[x][11])*pot,float(base[x][12]))),0)
    dri_p = max(weightedround(random.gauss(float(base[x][13])*pot,float(base[x][14]))),0)
    off_p = max(weightedround(random.gauss(float(base[x][15])*pot,float(base[x][16]))),0)
    vis_p = max(weightedround(random.gauss(float(base[x][17])*pot,float(base[x][18]))),0)
    fin_p = max(weightedround(random.gauss(float(base[x][19])*pot,float(base[x][20]))),0)
    acc_p = max(weightedround(random.gauss(float(base[x][21])*pot,float(base[x][22]))),0)
    agg_p = max(weightedround(random.gauss(float(base[x][23])*pot,float(base[x][24]))),0)

    #overall
    if x == 1: #ST
        fin_p += 1
        acc_p += 1
        off_p += 1
        p_overall = weightedround(35 + dri_p/20*7.5 + off_p/20*7.5 + vis_p/20*5 + fin_p/20*20 + acc_p/20*20)
    elif x == 2: #AM
        vis_p += 1
        pas_p += 1
        fin_p += 1
        p_overall = weightedround(35 + pas_p/20*12.5 + dri_p/20*7.5 + off_p/20*10 + vis_p/20*15 + fin_p/20*10 + acc_p/20*5)
    elif x == 3: #MF
        pas_p += 1
        dri_p += 1
        vis_p += 1
        p_overall = weightedround(35 + mar_p/20*5 + tac_p/20*5 + pas_p/20*17.5 + dri_p/20*12.5 + off_p/20*10 + vis_p/20*15)
    elif x == 4: #DM
        mar_p += 1
        pas_p += 1
        vis_p += 1
        p_overall = weightedround(35 + mar_p/20*15.5 + tac_p/20*13 + pas_p/20*14 + dri_p/20*12.5 + vis_p/20*5)
    elif x == 5: #DB
        mar_p += 1
        tac_p += 1
        pas_p += 1
        p_overall = weightedround(35 + mar_p/20*17 + tac_p/20*22.5 + pas_p/20*10 + dri_p/20*7.5 + vis_p/20*3)
    elif x == 6: #GK
        pos_p += 1
        rea_p += 1
        han_p += 1
        p_overall = weightedround(35 + pos_p/20*25 + rea_p/20*25 + han_p/20*10)
    #put it all together
    players.append([position,name,height,weight,city,potential,skill,pos_p,rea_p,han_p,mar_p,tac_p,pas_p,dri_p,off_p,vis_p,fin_p,acc_p,agg_p,p_overall])
    i += 1

filename ="drafteligibles.csv"
with open(filename, "w",encoding="utf8") as output:
        writer = csv.writer(output, lineterminator="\n")
        writer.writerows(players)
