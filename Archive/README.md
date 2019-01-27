# DotaPicker

Run the following shell script in the folder Data

1) Without proxy i.e running at home :  

	$ bash run.sh start_match_sequence_number end_match_sequence_number

2) With proxy i.e. when running in college on PICT wifi : 

	$ bash runWithProxy.sh start_match_sequence_number end_match_sequence_number

to change the proxy ip and post go in scriptWithProxy.js and change the ip in the key "host" and port number in the "port" key

Preferably end_match_sequence_number-start_match_sequence_number=2000

otherwise the code fails

The first match sequence number is 2372531764 for the first game played for the new version
