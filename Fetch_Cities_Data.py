import requests
import json

r = requests.get("http://localhost:5000/ClassDash/city")

j=r.json()

state={}


for data in j:
    d=json.loads(json.dumps(data))    
    if d['admin'] not in state:
        state[d['admin']]=[]
        
    state[d['admin']].append(d['city'])



print(len(state))
