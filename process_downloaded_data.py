import json
import os
import numpy as np

match_files = os.listdir("../matches/")

print(len(match_files))

attributes = ["kills","deaths","assists","last_hits","denies","gold_per_min","level","hero_damage","tower_damage","hero_healing","gold"]

match_data = {"hero_id": np.empty((0,244))}

for attr in attributes:
	match_data[attr] = np.empty((0,244))

count = 0
skipped = 0
actual_count = 0
pickle_count = 0

for filename in match_files:

	count+=1

	with open("../matches/"+filename, "r") as f:
		data = json.load(f)

	leaver = 0
	for player in data["players"]:
		if "leaver_status" not in player or player["leaver_status"]!=0:
			leaver = 1
			break
	# SOME PLAYERS DONT HAVE LEAVER_STATUS
	# MAYBE THE MATCH IS INVALID FOR SOME OTHER REASONS
	# EXCLUDED FOR NOW

	if data["game_mode"] not in [1,2,3,4,5,8,12,14,16,22] or data["lobby_type"] not in [2,5,6,7] or leaver == 1 or data["human_players"] != 10:
		print(count," skipped")
		skipped+=1
		continue	
	actual_count+=1
	print(count)

	hero_id_array_radiant = np.zeros(122)
	hero_id_array_dire = np.zeros(122)
	for i in range(5):
		hero_id_array_radiant[data["players"][i]["hero_id"]] = 1
		hero_id_array_dire[data["players"][i+4]["hero_id"]] = 1

	match_data["hero_id"] = np.append(match_data["hero_id"], [np.concatenate((hero_id_array_radiant, hero_id_array_dire))], axis = 0)

	for attr in attributes:
		attr_array_radiant = np.zeros(122)
		attr_array_dire = np.zeros(122)
		for i in range(5):
			attr_array_radiant[data["players"][i]["hero_id"]] = data["players"][i][attr]
			attr_array_dire[data["players"][i+4]["hero_id"]] = data["players"][i+4][attr]
		
		match_data[attr] = np.append(match_data[attr], [np.concatenate((attr_array_radiant, attr_array_dire))], axis = 0)

	if actual_count%5000==0:
		pickle_count += 1
		os.system("mkdir ../pickles/"+str(pickle_count))

		for attr in attributes:
			with open("../pickles/"+str(pickle_count)+"/"+attr, "wb") as f:
				np.save(f, match_data[attr])

			with open("../pickles/"+str(pickle_count)+"/hero_id", "wb") as f:
				np.save(f, match_data["hero_id"])

		match_data = {"hero_id": np.empty((0,244))}
		for attr in attributes:
			match_data[attr] = np.empty((0,244))

print("Count", count)
print("Actual Count", actual_count)
print("Skipped", skipped)