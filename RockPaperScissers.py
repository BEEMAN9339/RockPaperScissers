"""
File: RockPaperScissers.py
Description: ----
"""

import time, random

weaponz = ["Rock", "Paper", "Scissors"]

objects = {"R":"Rock", "P":"Paper", "S":"Scissors"}

#just an introduction, and choosing a robot name

print("ROCK-PAPER-SCISSORS")

name = input('What is your name?\n')

robotnamez = ["El Robo", "See3-po", "ↄ0{mpu}TER"]
robotname = random.choice(robotnamez)

print('{} vs. {}'.format(name, robotname))

time.sleep(2)

#The computer picks a random weapon, and we ask the person which item they will use
print("Let's play!")

cweapon = random.choice(weaponz)

#person selecting their object
def pick():
    while True:
       pweapon = input(" Rock, Paper or Scissors? R or P or S\n").upper()
       if pweapon in ("R", "P", "S"):
           print("You say: " + objects[pweapon])
           return pweapon
       else:
           print("Please put R, P, or S")

pweapon = pick()
#calculating the result
print("computer says: %s" % (cweapon))
time.sleep(1)
if pweapon == "R" and cweapon == "Rock":
    print("Tie!")
if pweapon == "R" and cweapon == "Paper":
    print("Paper beats rock! %s wins!" % robotname)
if pweapon == "R" and cweapon == "Scissors":
    print("Rock beats Scissors! %s wins!" % name)

if pweapon == "P" and cweapon == "Rock":
    print("Paper suffocates rock! You are the winner!")
if pweapon == "P" and cweapon == "Paper":
    print("Tie!")
if pweapon == "P" and cweapon == "Scissors":
    print("Scissors cuts paper. You lose. :(")

if pweapon == "S" and cweapon == "Rock":
    print("Rock destroys Scissors! %s wins!" % robotname)
if pweapon == "S" and cweapon == "Paper":
    print("Scissors always beats paper. You are the victor!")
if pweapon == "S" and cweapon == "Scissors":
    print("Tie!")
#more potential results
#---------------------------------------------
if pweapon == "r" and cweapon == "Rock":
    print("Tie!")
if pweapon == "r" and cweapon == "Paper":
    print("Paper beats rock! %s wins!" % robotname)
if pweapon == "r" and cweapon == "Scissors":
    print("Rock beats Scissors! %s wins!" % name)

if pweapon == "p" and cweapon == "Rock":
    print("Paper suffocates rock! You are the winner!")
if pweapon == "p" and cweapon == "Paper":
    print("Tie!")
if pweapon == "p" and cweapon == "Scissors":
    print("Scissors cuts paper. You lose. :(")

if pweapon == "s" and cweapon == "Rock":
    print("Rock destroys Scissors! %s wins!" % robotname)
if pweapon == "s" and cweapon == "Paper":
    print("Scissors always beats paper. You are the victor!")
if pweapon == "s" and cweapon == "Scissors":
    print("Tie!")
