import requests
import json
import random
import math

def atan_to_range(x, a, b):
    # Compute the arctangent of x
    arctan_value = math.atan(x)
    
    # Normalize arctan_value from the range [-π/2, π/2] to the range [a, b]
    normalized_value = a + (b - a) * (arctan_value + math.pi / 2) / math.pi
    
    return normalized_value


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

n =100000
profit = 0

balance = 100000
b = 100
a =1


for i in range(n):
    percentage = (i + 1) / n * 100
    print(f'\rProgress: {i + 1}/{n} ({percentage:.2f}%)', end='', flush=True)
    
    bet = atan_to_range(-profit, a, b)
    
    bet = random.uniform(a , b)
    
    if bet < 0:
        raise ValueError("Negative bet")
    
    if balance < bet:
        raise ValueError("Insufficient balance")
    
    
    # Define the input data
    decision = make_absurd_decision()
    
    prob = 0.5
    
    response = random.choices([True, False], weights=[prob, 1-prob], k=1)[0]
  
    
        
    if response == decision:
        profit += bet
        balance += bet
    else:
        profit -= bet
        balance -= bet
        
        
print(f"\nProfit: {profit}")
