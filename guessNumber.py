# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 19:49:43 2022

@author: Kadir
"""

import random

def guess(x):
    randomNumber = random.randint(1, x)
    guess = 0
    guessDegree = 0
    while guess != randomNumber:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        
        if guess < randomNumber:
            print("Your guess is lower than the Number")
            guessDegree += 1
        elif guess > randomNumber:
            print("Your guess is higher than the Number")
            guessDegree += 1
            
        elif guess == randomNumber:
            guessDegree += 1
            print(f"You guessed correctly Well done. You guess {guessDegree} times")
            break


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback= input(f'Is {guess} too high (H), too low (L) or correct (C) ??').lower()
        if feedback == 'h':
            high = guess - 1
        if feedback == 'l':
            low = guess + 1
            
    print(f'Yay the computer  guessed your number {guess} , correctly')
    
computer_guess(1000)