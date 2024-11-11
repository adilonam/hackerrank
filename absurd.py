import random

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

# Example usage
decision = make_absurd_decision()
print(f"The absurd decision is: {decision}")

