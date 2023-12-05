#!/usr/bin/python3

import random

ships = {
  'lab ship' : { 'type':'lab ship', 'hull' : 400, 'jump' : 2, 'cost' : 136374300 }
  }

alliesEnemies = [ 
 "Naval Officer", "Imperial Diplomat ", "Crooked Trader ", "Medical Doctor", "Eccentric", "Scientist", "Mercenary", "Famous", "Performer", "Alien Thief"
 "Free Trader", "Explorer", "Marine Captain", "Corporate", "Executive", "Researcher", "Cultural Attaché ", "Religious Leader ", "Conspirator",
 "Rich Noble", "Artificial", "Intelligence", "Bored Noble", "Planetary Governor", "Inveterate Gambler", "Crusading Journalist", "Doomsday Cultist",
 "Corporate Agent", "Criminal Syndicate", "Military Governor", "Army Quartermaster", "Private Investigator", "Starport Administrator", "Retired Admiral",
 "Alien Ambassador", "Smuggler", "Weapons Inspector", "Elder Statesman", "Planetary Warlord", "Imperial Agent"
 ]

patrons = [
  "Assassin","Smuggler","Terrorist","Embezzler","Thief","Revolutionary","Clerk","Administrator","Mayor","Minor Noble","Physician","Tribal Leader",
  "Diplomat","Courier","Spy","Ambassador","Noble","Police Officer","Merchant","Free Trader","Broker","Corporate Executive","Corporate Agent","Financier",
  "Belter","Researcher","Naval Officer","Pilot","Starport Administrator","Scout","Alien","Playboy","Stowaway","Family Relative","Agent of a Foreign","Power",
  "Imperial Agent"
]

missions = [
  "Assassinate a target", "Frame a target", "Destroy a target", "Steal from a target", "Aid in a burglary", "Stop a burglary", 
  "Retrieve data or an object from a secure facility", "Discredit a target", "Find a lost cargo", "Find a lost person", "Deceive a target", 
  "Sabotage a target", "Transport goods", "Transport a person", "Transport data", "Transport goods secretly", "Transport goods quickly", 
  "Transport dangerous goods", "Investigate a crime", "Investigate a theft", "Investigate a murder", "Investigate a mystery", "Investigate a target", 
  "Investigate an event", "Join an expedition", "Survey a planet", "Explore a new system", "Explore a ruin", "Salvage a ship", "Capture a creature", 
  "Hijack a ship", "Entertain a noble", "Protect a target", "Save a target", "Aid a target", "It is a trap – the Patron intends to betray the Traveller" 
  ]

starportEncounters = [
  "Maintenance robot at work", "Trade ship arrives or departs", "Captain argues about fuel prices",
  "News report about pirate activity on a starport screen draws a crowd", "Bored clerk makes life difficult for the Travellers", 
  "Local merchant with cargo to transport seeks a ship", "Dissident tries to claim sanctuary from planetaryauthorities",
  "Traders from offworld argue with local brokers", "Technician repairing starport computer system", "Reporter asks for news from offworld",
  "Bizarre cultural performance", "Patron argues with another group of Travellers", "Military vessel arrives or departs", "Demonstration outside starport",
  "Escaped prisoners begs for passage offworld", "Impromptu bazaar of bizarre items", "Security patrol", "Unusual alien", 
  "Traders offer spare parts and supplies at cut-price rates", "Repair yard catches fire", "Passenger liner arrives or departs",
  "Servant robot offers to guide Travellers aroundthe spaceport", "Trader from a distant system selling strange curios",
  "Old crippled belter asks for spare change andcomplains about drones taking their job", "Patron offers the Travellers a job", "Passenger looking for a ship",
  "Religious pilgrims try to convert the Travellers", "Cargo hauler arrives or departs", "Scout ship arrives or departs", 
  "Illegal or dangerous goods are impounded", "Pickpocket tries to steal from the Travellers", "Drunken crew pick a fight",
  "Government officials investigate the characters", "Random security sweep scans Travellers and their baggage", 
  "Starport is temporarily shut down for security reasons", "Damaged ship makes emergency docking"
  ]

urbanEncounters = [
  "Street riot in progress", "Travellers pass a charming restaurant", "Trader in illegal goods", "Public argument", "Sudden change of weather",
  "Travellers are asked for help", "Travellers pass a bar or pub", "Travellers pass a theatre or other entertainment venue ", "Curiosity Shop",
  "Street market stall tries to sell the Travellers something", "Fire, dome breach or other emergency in progress", "Attempted robbery of Travellers",
  "Vehicle accident involving the Travellers", "Low-flying spacecraft flies overhead", "Alien or other offworlder", "Random character bumps into a Traveller",
  "Pickpocket", "Media team or journalist", "Security Patrol", "Ancient building or archive", "Festival", "Someone is following the characters", 
  "Unusual cultural group or event", "Planetary official", "Travellers spot someone they recognise", "Public demonstration", 
  "Robot or other servant passes Travellers", "Prospective patron", "Crime such as robbery or attack in progress", "Street preacher rants at the Travellers",
  "News broadcast on public screens", "Sudden curfew or other restriction on", "movement", "Unusually empty or quiet street", "Public announcement",
  "Sports event", "Imperial Dignitary"
  ]

def main(): 
  # your ship details
  ship = ships['lab ship']
  print('### YOUR SHIP')
  print(ship)
  # mission
  patronRoll = int(diceRoll(1,len(patrons)) - 1)
  randomPatron = sorted(patrons)[patronRoll]
  missionRoll = int(diceRoll(1,len(missions)) - 1)
  randomMission = sorted(missions)[missionRoll]
  parsecs = diceRoll(1, 6)          # distance of 1d6 parsecs
  bonus = diceRoll(5, 6) * .01      # bonus percent on top, 5 to 30%
  jumps = 2 * int((parsecs / ship['jump']) + (parsecs % ship['jump'] > 0))
  print('\n### MISSION')
  print("Patron:",randomPatron)
  print("Mission:",randomMission)
  print('Distance:',parsecs,'parsecs away')
  print('Jumps:',jumps)
  operatingCosts(ship, parsecs, jumps, bonus)

def diceRoll(dieCount,dieSides):
  dieTotal = 0
  for i in range(0,dieCount):
    min = 1
    max = dieSides
    dieVal = random.randint(min,max)
    dieTotal += dieVal
  return(dieTotal)

def operatingCosts(ship, parsecs, jumps, bonus):
  print('\n### INCOME EXPENSES REVENUE')
  mortgage = ship['cost'] / 240   
  weeklyMaintenance = (ship['cost'] * .001) / 48   
  # fuel is 10% of hull per parsec
  fuelUsage = (ship['hull'] * .1 ) * (parsecs * 2)
  fuelExpense = int(fuelUsage * 500)
  # each jump takes 1 week
  mortgageExpense = int(mortgage / 4 * jumps)
  maintenanceExpense = int(weeklyMaintenance * jumps)
  expenses = mortgageExpense + maintenanceExpense + fuelExpense
  bonus = int(expenses *  bonus)
  income = bonus + expenses 
  # output
  formattedIncome = "{:,}".format(income)
  print('Income: Cr',formattedIncome)
  print('Expected Expense:',expenses)
  print('...mortage:', mortgageExpense) 
  print('...maintenance:', maintenanceExpense) 
  print('...fuel:', fuelExpense) 
  print('Revenue: ',bonus)

main()
