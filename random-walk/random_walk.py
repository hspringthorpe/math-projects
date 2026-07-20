import random
import matplotlib.pyplot as plt
import numpy as np

#be aware that a very large number input will be very labour intensive for your computer

coin = ["H", "T"]
walk_num = 5


def main():
    user_input = int(input("How many coin flips would you like? "))
    movements = []
    #runs the same simulation walk_num times
    for _ in range(walk_num):
        result = coin_flip(user_input)
        movements.append(outcome_movement(result))

    print(f"Here we have shown the simulation of {user_input} coin flips {walk_num} times, giving us {walk_num} random walks.")

    plot(movements)


#returns number of random choices from list coin
def coin_flip(n):
    event = []
    for _ in range(n):
        flip = random.choice(coin)
        event.append(flip)
    return event


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

#plot the movements on a graph
def plot(movements):
    for i, movement in enumerate(movements, start=1):
        plt.plot(range(len(movement)),movement, label={i})
    length = len(movements[0])-1
    plt.xlabel("Number of Outcomes")
    plt.ylabel("Heads (up) or Tails (down)")
    plt.title(f"Simulation of {length} coin flips {walk_num} times")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
