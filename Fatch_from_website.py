import requests
import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.krisia.com/city_list.htm'

response = requests.get(url)

res_data = BeautifulSoup(response.text, "html.parser")



Data=[]
count=0
for i in res_data.find_all('td'):
    
    if i.string is not None:
        #overwrite some logic because website hase many error class name problem....not proper formating 
        if len(i.string)==1:
            if count%3!=0 and count!=4:
                Data.append(" ")
            count=0
        if len(i.string)!=1 and i.string!="Top":
            Data.append(i.string)
            count+=1

        
Data=Data[4:]

State=[]

state_index=1



for i in range(0,len(Data)):
    

    if i==state_index:
        State.append([Data[i-1],Data[i]])
        state_index+=3

state_cities_dic={}



for i in State:
    if i[1] not in state_cities_dic:
        state_cities_dic[i[1]]=[]

    state_cities_dic[i[1]].append(i[0])

print(state_cities_dic)
        





