import time
import random
#just an introduction, and choosing a robot name
print("ROCK-PAPER-SCISSORS")
Name = input('What is your name?\n')
robotnamez = ["El Robo", "See3-po", "ↄ0{mpu}TER"]
robotname = random.choice(robotnamez)
print('{} vs. {}'.format(Name, robotname))
time.sleep(2)
#The computer picks a random weapon, and we ask the person which item they will use
print("Let's play!")
pweapon = input(" Rock, Paper or Scissors? R or P or S\n")
cweaponzz = ["Rock", "Paper", "Scissors"]
cweapon = (random.choice(cweaponzz))


#person selecting their object
def Pick():
    while True:
        if pweapon.upper() == "R":
            print("You say: Rock")
            return True
        elif pweapon.upper() == "P":
            print("You say: Paper")
            return True
        elif pweapon.upper() == "S":
            print("You say: Scissors")
            return True
        else:
          print("Please put R, P, or S")
          Pick()
          return False

Pick()
#calculating the result
print("computer says: %s" % (cweapon))
time.sleep(1)
if pweapon == "R" and cweapon == "Rock":
    print("Tie!")
if pweapon == "R" and cweapon == "Paper":
    print("Paper beats rock! %s wins!" % robotname)
if pweapon == "R" and cweapon == "Scissors":
    print("Rock beats Scissors! %s wins!" % Name)

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
    print("Rock beats Scissors! %s wins!" % Name)

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
