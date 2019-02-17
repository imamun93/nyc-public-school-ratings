import urllib.request, json 

with urllib.request.urlopen("https://data.cityofnewyork.us/resource/qwy7-5t54.json") as url:
    data = json.loads(url.read().decode())
    print(data)