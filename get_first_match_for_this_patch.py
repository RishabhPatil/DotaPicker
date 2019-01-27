#########
#IMPORTS#
#########

import json
import requests
import time

######
#INIT#
######

#As of 7.20 
patch_timestamp = 1542653251

query_text = "http://api.steampowered.com/IDOTA2Match_570/GetMatchHistoryBySequenceNum/v1/"

params = {	"key":"ENTER KEY HERE",
			"start_at_match_seq_num" : 3664399100}

###########
#FUNCTIONS#
###########

def get_first_match(params):

	while True:
		try:
			response = requests.get(query_text, params = params)
			json_response = response.json()
			break
		except:
			print("Error:",response.status_code)
			time.sleep(2)

	if 'status' in json_response['result'] and json_response['result']['status']==1:

		match_0 = json_response['result']['matches'][0]
		start_time_0 = match_0['start_time']

		match_f = json_response['result']['matches'][-1]
		start_time_f = match_f['start_time']

		if start_time_f < patch_timestamp:
			params["start_at_match_seq_num"] += 1
			print("Still not there")
			print("Starting at ",params["start_at_match_seq_num"])
			return get_first_match(params)
		elif start_time_0 > patch_timestamp or len(json_response['result']['matches'])==0:
			params["start_at_match_seq_num"] -= 1
			print("Overshot")
			print("Starting at ", params["start_at_match_seq_num"])
			return get_first_match(params)
		else:

			for i in json_response['result']['matches']:
				start_time = i['start_time']

				if patch_timestamp < start_time:
					print("Match ID:",i["match_id"])
					print("Match Seq Num:",i["match_seq_num"])
					return 0
	else:
		print("status failed")
		return -1

get_first_match(params)
######