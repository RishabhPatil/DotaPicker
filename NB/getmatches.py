import urllib, json
t=0
with open('lastmatch','r') as f:
    t=int(f.read())
count=0
while(1):
    print count,t
    url = "https://api.steampowered.com/IDOTA2Match_570/GetMatchHistoryBySequenceNum/V001/?skill=3&date_min=1481478892&start_at_match_seq_num="+str(t)+"&key=C4B5D001E352AB612DCECABBFAB949B1"
    response = urllib.urlopen(url)
    d=response.read()
    data = json.loads(d)
    for match in data["result"]["matches"]:
        if (match["game_mode"] in [1,2,3,4,5,8,12,14,16,22]) and (match["lobby_type"] in [0,2,7]) and match["human_players"]==10:
            invalid=0
            for player in match["players"]:
                if player["leaver_status"] not in [0,1]:
                    print "DC:        ",match["match_seq_num"]
                    invalid=1
                    break
            if invalid==0:
                with open("matches/"+str(match["match_id"]),'w') as f:
                    f.write(json.dumps(match))
                    print "Valid:   ",match["match_seq_num"]
            else:
                with open("matches1/"+str(match["match_id"]),'w') as f:
                    f.write(json.dumps(match))
        else:
            print "Invalid: ",match["match_seq_num"]
        t=match["match_seq_num"]
        with open('lastmatch','w') as f:
            f.write(str(t))
    count+=1

#7.00 first match 2499864431

#CONSTRAINTS
#valid lobby_type 0 7 2
#Valid leaver_status 0 1
#game_modes 1 2 3 4 5 8 12 16 14 22
#status==1
#human_players == 10
#See: https://wiki.teamfortress.com/wiki/WebAPI/GetMatchDetails
