#!/usr/bin/python3

# flat rate of Cr 1,000 per ton for service
# also can engage in speculative trade, buy low sell high

availability = {
  'Agricultural' : {
    'acronym' : 'A',
    'purchaseDM' : { 
      'Textiles' : -7,'Liquor' : -4, 'Wood' : -6, 'Grain' : -2, 'Meat' : -2 'Spices' : -2 'Fruit' : -3 
      },
    'resaleDM' : { 
      'Textiles' : -6,'Liquor' : -3, 'Wood' : -6, 'Grain' : -2, 'Meat' : -2 'Spices' : -2 'Fruit' : -2, 'Computers' : -3,
      'All Terrain Vehicles' : 1, 'Armored Vehicles' : 2, 'Farm Machinery' : 5, 'Cybernetic Parts' : 1,
      'Computer Parts' : 1, 'Machine Tools' : 1
      }
     },
  'Non-agricultural' : {
    'acronym' : 'NA',
    'purchaseDM' : { 
      'Textiles' : -5, 'Crystals' : -3, 'Petrochemicals' : -4, 'Grain' : 1, 'Meat' : 2, 'Spices' : 3, 'Fruit' : 1,
      'Pharmaceuticals' : -3, 'Vacc Suits' : -5
      },
    'resaleDM' : {
      'Textiles' : 1, 'Crystals' : -3, 'Petrochemicals' : -4, 'Pharmaceuticals' : -3, 'Armored Vehicles' : -2, 
      'Farm Machinery' : -8, 'Vacc Suits' : -1
      }
     },
  'Poor' : {
    'acronym' : 'P',
    'purchaseDM' : {
      'Polymers' : 2, 'Steel' : 1, 'Copper' : 1, 'Aluminum' : 1, 'Tin' : 1, 'Silver' : 2, 'Pharmaceuticals' : 3, 
      'Gems' : -3, 'Firearms' : 3, 'Ammunition' : 3, 'Blades' : 3, 'Tools' : 3, 'Body Armor' : 3, 'Armored Vehicles' : 4
      },
    'resaleDM' : {
        'Steel' : 3, 'Meat' : 1, 'Spices' : 3, 'Fruit' : 2, 'Firearms' : 3, 'Ammunition' : 3, 'Blades' : 3, 'Tools' : 3,
        'Body Armor' : 4, 'Aircraft' : 1, 'Air/Raft' : 1, 'Computers' : 1, 'All Terrain Vehicles' : 1, 
        'Farm Machinery' : 1, 'Elections Parts' : 1, 'Vacc Suits' : 1
      }
     },
  'Rich' : {
    'acronym' : 'R',
    'purchaseDM' : { },
    'resaleDM' : { }
  'Industrial' : {
    'acronym' : 'I',
    'purchaseDM' : { },
    'resaleDM' : { }
     },
  'Non-industrial' : {
    'acronym' : 'NI',
    'purchaseDM' : { },
    'resaleDM' : { }
     }
  }


# first roll 2 d6, set them together to get 
