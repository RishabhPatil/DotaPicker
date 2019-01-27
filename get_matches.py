import json
import requests
import state
import time

query_text = "http://api.steampowered.com/IDOTA2Match_570/GetMatchHistoryBySequenceNum/v1/"

params = {	"key":"ENTER KEY HERE",
			"start_at_match_seq_num" : state.seq_num}
# org_num = 3664399107 1st match for patch 7.20

while True:
	while True:
		try:
			response = requests.get(query_text, params = params)
			json_response = response.json()
			break
		except:
			print("Error:",response.status_code)
			time.sleep(2)

	if 'status' in json_response['result'] and json_response['result']['status'] == 1:
		last_seq_num = 0
		for i in range( len(json_response['result']['matches']) ):
			print(json_response['result']['matches'][i]["match_seq_num"])
			with open("matches/"+str(json_response['result']['matches'][i]["match_id"])+".json",'w') as f:
				json.dump( json_response['result']['matches'][i], f )
			last_seq_num = 	json_response['result']['matches'][i]["match_seq_num"]

	with open("state.py","w") as f:
		f.write("seq_num = "+str(last_seq_num+1))

	params["start_at_match_seq_num"] = last_seq_num+1
