#!/usr/bin/python3

from os import sys

# flat rate of Cr 1,000 per ton for service
# also can engage in speculative trade, buy low sell high

availability = {
  'Agricultural' : {
    'acronym' : 'A',
    'purchaseDM' : { 
      'Textiles' : -7,'Liquor' : -4, 'Wood' : -6, 'Grain' : -2, 'Meat' : -2, 'Spices' : -2, 'Fruit' : -3 
      },
    'resaleDM' : { 
      'Textiles' : -6,'Liquor' : -3, 'Wood' : -6, 'Grain' : -2, 'Meat' : -2, 'Spices' : -2, 'Fruit' : -2, 'Computers' : -3,
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
    },
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

tradeGoods = {
  'Textiles' : { 'roll' : 11, 'price' : 3000, 'quantityDice' : 3, 'quantityMultiplier' : 5 },
  'Polymers' : { 'roll' : 12, 'price' : 3000, 'quantityDice' : 3, 'quantityMultiplier' : 5 },
  'Liquor' : { 'roll' : 13, 'price' : 3000, 'quantityDice' : 3, 'quantityMultiplier' : 5 },
  'Wood' : { 'roll' : 14, 'price' : 3000, 'quantityDice' : 3, 'quantityMultiplier' : 5 },
  'Crystals' : { 'roll' : 15, 'price' : 3000, 'quantityDice' : 3, 'quantityMultiplier' : 5 },
  'Radioactives' : { 'roll' : 16, 'price' : 3000, 'quantityDice' : 3, 'quantityMultiplier' : 5 },
  'Steel' : { 'roll' : 21, 'price' : 3000, 'quantityDice' : 3, 'quantityMultiplier' : 5 },
  'Copper' : { 'roll' : 22, 'price' : 3000, 'quantityDice' : 3, 'quantityMultiplier' : 5 },
  'Aluminum' : { 'roll' : 23, 'price' : 3000, 'quantityDice' : 3, 'quantityMultiplier' : 5 },
  'Tin' : { 'roll' : 24, 'price' : 3000, 'quantityDice' : 3, 'quantityMultiplier' : 5 },
  'Silver' : { 'roll' : 25, 'price' : 3000, 'quantityDice' : 3, 'quantityMultiplier' : 5 },
  'Special Alloys' : { 'roll' : 26, 'price' : 3000, 'quantityDice' : 3, 'quantityMultiplier' : 5 },
  'Petrochemicals' : { 'roll' : 31, 'price' : 3000, 'quantityDice' : 3, 'quantityMultiplier' : 5 },
  'Grain' : { 'roll' : 32, 'price' : 3000, 'quantityDice' : 3, 'quantityMultiplier' : 5 },
  'Meat' : { 'roll' : 33, 'price' : 3000, 'quantityDice' : 3, 'quantityMultiplier' : 5 },
  'Spices' : { 'roll' : 34, 'price' : 3000, 'quantityDice' : 3, 'quantityMultiplier' : 5 },
  'Fruit' : { 'roll' : 35, 'price' : 3000, 'quantityDice' : 3, 'quantityMultiplier' : 5 },
  'Pharmaceuticals' : { 'roll' : 36, 'price' : 3000, 'quantityDice' : 3, 'quantityMultiplier' : 5 },
  'Gems' : { 'roll' : 41, 'price' : 3000, 'quantityDice' : 3, 'quantityMultiplier' : 5 },
  'Firearms' : { 'roll' : 42, 'price' : 3000, 'quantityDice' : 3, 'quantityMultiplier' : 5 },
  'Ammunition' : { 'roll' : 43, 'price' : 3000, 'quantityDice' : 3, 'quantityMultiplier' : 5 },
  'Blades' : { 'roll' : 44, 'price' : 3000, 'quantityDice' : 3, 'quantityMultiplier' : 5 },
  'Tools' : { 'roll' : 45, 'price' : 3000, 'quantityDice' : 3, 'quantityMultiplier' : 5 },
  'Body Armor' : { 'roll' : 46, 'price' : 3000, 'quantityDice' : 3, 'quantityMultiplier' : 5 },
  'Aircraft' : { 'roll' : 51, 'price' : 3000, 'quantityDice' : 3, 'quantityMultiplier' : 5 },
  'Air/Raft' : { 'roll' : 52, 'price' : 3000, 'quantityDice' : 3, 'quantityMultiplier' : 5 },
  'Computers' : { 'roll' : 53, 'price' : 3000, 'quantityDice' : 3, 'quantityMultiplier' : 5 },
  'All Terrain Vehicles' : { 'roll' : 54, 'price' : 3000, 'quantityDice' : 3, 'quantityMultiplier' : 5 },
  'Armored Vehicles' : { 'roll' : 55, 'price' : 3000, 'quantityDice' : 3, 'quantityMultiplier' : 5 },
  'Farm Machinery' : { 'roll' : 56, 'price' : 3000, 'quantityDice' : 3, 'quantityMultiplier' : 5 },
  '' : { 'roll' : 61, 'price' : 3000, 'quantityDice' : 3, 'quantityMultiplier' : 5 },
  '' : { 'roll' : 62, 'price' : 3000, 'quantityDice' : 3, 'quantityMultiplier' : 5 },
  '' : { 'roll' : 63, 'price' : 3000, 'quantityDice' : 3, 'quantityMultiplier' : 5 },
  '' : { 'roll' : 64, 'price' : 3000, 'quantityDice' : 3, 'quantityMultiplier' : 5 },
  '' : { 'roll' : 65, 'price' : 3000, 'quantityDice' : 3, 'quantityMultiplier' : 5 },
  '' : { 'roll' : 66, 'price' : 3000, 'quantityDice' : 3, 'quantityMultiplier' : 5 },
  }


worldType = str(sys.argv[1])

for t in availability:
  details = availability[t]
  if details['acronym'] == worldType:
    print(details)

