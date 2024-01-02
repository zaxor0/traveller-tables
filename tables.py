#!/usr/sbin/python3

# all tables in this file
tableList= [
  'ships',
  'starportQuality',
  'locations',
  'systemPOI',
  'parsecsAway',
  'distances',
  'planets',
  'alliesEnemies',
  'characterQuirks',
  'patrons',
  'missions',
  'targets',
  'oppositions',
  'starportEncounters',
  'urbanEncounters',
  'salaries',
  'femNames',
  'mascNames',
  'surnames'
  ]


# sample for mgt2e core rules
ships = {
  'lab ship' : { 'type':'lab ship', 'hull' : 400, 'jump' : 2, 'cost' : 136374300 }
  }

# from mgt2e core rules pg 257
starportQuality = {
 'A' : { 'Quality' : 'Excellent', 'Berthing Cost' : '1D x Cr1000', 'Fuel' : 'Refined',
         'Facilities' : 'Shipyard (all), Repair, Highport 6+', 'Bases' : 'Military  8+, Naval 8+, Scout 10+' },
 'B' : { 'Quality' : 'Good', 'Berthing Cost' : '1D x Cr500' , 'Fuel' : 'Refined',
         'Facilities' : 'Shipyard (spacecraft), Repair, Highport 8+', 'Bases' : 'Military 8+, Naval 8+, Scout 9+' },
 'C' : { 'Quality' : 'Routine', 'Berthing Cost' : '1D x Cr100', 'Fuel' : 'Unrefined',
         'Facilities' : 'Shipyard (small craft), Repair, Highport 10+', 'Bases' : 'Military 10+ Scout 9+' },
 'D' : { 'Quality' : 'Poor', 'Berthing Cost' : '1D x Cr 10',  'Fuel' : 'Unrefined',
         'Facilities' : 'Limited Repair, Highport 12+', 'Bases' : 'Scout 8+, Corsair 12+' },
 'E' : { 'Quality' : 'Frontier', 'Berthing Cost' : '0', 'Fuel': 'Unrefined', 'Facilities' : 'None', 'Bases' : 'Corsair 10+' },
 'X' : { 'Quality' : 'No Starport', 'Berthing Cost' : '0', 'Fuel': 'Unrefined', 'Facilities' : 'None', 'Bases' : 'Corsair 10+' }
 }


# 2d6 home brew
locations = [
   "null", "null", # 0 and 1 which are unused on a 2d6 table
   "Planet - Military", "Planet - Remote Location", "Planet - Rural",  # 2 to 6 
   "Planet - City", "Starport", "Starport", "Lunar - City",            # 6 to 8 
   "Lunar - Outpost", "System POI", "Capital Ship", "Lunar - Military" # 9 to 12
  ]

# system points of interest, per SWN page 170
systemPOI = {
  "Deep-space station" : { 
    "occupied" : { "Dangerously odd transhumans", "Freeze-dried ancient corpses", "Secretive military observers", 
                   "Eccentric oligarch and minions", "Deranged but brilliant scientist" },  
    "situation" : { "Systems breaking down", "Foreign sabotage attempt", "Black market for the elite", 
                    "Vault for dangerous pretech", "Supply base for pirates"}
   },
  "Asteroid base" : {},
  "Remote moon base" : {},
  "Ancient orbital ruin" : {},
  "Research base" : {},
  "Asteroid belt" : {},
  "Gas giant mine" : {},
  "Refueling station" : {}
}

# 2d6 distances, homebrew, 0 means same system
parsecsAway = [ 
  'null', 'null', # 0 and 1 
  5, 4, 3, 2,   # 2 to 5 
  0, 1, 0,      # 6 to 8
  2, 3, 4, 5    # 9 to 12
  ]

# from mgt2e core rules, pg 163, solar is homebrew but it is less than mercury's distance from the sun
distances = {
  "solar" : 50000000, "primary world" : 150000000, "close neighbor world" : 45000000, 
  "far neighbor world" : 255000000, "close gas giant" : 600000000, "far gas giant" : 900000000
  }

# 2d6 planets, homebrew, primary planet most likely
planets = [ 
  "null", "null", 
  "far gas giant", "close gas giant", "far neighbor world", "close neighbor world", # 2 to 5 
  "primary world","primary world","primary world",                                  # 6 to 8
  "close neighbor world","far neighbor world","close gas giant", "far gas giant"    # 9 to 12
  ]


# from mgt2e core rules 92
alliesEnemies = [ 
   "Naval Officer", "Imperial Diplomat ", "Crooked Trader ", "Medical Doctor", "Eccentric", "Scientist", "Mercenary", "Famous", "Performer", "Alien Thief",
   "Free Trader", "Explorer", "Marine Captain", "Corporate", "Executive", "Researcher", "Cultural Attaché ", "Religious Leader ", "Conspirator",
   "Rich Noble", "Artificial Intelligence", "Bored Noble", "Planetary Governor", "Inveterate Gambler", "Crusading Journalist", "Doomsday Cultist",
   "Corporate Agent", "Criminal Syndicate", "Military Governor", "Army Quartermaster", "Private Investigator", "Starport Administrator", "Retired Admiral",
   "Alien Ambassador", "Smuggler", "Weapons Inspector", "Elder Statesman", "Planetary Warlord", "Imperial Agent"
  ]

characterQuirks = [
  'Loyal', 'Distracted by other worries','In debt to criminals','Makes very bad jokes','Will betray characters','Aggressive','Has secret allies',
  'Secret anagathic user','Looking for something','Helpful','Forgetful','Wants to hire the Travellers','Has useful contacts','Artistic','Easily confused',
  'Unusually ugly','Worried about current situation','Shows pictures of their children','Rumour-monger','Unusually provincial','Drunkard or drug addict',
  'Government informant','Mistakes a Traveller for someone else','Possesses unusually advanced technology','Unusually handsome or beautiful',
  'Spying on the Travellers','Possesses TAS membership','Is secretly hostile towards the Travellers','Wants to borrow money',
  'Is convinced the Travellers are dangerous','Involved in political intrigue','Has a dangerous secret','Wants to get off planet as soon as possible',
  'Attracted to a Traveller','From offworld','Possesses telepathy or other unusual quality'
  ]

# from mgt2e core rules pg 93
patrons = [
  "Assassin","Smuggler","Terrorist","Embezzler","Thief","Revolutionary","Clerk","Administrator","Mayor","Minor Noble","Physician","Tribal Leader",
  "Diplomat","Courier","Spy","Ambassador","Noble","Police Officer","Merchant","Free Trader","Broker","Corporate Executive","Corporate Agent","Financier",
  "Belter","Researcher","Naval Officer","Pilot","Starport Administrator","Scout","Alien","Playboy","Stowaway","Family Relative","Agent of a Foreign Power",
  "Imperial Agent"
  ]

# from mgt2e core rules pg 93
missions = [
  "Assassinate a target", "Frame a target", "Destroy a target", "Steal from a target", "Aid in a burglary", "Stop a burglary", 
  "Retrieve data or an object from a secure facility", "Discredit a target", "Find a lost cargo", "Find a lost person", "Deceive a target", 
  "Sabotage a target", "Transport goods", "Transport a person", "Transport data", "Transport goods secretly", "Transport goods quickly", 
  "Transport dangerous goods", "Investigate a crime", "Investigate a theft", "Investigate a murder", "Investigate a mystery", "Investigate a target", 
  "Investigate an event", "Join an expedition", "Survey a planet", "Explore a new system", "Explore a ruin", "Salvage a ship", "Capture a creature", 
  "Hijack a ship", "Entertain a noble", "Protect a target", "Save a target", "Aid a target", "It is a trap – the Patron intends to betray the Traveller" 
  ]

# from mgt2e core rules pg 94
targets = [
  'Common Trade Goods','Common Trade Goods','Random Trade Goods','Random Trade Goods','Illegal Trade Goods','Illegal Trade Goods','Computer Data',
  'Alien Artefact','Personal Effects','Work of Art','Historical Artefact','Weapon','Starport','Asteroid Base','City','Research station','Bar or Nightclub',
  'Medical Facility','Roll on the Random Patron table','Roll on the Random Patron table','Roll on the Random Patron table',
  'Roll on the Allies and Enemies table','Roll on the Allies and Enemies table','Roll on the Allies and Enemies table','Local Government',
  'Planetary Government','Corporation','Imperial Intelligence','Criminal Syndicate','Criminal Gang','Free Trader','Yacht','Cargo Hauler','Police Cutter',
  'Space Station','Warship'
  ]

# from mgt2e core rules pg 94
oppositions = [
  'Animals','Large animal','Bandits & thieves','Fearful peasants','Local authorities','Local lord','Criminals – thugs or corsairs',
  'Criminals – thieves or saboteurs','Police – ordinary security forces','Police – inspectors & detectives','Corporate – agents',
  'Corporate – legal','Starport security','Imperial marines','Interstellar corporation','Alien – private citizen or corporation',
  'Alien – government ','Space travellers or rival ship','Target is in deep space','Target is in orbit','Hostile weather conditions',
  'Dangerous organisms or radiation','Target is in a dangerous region','Target is in a restricted area','Target is under electronic observation',
  'Hostile guard robots or ships','Biometric identification required','Mechanical failure or computer hacking','Travellers are under surveillance',
  'Out of fuel or ammunition','Police investigation','Legal barriers','Nobility','Government officials','Target is protected by a third party','Hostages'
  ]

# from mgt2e core rules pg 95
starportEncounters = [
  "Maintenance robot at work", "Trade ship arrives or departs", "Captain argues about fuel prices",
  "News report about pirate activity on a starport screen draws a crowd", "Bored clerk makes life difficult for the Travellers", 
  "Local merchant with cargo to transport seeks a ship", "Dissident tries to claim sanctuary from planetary authorities",
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

# from mgt2e core rules pg 96
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

# from mgt2e core rules pg 154, payment every 4 weeks
salaries = {
  "pilot" : 6000, "astrogator" : 5000, "engineer" : 4000, "steward" : 2000, "medic" : 3000, "gunner" : 1000, "marine" : 1000
  }

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

### Appearances

# grabbed from various wikipedia articles
naturalHairColors = [
  # black colors
 'black','jey black','soft black','raven black',
  # brown colors
  'brunette','dark brown','brown','light brown','walnut brown','dark chesnut brown','chesnut brown','light chesnut brown','caramel brown',
  'light golden brown','mousy brown','light ash brown','maple brown',
  # red colors
  'reddish brown','deep burgundy','burgundy','auburn','red','red orange','orange red','bright copper','copper','burnt orange','ginger','strawberry blond',
  'ruby red',
  # blond colors
  'light blond', 'golden blond','blond','fair','yellowish blond','golden brownish','light chesnut','ash blond','flaxen blond','dirty blond',
  'dishwater blond','honey blond','platinum blond','sandy blond','venetian blond','reddish blond','bleached blond',
  # grey and white colors
  'dark gray','gray','silver','white'
 ]

# off the top of my head, adding neon to some to distinguish from natural variants
unnaturalHairColors = [
 'green','blue','purple','pink','neon orange','neon yellow','violet'
 ]

# didnt find any good descriptions, these are off the top of my head
grayedHair = [
 'salt and peppered gray','streaks of gray','gray highlights','grayed roots','gray low lights'
 ]

# descriptors used on wikipedia page on eye color, and some of my own variations on those
eyeColors = [
  'brown','dark','dark brown','black','light brown',                         # brown
  'amber','copper','golden','yellow','green and amber','orangish amber',     # amber
  'hazel','brownish green','goldish green',                                  # hazel
  'dark green','blue and green','blueish green',                             # green
  'blue','crystal blue','blue green','dark blue','bright blue',              # blue 
  'gray','light gray','dark grey','grey and blue','greyish blue'             # gray 
  ]

# 2d6 off the top of my head
heights = [ 
  'null', 'null',
  'very short', 'short', 'below average height', 'just under average height',   # 2 to 5 
  'average height', 'average height', 'average height',                         # 6 to 8
  'above average height', 'tall', 'very tall', 'incredibly tall'                # 9 to 12
  ]

# 2d6 off the top of my head
bodyTypes = [
  'null', 'null',
  'skeletal', 'very slender', 'slender', 'slim but muscular',   # 2 to 5
  'slim', 'average build', 'fit',                               # 6 to 8
  'curvy', 'muscular', 'heavy set', 'very muscular'             # 9 to 12
  ]
