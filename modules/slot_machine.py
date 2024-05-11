import random

symbols = ['cherry',' grape', 'melon', '7']
jackpot = ['7','7','7']
results = []

results = random.choices(symbols, k=3)

print(results)

if results == jackpot:
        print("JACKPOT!")
else :
        print("Thanks for playing!")

# play() function
# while loop for player to keep playing
# input() function to ask Yes or No