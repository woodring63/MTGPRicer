from mtgsdk import Card
import json
import urllib.request
req = urllib.request.Request("https://api.magicthegathering.io/v1/cards?name=humility", headers={'User-Agent': 
	'Mozilla/5.0'})
card = urllib.request.urlopen(req)
data = json.load(card)
print(data['cards'][len(data['cards'])-1]['text'])

