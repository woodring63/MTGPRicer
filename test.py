from mtgsdk import Card
import json
import urllib.request
card = Card.where(name="garruk, primal hunter").all()
print(card[0].text)

