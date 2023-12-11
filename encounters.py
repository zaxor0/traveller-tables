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
world = sys.argv[2]
 
def main(): 
  # your ship details
  with open(shipFile, 'r') as file:
    ship = yaml.safe_load(file)

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
    targetSystem = random.choice(planetsArray)
    for worldDetails in nearbyWorlds['Worlds']:
      if worldDetails['Name'] == targetSystem:
        targetSystemDetails = worldDetails
  else:
    targetSystem = world

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
  acceleration = ship['thrust'] * 10

  days = diceRoll(2,4) # additional days to complete on top of jumps
  earlyBonus = int(diceRoll(1,6) * 1000) # bonus for each day completed early

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

  jumps = 2 * int((parsecs / ship['jump']) + (parsecs % ship['jump'] > 0))
  bonusDice = 4 + jumps
  bonus = diceRoll(bonusDice, 6) * .01      

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
    travelTime = int((jumps * 7))
    daysToComplete = int((jumps * 7) + days)

  # threat multiplier
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

  distance = "{:,}".format(distance)
  # output to screen
  print('### MISSION')
  worldPosterLink = str('[Source World: '+ world +'](' + worldPoster(world) + ')')
  jumpMapLink = str('[Jump Map](' + jumpMap(world) + ')')
  print(worldPosterLink, jumpMapLink)
  print("Patron:", patron,"-",surname, forename)
  print("Mission:",mission)
  print('Threat level:',threat)
  print("Target:",target)
  print("Opposition:",opposition)
  print('Location:', location)
  print('### TRAVEL')
  if jumps > 0:
    targetWorldLink = str('['+ targetSystem +'](' + worldPoster(targetSystem) + ')')
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
  operatingCosts(ship, parsecs, jumps, bonus, daysToComplete)

def diceRoll(dieCount,dieSides):
  dieTotal = 0
  for i in range(0,dieCount):
    min = 1
    max = dieSides
    dieVal = random.randint(min,max)
    dieTotal += dieVal
  return(dieTotal)

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

main()
