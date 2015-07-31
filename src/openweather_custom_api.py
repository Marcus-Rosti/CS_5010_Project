#this is just an example
import json

f = open('../data/example.json','r')

weather_json=f.read()

weather_json=weather_json.rstrip('\n')

print(json.dumps(weather_json,sort_keys=True,indent=1))
