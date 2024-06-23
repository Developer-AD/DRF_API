import requests

print('----------------------- Python Application Start -----------------------------')
# id = input('Enter Student Id : ')
# response = requests.get(f'http://127.0.0.1:8000/stdinfo/{id}')
response = requests.get(f'http://127.0.0.1:8000/stdinfo')
data = response.json()
print(data)
print('----------------------- Python Application End -----------------------------')