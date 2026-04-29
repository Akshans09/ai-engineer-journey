import os
import json
import requests


# We'll use two free APIs that need no key for practice

# ---- TASK 1 ----
# Call the GitHub API to get YOUR profile info
# URL: https://api.github.com/users/Akshans09
# Print: your name, public repos count, followers 

response = requests.get("https://api.github.com/users/Akshans09")

print(response.json()["name"])
print(response.json()["public_repos"])
print(response.json()["followers"])



# ---- TASK 2 ----
# Call this free joke API and print a joke
# URL: https://official-joke-api.appspot.com/random_joke
# Print: the setup and punchline separately

joke = requests.get("https://official-joke-api.appspot.com/random_joke")

print(joke.json()["setup"])
print(joke.json()["punchline"])


# ---- TASK 3 ----
# The response from Task 1 is a Python dict after .json()
# Pretty print the ENTIRE GitHub response using json.dumps()
# Hint: json.dumps(data, indent=2) makes it readable
# Look at the output — notice all the fields available

response_string = json.dumps(response.json(), indent=2)
print(response_string)

# ---- TASK 4 ----
# Error handling — what if the API call fails?
# Call this URL which doesn't exist:
# https://api.github.com/users/thisuserdoesnotexist99999
# Print the status code
# Print a message based on status code:
# if 200 → "Success"
# if 404 → "User not found"
# if anything else → "Unexpected error: {status_code}"



user_data = requests.get("https://api.github.com/users/thisuserdoesnotexist99999")

print(user_data.status_code)

if user_data.status_code == 200:
    print("Success")
elif user_data.status_code == 404:
    print("User not found")
else:
    print("unexpected error:", user_data.status_code)



# ---- TASK 5 ----
# Make a POST request to this test API:
# URL: https://httpbin.org/post
# Send this as the body:
# {"name": "Akshan", "phase": "Phase 1", "topic": "REST APIs"}
# Print the "json" field from the response
# This echoes back what you sent — confirms POST worked

sending = requests.post(
    url = "https://httpbin.org/post",
    json={"name": "Akshan", "phase": "Phase 1", "topic": "REST APIs"}
  )

print(sending.json()["json"])