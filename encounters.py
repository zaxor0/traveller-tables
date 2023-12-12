#!/usr/bin/python3

from tables import *
from possibleWorlds import *

import datetime
import math
import random
import sys
import yaml

## mgt2e refers to mongoose traveller second edition 2022 update
## SWN refers to Stars Without Number free edition, which contains tons of useful tables

shipFile = sys.argv[1]
worldName = sys.argv[2]
 
def main(): 
  # your ship details
  with open(shipFile, 'r') as file:
    ship = yaml.safe_load(file)
  world = worldSearch(worldName)
  world = worldDetailed(world)
  for i in range(1,2):
    patron = rollPatron()
    mission, target, opposition, parsecs, targetSystem = rollMission(world)
    location, relevantPlanet = rollLocation()
    distance = determineDistance(parsecs, relevantPlanet)
    jumps = 2 * int((parsecs / ship['jump']) + (parsecs % ship['jump'] > 0))
    days = diceRoll(2,4) 
    travelTime, daysToComplete, thrustDays, thrustHoursRemainder = thrustCalculation(ship, parsecs, distance, jumps, days)
    bonusDice = 4 + jumps
    bonus = diceRoll(bonusDice, 6) * .01 
    bonus, threat = threatMultiplier(location, opposition, target, mission, bonus)

    # exceptions
    if mission == "Explore a new system" and parsecs == 0:
      target = "New system"
      parsecs = parsecsAway[diceRoll(2, 6)]
    elif "It is a trap" in mission:
      missionRoll = int(diceRoll(1,len(missions)) - 1)
      mission = sorted(missions)[missionRoll]
      mission = mission + "*"
    elif mission == "Salvage a ship":
      location == "near gas giant"
    elif "Planetary" in target:
      location = locations[diceRoll(1,4) + 2]
    elif location == "Orbital Station":
      distanceRoll = int(diceRoll(1,len(distances)) - 1)
      orbiting = sorted(distances)[distanceRoll]
      location = location + " - " + orbiting
    else:
      False
  
    printMission(distance, world, patron, mission, threat, target, opposition, location)
    printTravel(jumps, targetSystem, parsecs, daysToComplete, travelTime, distance, thrustDays, thrustHoursRemainder, ship)
    operatingCosts(ship, parsecs, jumps, bonus, daysToComplete)

def rollPatron():
  # patron 
  patronRoll = int(diceRoll(1,len(patrons)) - 1)
  patron = sorted(patrons)[patronRoll]
  if diceRoll(1,2) == 2: 
    forelist = mascNames
  else: 
    forelist = femNames
  forenameRoll = int(diceRoll(1,len(forelist)) - 1)
  forename = sorted(forelist)[forenameRoll]
  surnameRoll = int(diceRoll(1,len(surnames)) - 1)
  surname = sorted(surnames)[surnameRoll]
  patron = str(patron + " - " + surname + " " + forename)
  return patron

def rollMission(world):
  # mission
  missionRoll = int(diceRoll(1,len(missions)) - 1)
  mission = sorted(missions)[missionRoll]
  targetRoll = int(diceRoll(1,len(targets)) - 1)
  target = sorted(targets)[targetRoll]
  oppositionRoll = int(diceRoll(1,len(oppositions)) - 1)
  opposition = sorted(oppositions)[oppositionRoll]
  parsecs = parsecsAway[diceRoll(2, 6)]
  if parsecs > 0:
    planetsArray, nearbyWorlds = nearbyPlanets(world, parsecs)
    targetSystemName = random.choice(planetsArray)
    for worldDetails in nearbyWorlds['Worlds']:
      if worldDetails['Name'] == targetSystemName:
        targetSystem = worldDetails
  else:
    targetSystem = world

  return mission, target, opposition, parsecs, targetSystem 

def rollLocation():
  # location in system
  location = locations[diceRoll(2,6)]
  relevantPlanet = planets[diceRoll(2,6)]
  # planet and moon location
  if "Planet" in location:
    relevantPlanet = random.choice(['primary world','close neighbor world','far neighbor world'])
    location = location + " - " + relevantPlanet
  if "Lunar" in location:
    location = relevantPlanet + "'s " + location
  # random point of interest in a system
  if location == "Starport":
    relevantPlanet = "primary world"
    location = location + " orbiting " + relevantPlanet
  if location == "Capital Ship":
    location = location + " orbiting " + relevantPlanet
  if location == "System POI":
    location = sorted(systemPOI)[diceRoll(1,8) - 1] 
    if "Gas gaint" in location:
      relevantPlanet = random.choice(["close gas gaint","far gas giant"])
    location = location + " (SWN pg. 171)"
  return location, relevantPlanet

def determineDistance(parsecs,relevantPlanet):
  # if same system calc distance from primary world
  if parsecs == 0: 
    standardDistance = distances[relevantPlanet]
  # if different system, calc distance from system's star
  elif relevantPlanet == "primary world":
    standardDistance = distances[relevantPlanet]
  # distances per pg 163 of mgt2e are from the perspective of the primary world, so we need to add in its distance from the star
  else:
    standardDistance = distances[relevantPlanet] + distances["primary world"]
  # modulate the distance from 80 to 120% of standard distance
  distance = int(standardDistance * (.8 + (random.randint(0,40) / 100)))
  return distance 

def thrustCalculation(ship, parsecs, distance, jumps, days):
  acceleration = ship['thrust'] * 10
  # if travelling in the same system, calculate time in "thrust" between planets 
  if parsecs == 0:
    thrustSeconds = int(2 * math.sqrt((distance * 1000) / acceleration))
    thrustHours = int(thrustSeconds / 3600)
    thrustDays = int(thrustHours / 24)
    thrustHoursRemainder = int(thrustHours % 24)
    thrustDaysFormatted = str(datetime.timedelta(seconds=thrustSeconds))
    thrustRTT = int((2 * thrustSeconds) / 86400)
    travelTime = thrustRTT
    daysToComplete = days + thrustRTT
  else:
    thrustDays = 0
    thrustHoursRemainder = 0
    travelTime = int((jumps * 7))
    daysToComplete = int((jumps * 7) + days)
  return travelTime, daysToComplete, thrustDays, thrustHoursRemainder

def threatMultiplier(location, opposition, target, mission, bonus):
  threat = 0
  if 'Military' in location:
    threat += 1
  if ('angerous' or 'Hostile' or 'restricted' or 'protected' or 'Police') in opposition:
    threat += 1
  if 'Illegal' in target:
    threat += 1
  if ('dangerous' or 'Assassinate' or 'Steal' or 'Aid in burglary' or 'Sabotage' or 'Hijack') in mission:
    threat += 1
  if threat > 0:
    bonus = bonus * (diceRoll(1,4) + threat)
  return bonus, threat

def printMission(distance, world, patron, mission, threat, target, opposition, location):
  distance = "{:,}".format(distance)
  # output to screen
  print('### MISSION')
  worldPosterLink = str('Source World: ['+ world['WorldName'] +'](' + worldPoster(world) + ')')
  jumpMapLink = str('[Jump Map](' + jumpMap(world) + ')')
  print(worldPosterLink,'  -  ', jumpMapLink)
  print("Patron:", patron)
  print("Mission:",mission)
  print('Threat level:',threat)
  print("Target:",target)
  print("Opposition:",opposition)
  print('Location:', location)

def printTravel(jumps, targetSystem, parsecs, daysToComplete, travelTime, distance, thrustDays, thrustHoursRemainder, ship):
  print('### TRAVEL')
  if jumps > 0:
    targetWorldLink = str('['+ targetSystem['Name'] +'](' + worldPoster(targetSystem) + ')')
    print('Target located in:',targetWorldLink)
    print('Distance:',parsecs,'parsecs')
    print('Total Jumps:',jumps,"(round trip)")
    print("Days to complete:", daysToComplete)
    print("Days in travel:",travelTime) 
  else:
    print('Total Jumps: 0')
    print('Distance in system:',distance,'km')
    print('Time in thrust:',thrustDays,'Days',thrustHoursRemainder,'Hours at thrust',ship['thrust'])
    print("Days to complete:", daysToComplete)
    print("Days in travel:",travelTime) 

def operatingCosts(ship, parsecs, jumps, bonus, days):
  print('### INCOME EXPENSES REVENUE')
  if parsecs > 0:
    mortgage = ship['cost'] / 240   
    weeklyMaintenance = (ship['cost'] * .001) / 48   
    # fuel is 10% of hull per parsec
    fuelUsage = (ship['hull'] * .1 ) * (parsecs * 2)
    fuelExpense = int(fuelUsage * 500)
    # each jump takes 1 week
    mortgageExpense = int(mortgage / 4 * jumps)
    maintenanceExpense = int(weeklyMaintenance * jumps)
    # crew salary
    salaryExpense = 0
    for crew in ship['crew']:
      crewSalary = int(salaries[crew] / 4) * jumps
      salaryExpense += crewSalary
    # total
    expenses = mortgageExpense + maintenanceExpense + fuelExpense + salaryExpense
    bonus = int(expenses *  bonus)
    income = bonus + expenses 
    # output
    print('Income: Cr', str("{:,}".format(income)))
    print('Expected Expense:', str("{:,}".format(expenses)))
    print('...crew salary: Cr', str("{:,}".format(salaryExpense)))
    print('...mortage: Cr', str("{:,}".format(mortgageExpense)))
    print('...maintenance: Cr', str("{:,}".format(maintenanceExpense)))
    print('...fuel: Cr', str("{:,}".format(fuelExpense)))
    print('Revenue: Cr ',str("{:,}".format(bonus)))
  else:
    # crew salary
    salaryExpense = 0
    for crew in ship['crew']:
      crewSalary = int(salaries[crew] / 28) * days 
      salaryExpense += crewSalary
    expenses = salaryExpense 
    bonus = int(diceRoll(4,6) * 1000)
    income = bonus + expenses 
    # output
    print('Income: Cr', str("{:,}".format(income)))
    print('Expected Expense:', str("{:,}".format(expenses)))
    print('Revenue: Cr ',str("{:,}".format(bonus)))

def diceRoll(dieCount,dieSides):
  dieTotal = 0
  for i in range(0,dieCount):
    min = 1
    max = dieSides
    dieVal = random.randint(min,max)
    dieTotal += dieVal
  return(dieTotal)

main()
