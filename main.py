"""
main.py
-------
This is the entry point of the game.
The player interacts with Survivor and Zombie objects here.
Finish off the game logic using the TODO methods from the Survivor and Zombie objects
"""
import os
from survivor import Survivor
from zombie import Zombie

os.system('clear' if os.name != 'nt' else 'cls')

print("~~~ WELCOME TO: THE LAST DAY BEFORE THE LAST DAY ~~~\n")

name = input("Enter your survivor name: ")
player = Survivor(name)

print(f"\nHello {player.name}, you find yourself inside an empty Checkers...")
player.pick_up("Half-eaten energy bar")

print(f"You picked up an item! Inventory: {player.inventory}\n")

z = Zombie(type="Crawler", damage=20)
print("A zombie appears!\n")

choice = input("Do you want to (f)ight or (r)un? ")

if choice.lower() == "f":
    print("\nYou choose to fight!")
    z.attack(player)
else:
    print("\nYou ran! But you tripped and scraped your knee.")
    player.take_damage(5)

os.system('clear' if os.name != 'nt' else 'cls')
print("Current Player State:", player)
decision = input("\nWhat do you want to do?: [l]look around, [f]find shelter, [h]help(get more commands)")
# def start(name):
#     name = input("Enter your survivor name: ")
#     player = Survivor(name)
#     print(f"\nHello {player.name} | {Survivor.health}")




