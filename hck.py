#Hacker

#---------------------------------
#Imports
#---------------------------------

import random
import time
import datetime
import sys
import os
from termcolor import colored, cprint

#---------------------------------
#Misc
#---------------------------------

#Colour Names
'''
>>> palette.keys() # Available colors.
['pink', 'yellow', 'cyan', 'magenta', 'blue', 'gray', 'default', 'black', 'green', 'white', 'red']
>>> highlighter.keys() # Available highlights.
['blue', 'pink', 'gray', 'black', 'yellow', 'cyan', 'green', 'magenta', 'white', 'red']
>>> formatter.keys() # Available formatter, 
[ 'bold' 'underline', 'blinking', 'reverse']        
'''

#---------------------------------
#Functions 
#---------------------------------

#Display the text character by character

def write(str):
  for char in str:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)
  print("")

#Game Over
def gameOver():
  os.system("cls")
  text = colored("Well, look what you've got yourself into now.\nI'd get comfy if I were you; something is telling me you'll be here a while.\nCan I borrow your computer? I don't think you'll be needing it any time soon. \nGood, because I've already sold it.\nMaybe you should have been more careful...\nHow's the cell?\n", "grey")
  write(text)
  text = colored("Your worst nightmare,", "grey")
  write(text)
  text = colored("Oni.", "red")
  write(text)
  endText = colored("  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  \n ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒\n▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒\n░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  \n░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒\n ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░\n  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░\n░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ \n      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     \n                                                     ░                   ", "red", "on_white")
  print(endText)
  text = colored("Thank you for playing!", "green")
  write(text)
  quit()
  


  
#Update the suspicion variable
def updateSuspicion(suspicionUpdate):
  global suspicion
  suspicion += suspicionUpdate
  if suspicion < 0:
    suspicion = 0
  if suspicionUpdate > 0:
    text = colored("Suspicion level increased by {}.".format(suspicionUpdate), "red")
    write(text)
  elif suspicionUpdate < 0:
    text = colored("Suspicion level decreased by {}".format(abs(suspicionUpdate)), "green")
    write(text)
  if suspicion >= 5:
    text = colored("You were caught being suspicious. Fine = £500", "red")
    write(text)
    text = colored("Press ENTER to pay the fine.", "red")
    write(text)
    input("")
    if bankBalance >= 500:
      updateBalance(-500)
    else:
      gameOver()
  
#Update the networkLimit variable
def upgradeYokai():
  global networkLimit
  networkLimit = networkLimit * 2
  text = colored("Yokai upgraded to target more personal data.\nMaximum data selling price = £{}".format(networkLimit), "grey")
  write(text)
  text = colored("Press ENTER to return to Yokai.", "grey")
  write(text)
  input("")
  os.system("cls")
  updateBalance(-1000)

  
#Update the player's balance
def updateBalance(moneyUpdate):
  global bankBalance
  bankBalance += moneyUpdate
  openYokai()

#Display Commands
def yokaiHelp():
  os.system("cls")
  text = colored("Commands:\n   (A)ccess Network\n   (B)uy Stocks\n   (C)heck Balance\n   (V)isit Black Market\n   (W)ork", "green")
  write(text)
  openYokai()

#Access the hacker network
def accessNetwork():
  #Connect to the network
  os.system("cls")
  text = colored("Accessing Network", "green")
  write(text)
  time.sleep(0.5)
  os.system("cls")
  text = colored("Accessing Network.", "green")
  print(text)
  time.sleep(0.5)
  os.system("cls")
  text = colored("Accessing Network..", "green")
  print(text)
  time.sleep(0.5)
  os.system("cls")
  text = colored("Accessing Network...", "green")
  print(text)
  time.sleep(0.5)
  os.system("cls")
  timeNow = datetime.datetime.now()
  timeNow = timeNow.strftime("%c")
  text = colored("Network Connection Established at " + timeNow, "green")
  write(text)
  #Extract data minigame
  for x in range(0,5):
    code = ""
    for i in range (0,5):
      code += chr(random.randint(64,122))
    text = colored("Repeat the code to extract the data or type 'quit' to disconnect.: {}   ({}/5)".format(code, x), "green")
    print(text)
    answer = input("")
    os.system("cls")
    if answer == code:
      text = colored("Correct!", "green")
      write(text)
    elif answer.lower() == "quit":
      text = colored("Disconnecting from network...", "green")
      write(text)
      time.sleep(1)
      os.system("cls")
      openYokai()
    else:
      text = colored("Incorrect. Data lost.", "green")
      write(text)
      time.sleep(1)
      updateSuspicion(2)
      openYokai()
  #Decide earnings and display
  os.system("cls")
  moneyEarnt = random.randint(5,networkLimit)
  text = colored("Data sold for £" + str(moneyEarnt), "green")
  write(text)
  text = colored("Press ENTER to return to the console.", "green")
  write(text)
  input("")
  os.system("cls")
  updateBalance(moneyEarnt)

#Buy stocks to earn (or lose) money
def buyStocks():
  os.system("cls")
  text = colored("Would you like to purchase a stock for £250? (Y/N)", "yellow")
  write(text)
  stockChoice = input("")
  if stockChoice.lower() == "y" and bankBalance > 249:
    returns = random.randint(1,500)
    difference = returns - 250
    #Display profit in green or red depending on profit + or -
    if difference > 0:
      text = colored("You earnt £{} from your stock. Profit: £{}".format(returns, difference), "green")
    else:
      text = colored("You earnt £{} from your stock. Profit: £{}".format(returns, difference), "red")
    write(text)
    text = colored("Press ENTER to return to Yokai.", "yellow")
    write(text)
    input("")
    os.system("cls")
    updateBalance(difference)
  elif stockChoice.lower() == "n":
    os.system("cls")
  #Check for sufficient funds.
  elif bankBalance < 250:
    text = colored("Insufficient Funds.", "yellow")
    write(text)
    time.sleep(1)
    buyStocks()
  else:
    text = colored("Invalid Input.", "yellow")
    time.sleep(1)
    write(text)
    buyStocks()
  openYokai()

#Check the current bank balance
def checkBalance():
  os.system("cls")
  text = colored("United Bank of Money.", "cyan")
  write(text)
  text = colored("Account Total: £{}".format(bankBalance), "cyan")
  write(text)
  text = colored("Press ENTER to return to Yokai.", "cyan")
  write(text)
  input("")
  os.system("cls")
  openYokai()

#Visit the Black Market to purchase upgrades or gamble
def visitMarket():
  os.system("cls")
  text = colored("Welcome to the Black Market.", "grey")
  write(text)
  text = colored("   1: Purchase a virtual scratchcard.\n   2: Upgrade Yokai\n   3: Return to Yokai.", "grey")
  write(text)
  marketChoice = input("")
  #Scratchcard
  if marketChoice == "1":
    text = colored("Purchase a virtual scratchcard for £5? (Y/N)", "grey")
    write(text)
    scratchChoice = input("")
    os.system("cls")
    if scratchChoice.lower() == "y":
      winnings = random.randint(0,10)
      text = colored("You won £{}".format(winnings), "grey")
      write(text)
      text = colored("Press ENTER to return to Yokai.", "grey")
      write(text)
      input("")
      profit = winnings - 5
      updateBalance(profit)
    elif scratchChoice.lower() == "n":
      visitMarket()
    else:
      text = colored("Invalid Input.", "grey")
      write(text)
      time.sleep(1)
      visitMarket()
  #Upgrade Yokai
  elif marketChoice == "2":
    text = colored("Upgrade Yokai for £1000? (Y/N)", "grey")
    write(text)
    upgradeChoice = input("")
    os.system("cls")
    if upgradeChoice.lower() == "y" and bankBalance > 999:
      upgradeYokai()
    elif upgradeChoice.lower() == "n":
      visitMarket()
    elif bankBalance < 1000:
      text = colored("Insufficient Funds.", "grey")
      write(text)
      time.sleep(1)
      visitMarket()
    
    else:
      text = colored("Invalid Input.", "grey")
      write(text)
      time.sleep(1)
      visitMarket()
  #Quit
  elif marketChoice == "3":
    openYokai()
  else:
    text = colored("Invalid Input.", "grey")
    write(text)
    time.sleep(1)
    visitMarket()

#Work and complete tasks
def work():
  os.system("cls")
  for i in range(1,10):
    colour = random.choice(colours)
    text = colored("Complete the task or type 'quit' to leave work.\nRepeat the colour '{}'. ({}/10)".format(colour, i), colour)
    print(text)
    answer = input("")
    os.system("cls")
    if answer.lower() == colour:
      text = colored("Correct!", "green")
      write(text)
    elif answer.lower() == "quit":
      text = colored("Qutting work...", colour)
      write(text)
      time.sleep(1)
      os.system("cls")
      openYokai()
    else:
      text = colored("Incorrect! Restarting...", "red")
      write(text)
      time.sleep(1)
      work()
    
  text = colored("Good job! Earnt £70!", "magenta")
  write(text)
  text = colored("Press ENTER to return to Yokai.", "magenta")
  write(text)
  input("")
  os.system("cls")
  updateSuspicion(-1)
  updateBalance(70)
  
  
#Open Yokai application
def openYokai():
  text = colored("Enter '?' or 'help' to see commands.", "green")
  write(text)
  text = colored("<yokai.localhost>: ", "green")
  yokaiChoice = input(text)
  if yokaiChoice == "?" or yokaiChoice.lower() == "help":
    yokaiHelp()
  elif yokaiChoice.lower() == "a":
    accessNetwork()
  elif yokaiChoice.lower() == "b":
    buyStocks()
  elif yokaiChoice.lower() == "c":
    checkBalance()
  elif yokaiChoice.lower() == "v":
    visitMarket()
  elif yokaiChoice.lower() == "w":
    work()
  else:
    text = colored("Invalid Input.", "green")
    time.sleep(1)
    os.system("cls")
    openYokai()

#---------------------------------
#Main
#---------------------------------

colours = ["red", "blue" ,"yellow", "green", "magenta", "cyan", "grey"]
networkLimit = 250
bankBalance = 0
suspicion = 0

#Display Title Screen
title = colored("      :::    :::     :::      ::::::::  :::    ::: :::::::::: ::::::::: \n     :+:    :+:   :+: :+:   :+:    :+: :+:   :+:  :+:        :+:    :+: \n    +:+    +:+  +:+   +:+  +:+        +:+  +:+   +:+        +:+    +:+  \n   +#++:++#++ +#++:++#++: +#+        +#++:++    +#++:++#   +#++:++#:    \n  +#+    +#+ +#+     +#+ +#+        +#+  +#+   +#+        +#+    +#+     \n #+#    #+# #+#     #+# #+#    #+# #+#   #+#  #+#        #+#    #+#     \n###    ### ###     ###  ########  ###    ### ########## ###    ###      ", "green")
print(title)
write("\nA text-based game created by Ezra.")
text = colored("Press ENTER to start the game.", "green")
write(text)
input("")
os.system("cls")

#Introduction
text = colored("Hello Hacker,\nA little birdie told me you need an easier way to get into a target's device.\nI have a solution for you; our new software.\nI have attached a copy of our new program, Yokai, to this email.\nFeel free to download it and use it however you wish.", "grey")
write(text)
time.sleep(1)
text = colored("Just remember, I never told you about this.", "grey")
write(text)
text = colored("\n\nHappy Hunting,", "grey")
write(text)
text = colored("Oni", "red")
write(text)
time.sleep(1)
text = colored("\nPress ENTER to download Yokai.", "green")
input(text)
loading = 0
while loading < 20:
  os.system("cls")
  loading += 1
  spaces = 20 - loading
  text = colored("Installing...", "blue")
  print(text)
  text = colored("[{}{}]".format("=" * loading, " " * spaces), "blue")
  print(text)
  wait = random.randint(1,10) / 20
  time.sleep(wait)
print("Installed")
time.sleep(1)
text = colored("Press ENTER to open Yokai.", "green")
input(text)


os.system("cls")
openYokai()