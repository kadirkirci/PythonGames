# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 20:24:29 2022

@author: Kadir
"""

import random

def play():
    user = input("What's your choice 'r' for rock , 'p' for paper , 's' for scissors: ")
    computer = random.choice(['r','p','s'])
    
    if user == computer:
        return 'tie'
    if is_win(user, computer):
        return 'win'
    
    return 'You lost'

def is_win(player, opponent):
    # return true if player wins
    # r>s s>p p>r
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True
    
print(play())