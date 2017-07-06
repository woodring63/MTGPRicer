import json 
output_f = open("cards.txt", 'w')
json_file = "AllCards.json"
json_data = open(json_file)
data = json.load(json_data)
json_data.close()
for item in data:
	output_f.write(item.encode('utf-8')+"\n")