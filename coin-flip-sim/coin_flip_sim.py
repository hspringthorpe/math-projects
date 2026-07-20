import random
import matplotlib.pyplot as plt
import numpy as np

coin = ["H", "T"]


def main():
    user_input = int(input("How many coin flips would you like? "))
    result = coin_flip(user_input)
    print(result)
    print(f"Above are the outcomes from {user_input} flips")
    print(f"The probability of getting heads is {round((heads_probability(result)*100), 2)}%")
    print(f"The probability of getting tails is {round((tails_probability(result)*100), 2)}%")
    movement = outcome_movement(result)
    plot(movement)


#returns number of random choices from list coin
def coin_flip(n):
    event = []
    for _ in range(n):
        flip = random.choice(coin)
        event.append(flip)
    return event

#probability of getting heads
def heads_probability(event):
    heads = event.count("H")
    total = len(event)
    heads_prob = heads/total
    return heads_prob

#probability of getting tails
def tails_probability(event):
    tails = event.count("T")
    total = len(event)
    tails_prob = tails/total
    return tails_prob


#shows the movement of the heads and tails by +1 for heads and -1 for tails for use in plotting
def outcome_movement(event):
    outcome = 0
    outcome_list = [0]
    for i in event:
        if i == "H":
            outcome += 1
            outcome_list.append(outcome)
        elif i == "T":
            outcome -= 1
            outcome_list.append(outcome)
        
    return outcome_list

#plot the movement on a graph
def plot(movement):
    flips = len(movement) - 1
    plt.plot(range(len(movement)),movement)
    plt.xlabel("Number of Outcomes")
    plt.ylabel("Heads (up) or Tails (down)")
    plt.title(f"Outcome of {flips} Coin Flips")
    plt.show()


if __name__ == "__main__":
    main()