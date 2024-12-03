import requests


term = input("Let me tell you a joke! Give me a topic: ") 
  
response_json = requests.get("https://icanhazdadjoke.com/search", 
                             headers={"Accept": "application/json"}, params={"term": term}).json() 
  
results = response_json["results"] 

if results:
    print(results[0]['joke'])
else:
    print('Sorry, I don\'t have a joke for you')
