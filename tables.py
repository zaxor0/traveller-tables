#!/usr/sbin/python3

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

# 2d6 planets, homebrew, primary planet most likely
planets = [ 
  "null", "null", 
  "far gas giant", "close gas giant", "far neighbor world", "close neighbor world", # 2 to 5 
  "primary world","primary world","primary world",                                  # 6 to 8
  "close neighbor world","far neighbor world","close gas giant", "far gas giant"    # 9 to 12
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

### Appearances

# grabbed from various wikipedia articles
naturalHairColors = [
  # black colors
 'black','jet black','soft black','raven black',
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
