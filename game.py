import requests
import json
import random

API_KEY = ""
def make_absurd_decision():
    # Generate random weights for 'over' and 'under'
    weight_over = random.uniform(0, 1)
    weight_under = 1 - weight_over  # Ensure the total probability is 1
    
    # Choose the decision based on the random weights
    decision = random.choices(
        [True, False],
        weights=[weight_over, weight_under],
        k=1
    )
    return decision[0]

n =1000
profit = 0
for _ in range(n):
    # Define the input data
    input_data = {
        "Bet": 0.0000001,
        "Payout": 2.0,
        "UnderOver": make_absurd_decision(),
        "ClientSeed": "somerandomseed"
    }

    # Define the URL
    url = f"https://api.crypto.games/v1/placebet/BTC/{API_KEY}"

    # Make the POST request
    response = requests.post(url, data=json.dumps(input_data), headers={"Content-Type": "application/json"})

    # Check the response
    if response.status_code == 200:
        print(response.json())
        profit += response.json()["Profit"]
        print(f"Profit: {profit}")
    else:
        print(f"Error: {response.status_code}")
