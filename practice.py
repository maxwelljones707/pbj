#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 20:03:24 2020

@author: benjaminfeciura
"""

##### initialize #####

bread = False
peanutButter = False
jelly = False
success = False
completed = False
chosenStep = 0
calories = 350 

##### functions #####

def printSteps():
    
    print('\n\nRemaining Sandwich Tasks:\n')
    
    # only show option if bread is not yet placed
    if not bread:
        print('[0] : Place Bread')
        
    # only show option if pb is not spread
    if not peanutButter:
        print('[1] : Spread Peanut Butter')
        
    # only show option if jelly is not spread
    if not jelly:
        print('[2] : Spread Jelly')
        
    print('[3] : Join Bread\n')

def validate(chosenStep):
    global bread
    global peanutButter
    global jelly
        
    # check if the user input is an integer... if not, invalid
    try:
        stepNumber = int(chosenStep)
    except ValueError:
        return False
    
    # check if the user input is one of the options
    if not stepNumber in range(0,4):
        return False
        
    # check if the user picked a task that's already completed
    if stepNumber == 0:
        if bread:
            return False
    if stepNumber == 1:
        if peanutButter:
            return False
    if stepNumber == 2:
        if jelly:
            return False   
    
    # otherwise, the user picked a valid option
    return True
    
def doStep(chosenStep):
    global completed
    global success
    global bread
    global peanutButter
    global jelly

    # check if the user input is valid
    valid = validate(chosenStep)
    
    # if not valid, notify and return to options
    if not valid:
        print('Invalid Selection.\n')
        return
     
    # if valid, take integer and check which step the user chose...
    stepNumber = int(chosenStep)
    
    # chose 0: bread
    # as long as the user picks this first, continue
    if stepNumber == 0:
        print('\nYou have placed the bread.')
        bread = True
        return
    
    # chose 1: peanut butter
    if stepNumber == 1:
        
        # sandwich fails if chosen before 0
        if not bread:
            print('\nYou spread peanut butter on the work surface.')
            completed = True # end the loop
            return
        
        # otherwise, continue
        print('\nYou spread peanut butter on the bread!')
        peanutButter = True #flag so the option doesn't appear again
        return
    
    # chose 2: jelly
    if stepNumber == 2:
        
        # sandwich fails if chosen before 0
        if not bread:
            print('\nYou spread jelly on the work surface.')
            completed = True # end the loop
            return
        
        # otherwise, continue
        print('\nYou spread jelly on the bread!')
        jelly = True # flag so the option doesn't appear again
        return
    
    # chose 3: join bread
    if stepNumber == 3:
        
        # sandwich fails if chosen before 0
        if not bread:
            print('\nYou did not place any bread yet.')
            completed = True # end the loop
            return
        
        #sandwich fails if chosen before both 1 and 2 selected
        if not (peanutButter or jelly):
            print('\nYou made a bread sandwich.')
            completed = True # end the loop
            return
        if not peanutButter:
            print('\nYou made a jelly sandwich.')
            completed = True # end the loop
            return
        if not jelly:
            print('\nYou made a peanut butter sandwich.')
            completed = True # end the loop
            return
        
        # otherwise, sandwich is completed successfully
        print('\nYou made a peanut butter and jelly sandwich. Congratulations!')
        completed = True # end the loop
        success = True # don't show the error message
        return
      
##### main #####
        
# welcome user
print('\nWelcome to Sandwich Practice!\n')
print('This application can assist in practicing sandwiches.')
input('Press any key to begin sandwich.')

# sandwich tasks:
# 0: place bread
# 1: spread peanut butter on bread
# 2: spread jelly on bread
# 3: join bread

# run until all sandwich completed or an error is made
while not completed:
    printSteps()
    chosenStep = input("Please select a sandwich step: ")
    doStep(chosenStep)
    
# if the loop exited on an error, display failure message
if not success:
    print('Sandwich incomplete. Please try again!\n')
    
##### end #####
