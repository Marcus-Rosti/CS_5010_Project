import urllib.request
import json

def extractor(start_time, end_time):
    # Create the url that needs to access
    url = "http://api.openweathermap.org/data/2.5/history/city?id=4752046&type=hour&start="+str(start_time)+"&end="+str(end_time)

    # Open the url
    response = urlopen(url)

    # Read-in the JSON file and return the value
    JSONFile = response.read()
    return JSONFile
