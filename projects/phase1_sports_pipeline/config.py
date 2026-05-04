import requests
import os 

api_key = os.environ.get("RAPIDAPI_KEY")

response = requests.get(
    url = "https://free-api-live-football-data.p.rapidapi.com/football-players-search",
    headers={
        'x-rapidapi-key': api_key,
    'x-rapidapi-host': "free-api-live-football-data.p.rapidapi.com",
    'Content-Type': "application/json"
    }    
)

print(response.json())