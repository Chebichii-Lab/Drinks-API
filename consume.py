import requests

response = requests.get('http://127.0.0.1"8000/drinks')
print(response.json())

# gets the json on the browser to the terminal by running python3.8 consume.py