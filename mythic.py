#!/usr/bin/python3

import os
import random

# variables

fateChart = {
  'certain' : {
    1 : {10,50,91}, 2 : {13,65,94}, 3 : {15,75,96}, 4 : {17,85,98}, 5 : {18,90,99}, 6 : {19,95,100}, 7 : {20,99,'X'}, 8 : {20,99,'X'}, 9 : {20,99,'X'} },
  'nearly certain' : {
    1 : {7,35,88}, 2 : {10,50,91}, 3 : {13,65,94}, 4 : {15,75,96}, 5 : {17,85,98}, 6 : {18,90,99}, 7 : {19,95,100}, 8 : {20,99,'X'}, 9 : {20,99,'X'}},
  'very likely' : {
    1 : { 5,25,86}, 2 : {7,35,88}, 3 : {10,50,91}, 4 : {13,65,94}, 5 : {15,75,96}, 6 : {17,85,98}, 7 : {18,90,99}, 8 : {19,95,100}, 9 : {20,99,'X'}},
  'likely' : {
    1 : { 3,15,84}, 2 : {5,25,86}, 3 : {7,35,88}, 4 : {10,50,91}, 5 : {13,65,94}, 6 : {15,75,96}, 7 : {17,85,98}, 8 : {18,90,99}, 9 : {19,95,100}},
  '50/50' : {
    1 : { 2,10,83}, 2 : {3,15,84}, 3 : {5,25,86}, 4 : {7,35,88}, 5 : {10,50,91}, 6 : {13,65,94}, 7 : {15,75,96}, 8 : {17,85,98}, 9 : {18,90,99}},
  'unlikely' : {
    1 : { 1,5,82}, 2 : {2,10,83}, 3 : {3,15,84}, 4 : {5,25,86}, 5 : {7,35,88}, 6 : {10,50,91}, 7 : {13,65,94}, 8 : {15,75,96}, 9 : {17,85,98}},
  'very unlikely' : {
    1 : { 'X',1,81}, 2 : {1,5,82}, 3 : {2,10,83}, 4 : {3,15,84}, 5 : {5,25,86}, 6 : {7,35,88}, 7 : {10,50,91}, 8 : {13,65,94}, 9 : {15,75,96}},
  'nearly impossible' : {
    1 : { 'X',1,81}, 2 : {'X',1,81}, 3 : {1,5,82}, 4 : {2,10,83}, 5 : {3,15,84}, 6 : {5,25,86}, 7 : {7,35,88}, 8 : {10,50,91}, 9 : {13,65,94}},
  'impossible' : {
    1 : { 'X',1,81}, 2 : {'X',1,81}, 3 : {'X',1,81}, 4 : {1,5,82}, 5 : {2,10,83}, 6 : {3,15,84}, 7 : {5,25,86}, 8 : {7,35,88}, 9 : {10,50,91}}
  }

sceneAdjustmentTable = {
  1 : 'Remove a character', 2 : 'Add a character', 3 : 'Reduce/remove an activity', 4 : 'Increase an activity', 
  5 : 'Remove an object', 6 : 'Add an object', 7 : 'Make 2 adjustments' 
  }

yesses = ['Yes','yes','Y','y','Ye','ye','ya','Ya','Yup','yup']
nos    = ['No','no','N','n','Nope','nope','Nah','nah']


clear = lambda: os.system('clear')

def main():
  clear()
  print("welcome to mythic")
  begin = False
  while begin == False:
    print("the starting chaos factor is always 5")
    startScene = str(input("Are you ready to start the first scene?\n> "))
    if startScene in yesses:
      begin = True
    else:
      being = False
      
  chaosFactor=5
  while True:
    clear()
    # first test the expected scene, page 63
    print('\n### NEW SCENE ###')
    print('\nNow we need to test the scene against our expectations with a d10 versus the Chaos Factor,',str(chaosFactor))
    sceneRoll = diceRoll(1,10)
    # if equal to or lower than the chaos factor, modify the scene
    if sceneRoll <= chaosFactor:
      print("Rolled less than or equal to the Chaos Factor")
      # if odd, alter the scene
      if sceneRoll % 2 != 0:
        print('\nRolled,',str(sceneRoll),'! Odd -- The scene is Altered!') 
        print('This mean the scene occurs in the next most expected way, make just a tweak to it or you can ask a fate question')
        adjustmentRoll = diceRoll(1,10)
        print('....Rolling adjustments...',str(adjustmentRoll))
        adjustmentString = ''
        # keep the odds of the d10, but if the roll is 7 or higher randomly add 2 adjustments using a d6
        if adjustmentRoll >= 7:
          adjustments = [diceRoll(1,6), diceRoll(1,6)]
          for adjustNumRolled in adjustments:
            adjustmentString = adjustmentString + sceneAdjustmentTable[adjustNumRolled] + ' and ' 
        else:
          adjustmentString = sceneAdjustmentTable[adjustmentRoll]
        print('adjust scene by:',adjustmentString,'\n')
        testing = input("Enter any key to continue\n> ")
          
      # if even, alter interrupt the scene
      if sceneRoll % 2 == 0:
        print("Event! Interrupt the Scene!") 
        testing = input("Enter any key to continue\n> ")
    else:
      print("Rolled greater than the Chaos Factor", str(chaosFactor))
      print("Play out the scene until there is a question.")
      sceneActive = True
      while sceneActive == True:
        question = str(input("\nWhile in the scene, if you have a question enter 'yes' OR if the scene ends enter 'no'\n> "))
        clear()
        print('\n ### \n')
        if question in yesses:
          sceneActive = True
          fateLikeSelect = False
          while fateLikeSelect == False:
            print("Ask a yes or no question. Then follow your expectations, what is the likelihood of a yes?")
            number = 1
            for likeliness in fateChart:
              print(str(number),likeliness)
              number += 1
            playerLikely = int(input("Which likeliness will you select?\n> "))
            if playerLikely > 0 and playerLikely < 10:
              selection = 1 
              for likeliness in fateChart:
                if selection == playerLikely:
                  likelihood = likeliness
                selection += 1
              fateLikeSelect = True
              percentages = sorted(fateChart[likelihood][chaosFactor])
              exceptionalYes = percentages[0]
              yesAnswer = percentages[1]
              exceptionalNo = percentages[2]
            else:
              print("not a valid selection, select a number between 1 and 9")
              fateLikeSelect = False
          fateRoll = diceRoll(1,100)
#          print('You have selected',likelihood,'which has 3 numbers determined by the chaos factor, which is',chaosFactor)
#          print('\n    Execptional Yes     1 to',str(exceptionalYes))
#          print('        Yes           ',str(exceptionalYes + 1),'to',yesAnswer)
#          print('        No            ',str(yesAnswer + 1),'to',str(exceptionalNo - 1))
#          print('    Execptional No    ',exceptionalNo,'to 100')
#          input('\n Press any key to ROLL!')
#          print("\nRolling...", str(fateRoll))
          if fateRoll <= exceptionalYes:
            fateAnswer = 'exceptional YES!'
          if fateRoll > exceptionalYes and fateRoll <= yesAnswer:
            fateAnswer = 'YES!'
          if fateRoll > yesAnswer and fateRoll < exceptionalNo:
            fateAnswer = 'NO!'
          if fateRoll >= exceptionalNo:
            fateAnswer = 'exceptional NO!'
          print('the fates say ...',fateAnswer,'... rolled',fateRoll,' on [',exceptionalYes,'|',yesAnswer,'|',exceptionalNo,']')
        else:
          sceneActive= False  
          chaosUpdated = False
          while chaosUpdated == False:
            chaosEnsued = input("Were the players mostly in control of the scene? Yes or no\n> ")
            if chaosEnsued in yesses:
              chaosFactor -= 1
              chaosUpdated= True
            elif chaosEnsued in nos:
              chaosFactor += 1
              chaosUpdated= True
            else:
              chaosUpdated = False
          print('chaos factor has been changed to', str(chaosFactor))

def diceRoll(dieCount,dieSides):
  dieTotal = 0
  for i in range(0,dieCount):
    min = 1
    max = dieSides
    dieVal = random.randint(min,max)
    dieTotal += dieVal
  return(dieTotal)




main()
