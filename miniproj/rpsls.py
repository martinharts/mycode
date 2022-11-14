#!/usr/bin/env python3

#Rock, Paper, Scissors, Lizard, Spock

#Game rules: As Sheldon says in the Big Bang Theory scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock, and as it always has, rock crushes scissors

import random

while True:

    your_item = input("Choose your weapon (rock, paper, scissors, lizard, spock): ").lower()

    weapon = ["rock", "paper", "scissors", "lizard", "spock"]

#Random weapon for opponent
    opponent = random.choice(weapon)

#Let the match begin

    if your_item not in weapon:
        print("Please choose either rock, paper, scissors, lizard, or spock\n")
        continue

    print(f"\nYou chose {your_item}, opponent chose {opponent}.\n")

    if your_item == opponent:
        print("Stalemate. You both live another day!")
    elif your_item == 'rock':
        if opponent == 'paper':
            print("A piece of paper covered you, YOU LOSE!")
        elif opponent == 'scissors':
            print("You Broke their scissors! YOU WIN!")
        elif opponent == 'lizard':
            print("You squished the lizard! YOU WIN!")
        elif opponent == "spock":
            print("You've been vaporized! YOU LOSE!")        
    elif your_item == 'paper':
        if opponent == 'scissors':
            print("I heard a slice, YOU LOSE!")
        elif opponent == 'rock':
            print("You covered their rock! YOU WIN!")
        elif opponent == 'lizard':
            print("You got eaten by the lizard! YOU LOSE!")
        elif opponent == "spock":
            print("You've disproved spock! HAH! YOU WIN!") 
    elif your_item == 'scissors':
        if opponent == 'rock':
            print("You've been crushed! YOU LOSE!")
        elif opponent == 'paper':
            print("I heard a slice, YOU WIN!")
        elif opponent == 'lizard':
            print("You cut the head off the beast! YOU WIN!")
        elif opponent == "spock":
            print("You're scissors were smashed by spock! YOU LOSE!") 
    elif your_item == 'lizard':
        if opponent == 'spock':
            print("You've poisened Spock! YOU WIN!")
        elif opponent == 'paper':
            print("You swallowed the paper, YOU WIN!")
        elif opponent == 'rock':
            print("You've been squished! YOU LOSE!")
        elif opponent == "scissors":
            print("You're head got cut off! YOU LOSE!") 
    elif your_item == "spock":
        if opponent == "rock":
            print("Hasta La vista, rock!")
        elif opponent == 'paper':
            print("You've been disproven, YOU LOSE!")
        elif opponent == 'lizard':
            print("You've been poisened! YOU LOSE!")
        elif opponent == "scissors":
            print("You smashed the scissors! YOU WIN!") 

    one_more_round = input("Challenge another opponent? (y/n): ").lower()
    if one_more_round.lower() != "y":
        break
