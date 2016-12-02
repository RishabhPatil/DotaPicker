var http = require('http');
var jsonfile = require('jsonfile')

function getTestPersonaLoginCredentials(min,max,data) {
    if(min<max){
        http.get({
            host: 'api.steampowered.com',
            path: '/IDOTA2Match_570/GetMatchHistoryBySequenceNum/v0001/?start_at_match_seq_num='+min+'&key=C4B5D001E352AB612DCECABBFAB949B1'
        }, function(response) {
            // Continuously update stream with data
            var body = '';
            response.on('data', function(d) {
                body += d;
            });
            response.on('end', function() {
                console.log("hello world "+min+" "+max+" "+data.length);
                if(min<max)
                {
                    // Data reception is done, do whatever with it!

                    var parsed = JSON.parse(body);
                    // data.push(parsed);
                    // console.log(data);
                    var matches=parsed.result.matches;
                    var toadd=[];
                    for(var i=0;i<matches.length;i++)
                    {
                        if(matches[i]["match_seq_num"]<max)
                        {
                            if(matches[i]["start_time"]>1476785907)
                            {
                                if(matches[i]["human_players"]==10)
                                {
                                    if(matches[i]["game_mode"]==0 || matches[i]["game_mode"]==6 || matches[i]["game_mode"]==7 || matches[i]["game_mode"]==9 || matches[i]["game_mode"]==10 || matches[i]["game_mode"]==11 || matches[i]["game_mode"]==15 || matches[i]["game_mode"]==18 || matches[i]["game_mode"]==20 || matches[i]["game_mode"]==21)
                                    {
                                        var addingMatch=true;
                                        for(var j=0;j<10;j++)
                                        {
                                            if(matches[i]["players"][j]["leaver_status]"]==-1 || matches[i]["players"][j]["leaver_status]"]==3 || matches[i]["players"][j]["leaver_status]"]==4 || matches[i]["players"][j]["leaver_status]"]==8)
                                            {
                                                addingMatch=false;
                                                break;
                                            }
                                        }
                                        if(addingMatch)
                                        {
                                            toadd.push(matches[i]);
                                        }
                                    }
                                }
                            }
                        }
                        else
                        {
                            break;  
                        }
                    }
                    data=data.concat(toadd);
                    getTestPersonaLoginCredentials(matches[matches.length-1]["match_seq_num"]+1,max,data)
                }
                else{
                    console.log("wrote");
                    var file = 'data.json';
         
                    var dataFile=jsonfile.readFileSync(file);
                    data=dataFile.concat(data);
                    jsonfile.writeFileSync(file, data);
                }
            });
        });
    }
    else{
        console.log("wrote");
        var file = 'data.json';

        var dataFile=jsonfile.readFileSync(file);
        data=dataFile.concat(data);
        jsonfile.writeFileSync(file, data);
    }
}

getTestPersonaLoginCredentials(parseInt(process.argv[2]),parseInt(process.argv[3]),[]);