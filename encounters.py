#!/usr/bin/python3

import random
import sys
import yaml


shipFile = sys.argv[1]
 
ships = {
  'lab ship' : { 'type':'lab ship', 'hull' : 400, 'jump' : 2, 'cost' : 136374300 }
  }

# 2d6 home brew
locations = [
   "null", "null", # 0 and 1
   "Planet - Military", "Planet - Remote Location", "Planet - Rural", "Planet - City", "Starport",     # 2 to 6
   "Starport", "Lunar - City", "Lunar - Outpost", "Asteroid - Base", "Capital Ship", "Lunar - Military"  # 7 to 12
  ]

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

# pooled from outputs from donjon.bin.sh
femNames = [
  "Amber","Andann","Anis","Arah","Arel","Athen","Ather","Berle","Betty","Bianca","Caitlan","Carea","Cayla","Ceridwen","Chelsea",
  "Chrotha","Delphine","Dianie","Dory","Elan","Eloise","Elsa","Elsy","Erer","Eveyln","Fae","Freya","Geneva","Guinevere","Haley",
  "Heria","Inian","Jacquel","Jade","Jane","Jessa","Jetta","Jinny","Jovena","Kara","Karla","Kathlie","Kathly","Kathry","Kathy",
  "Kerilyn","Kona","Kylie","Lecia","Lindsy","Lizab","Loria","Luna","Lyne","Manda","Mara","Marthy","Melina","Micha","Mila",
  "Mildra","Minerva","Morgana","Natalya","Neith","Nyx","Pamy","Parker","Phera","Portia","Raven","Rayna","Regine","Renate","Rice",
  "Sabine","Sane","Sanie","Sara","Selene","Seren","Sheria","Sica","Sicia","Skye","Sydney","Tamma","Tamsin","Tessa","Thalia",
  "Tina","Tine","Tinie","Trinity","Ulla","Vely","Verona","Wyn","Xylona","Yvone","Zuri"
  ]

# pooled from outputs from donjon.bin.sh
mascNames = [
  "Ahren","Aidan","Alex","Amer","Andold","Andres","Anton","Aron","Arott","Avery","Avip","Bertev","Braymy","Britt","Brodric","Camden","Carter",
  "Chraige","Chroge","Cyan","Damien","Damy","Darius","Dave","Derrik","Dony","Earthur","Edwas","Elon","Ethan","Ezra","Finnegan","Fruce","Galen",
  "Glen","Gory","Hardy","Harrison","Hawk","Hery","Hewill","Holden","Hurey","Idris","Ivan","Jace","Jackenn","Jaeger","Jamy","Jareth","Jeffry",
  "Jesse","Johnio","Johny","Jordan","Jose","Juanio","Kenne","Keve","Kynon","Liamy","Maddox","Marten","Merlin","Minio","Mothua","Muelie","Paris",
  "Pascal","Preston","Quentin","Quill","Quinn","Raige","Rankeith","Raphael","Redy","Remy","Rickenn","Rion","Rise","Ristin","Roby","Roldy","Roy",
  "Shawny","Stine","Stophua","Taylor","Tery","Thaddeus","Thony","Tobias","Vance","Wagner","Waltoph","Wardy","Wayne","Wynston","Xander","Xavier","Xerxes",
  "Yavin","Yukon","Yves","Ziven"
  ]

# pooled from outputs from donjon.bin.sh
surnames = [
  "Albach","Alcantar","Alder","Alers","Andes","Arciams","Arciaz","Arkes","Artips","Avant","Avin","Avison","Bailee","Bakins","Bancroft",
  "Barick","Barrick","Basset","Belley","Belly","Bentzen","Bowdoin","Brosson","Buccheri","Butlee","Byrn","Caldera","Campbak","Campbenn","Carrick",
  "Carte","Carthen","Castiglione","Castillon","Clezal","Clipson","Colee","Coley","Colly","Cooker","Coopark","Cooper","Coopow","Corwin","Cotte",
  "Croyle","Davis","Dewitt","Dezal","Diseth","Dowe","Drayton","Edwant","Ewaz","Faulknen","Finels","Flanigan","Fleray","Forgrave","Foste",
  "Girbach","Greeders","Grippen","Hardson","Harre","Haught","Helsing","Hewett","Hezal","Hohstadt","Holbach","Hompson","Jacksanch","Jackson","Jamas",
  "Jamoor","Jamorg","Jann","Jenker","Johnsand","Johnsimm","Johnson","Jonand","Kehoe","Kelly","Kennet","Kerensky","Kiani","Kinton","Kniffin",
  "Laux","Lauxo","Lavanchy","Lavigne","Lera","Lexand","Macbeth","Madigan","Manand","Manez","Markell","Masell","McLaren","McRaven","Melchor",
  "Mika","Monson","Morgan","Morgonz","Morguez","Murphy","Nesheim","O'Heron","Patte","Pera","Pere","Perra","Pete","Pezal","Quintan",
  "Racine","Rackham","Raschke","Reedams","Reedav","Reenes","Reson","Rezal","Rice","Ricia","Rigarc","Riordan","Rocheford","Rogan","Rogonz",
  "Rookson","Rosek","Rosson","Russon","Ryant","Ryante","Ryen","Sanchy","Sarratt","Scoopez","Severt","Sharpey","Slayton","Smeson","Smilley",
  "Solari","Sonels","Sonez","Sonoda","Steiger","Steward","Stoyer","Strachan","Takach","Tameron","Tera","Terson","Tian","Tindal","Tinett",
  "Toten","Tower","Tronstad","Turnes","Tyrrell","Vangelos","Vanlith","Veillon","Vilchis","Voight","Volante","Warders","Wardsanch","Washy","Watson",
  "Wescott","Wethern","Wheson","Winslett","Wyrick","Yueh","Zahra","Zavaleta","Zemke"
  ]


def main(): 
  # your ship details
  with open(shipFile, 'r') as file:
    ship = yaml.safe_load(file)
  print('### YOUR SHIP')
  print(ship)

  # patron 
  patronRoll = int(diceRoll(1,len(patrons)) - 1)
  randomPatron = sorted(patrons)[patronRoll]
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
  randomMission = sorted(missions)[missionRoll]
  parsecs = diceRoll(1, 6)          # distance of 1d6 parsecs
  jumps = 2 * int((parsecs / ship['jump']) + (parsecs % ship['jump'] > 0))
  location = locations[diceRoll(2,6)]
  bonus = diceRoll(5, 6) * .01      # bonus percent on top, 5 to 30%
  print('\n### MISSION')
  print("Patron:",randomPatron,"-",surname, forename)
  print("Mission:",randomMission)
  print('Location:', location)
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
