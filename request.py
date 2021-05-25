import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Text1':"My name is Pooja", 'Text2':"My name is Raja."})

print(r.json())