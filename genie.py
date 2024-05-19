import requests
import json
import sys

API_KEY = "AIzaSyClfcKag4p69iqm31d4sG86ncwOqf2BSm0"

text = ""
if len(sys.argv) > 1:

    text = sys.argv[1]

else:

    exit()

# Check for mathematical operations

if any(char.isdigit() for char in text):
    print(" I’m sorry, I only answer bash specific questions")
else:
    # Define the request body
    content = {

        "contents": [

            {

                "parts": [

                    {"text":"only work if i am talking about bash commands"+ text}



            ]

            }

        ]
    }
    headers = {"Content-Type": "application/json"}
    # Build the URL with your API key
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"
    # Send the POST request
    response = requests.post(url, headers=headers, json=content)
    # Check for successful response
    if response.status_code == 200:
        try:
            # Parse the JSON response
            response_data = response.json().get('candidates')[0].get('content').get('parts')[0].get('text')

            print("Genie:")

            print(response_data)

        except (KeyError, IndexError) as e:

            print("Error: Unable to retrieve generated text. JSON response structure may be different.")

    else:

        print(f"Error: {response.status_code}")

