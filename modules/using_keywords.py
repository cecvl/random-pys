# from , as keywords
# calculate surface areas of planets

from math import pi , floor , ceil
from random import choice as ch

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]
random_planet = ch(planets)

if random_planet == "Mercury":
    r = 2440
elif random_planet == "Venus":
    r = 6052
elif random_planet == "Earth":
    r = 6371
elif random_planet == "Mars":
    r = 3390
elif random_planet == "Saturn":
    r = 58232
else:
    print("Oops! An error occurred.")

print(f"radius of {random_planet} = {r} km")

def area(r):
    return 4 * pi * r**2
def print_area(random_planet,r):
    print(f"The area of {random_planet} is {ceil(area(r))} square kilometers.")

print_area(random_planet,r)

