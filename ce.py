#!/usr/sbin/python3

# cephius engine tables

# ce srd page 168
worldSize = { 
  '0' : {'Size' : '800 km',    'Gravity' : 'negligible' }, # typically an asteroid
  '1' : {'Size' : '1,600 km',  'Gravity' : '.05' },
  '2' : {'Size' : '3,200 km',  'Gravity' : '.15' },
  '3' : {'Size' : '4,800 km',  'Gravity' : '.25' },
  '4' : {'Size' : '6,400 km',  'Gravity' : '.35' },
  '5' : {'Size' : '8,000 km',  'Gravity' : '.45' },
  '6' : {'Size' : '9,600 km',  'Gravity' : '.7' },
  '7' : {'Size' : '11,200 km', 'Gravity' : '.9' },
  '8' : {'Size' : '12,800 km', 'Gravity' : '1.' },
  '9' : {'Size' : '14,400 km', 'Gravity' : '1.25' },
  'A' : {'Size' : '16,000 km', 'Gravity' : '1.4' }
  }

# ce srd page 169
worldAtmosphere = {
  '0' : {'Atmosphere' : 'None',               'Pressure' : '0.00',         'Required Gear' : 'Vacc Suit'         },
  '1' : {'Atmosphere' : 'Trace',              'Pressure' : '0.001 to 0.09','Required Gear' : 'Vacc Suit'         },
  '2' : {'Atmosphere' : 'Very Thin, Tainted', 'Pressure' : '0.1 to 0.42',  'Required Gear' : 'Respirator, Filter'},
  '3' : {'Atmosphere' : 'Very Thin',          'Pressure' : '0.1 to 0.42',  'Required Gear' : 'Respirator'        },
  '4' : {'Atmosphere' : 'Thin, Tainted',      'Pressure' : '0.43 to 0.7',  'Required Gear' : 'Filter'            },
  '5' : {'Atmosphere' : 'Thin',               'Pressure' : '0.43 to 0.7',  'Required Gear' : 'None'              },
  '6' : {'Atmosphere' : 'Standard',           'Pressure' : '0.71 to 1.49', 'Required Gear' : 'None'              },
  '7' : {'Atmosphere' : 'Standard, Tainted',  'Pressure' : '0.7 to 1.49',  'Required Gear' : 'Filter'            },
  '8' : {'Atmosphere' : 'Dense',              'Pressure' : '1.5 to 2.49',  'Required Gear' : 'None'              },
  '9' : {'Atmosphere' : 'Dense, Tainted',     'Pressure' : '1.5 to 2.49',  'Required Gear' : 'Filter'            },
  'A' : {'Atmosphere' : 'Exotic',             'Pressure' : 'Varies',       'Required Gear' : 'Air Supply'        },
  'B' : {'Atmosphere' : 'Corrosive',          'Pressure' : 'Varies',       'Required Gear' : 'Vacc Suit'         },
  'C' : {'Atmosphere' : 'Insidious',          'Pressure' : 'Varies',       'Required Gear' : 'Vacc Suit'         },
  'D' : {'Atmosphere' : 'Dense, High',        'Pressure' : '2.5+',         'Required Gear' : 'None'              },
  'E' : {'Atmosphere' : 'Thin, Low',          'Pressure' : '0.5 or less',  'Required Gear' : 'None'              },
  'F' : {'Atmosphere' : 'Unusual',            'Pressure' : 'Varies',       'Required Gear' : 'Varies'            }
  }

# ce crd page 169
atmosphereTypes = {
  'Tainted' : 'Tainted atmospheres contain some element that is harmful to humans, such as an unusually high proportion of carbon dioxide. A character who breathes a tainted atmosphere without a filter will suffer 1D6 damage every few minutes (or hours, depending on the level of taint).',
  'Exotic: An exotic atmosphere is unbreathable by humans, but is not otherwise hazardous. A character needs an air supply to breath in an exotic atmosphere.',
  'Corrosive' : 'Corrosive atmospheres are highly dangerous. A character who breathes in a corrosive atmosphere will suffer 1D6 damage each round.',
  'Insidious' : 'An insidious atmosphere is like a corrosive one, but it is so corrosive that it attacks equipment as well. The chief danger in an insidious atmosphere is that the toxic gases will destroy the seals and filters on the character’s protective gear. An insidious atmosphere worms its way past protection after 2D6 hours on average, although vigilant maintenance or advanced protective gear can prolong survival times.',
  'Dense, High' : 'These worlds have thick N2/O2 atmospheres, but their mean surface pressure is too high to support unprotected human life (high pressure nitrogen and oxygen are deadly to humans). However, pressure naturally decreases with increasing altitude, so if there are highlands at the right altitude the pressure may drop enough to support human life. Alternatively, there may not be any topography high enough for humans to inhabit, necessitating floating gravitic or dirigible habitats or sealed habitats on the surface.',
  'Thin, Low' : 'The opposite of the Dense, High atmosphere, these massive worlds have thin N2/O2 atmospheres that settle in the lowlands and depressions and are only breathable there – the pressure drops off so rapidly with altitude that the highest topographic points of the surface may be close to vacuum.',
  'Unusual' : 'An Unusual atmosphere is a catchall term for an atmosphere that behaves in a strange manner. Examples include ellipsoidal atmospheres, which are thin at the poles and dense at the equator; Panthalassic worlds composed of a rocky core surrounded by a water layer hundreds of kilometers thick; worlds wracked by storms so intense that that the local air pressure changes from dense to thin depending on the current weather; and other planets with unusual and hazardous atmospheric conditions.'
}

# ce srd page 170, different arrangment of descriptions than mgt2e, CT doesnt have desctipions.
worldHydrographics = {
  '0' : {'Hydrographic Percentage' : '0% - 5%',    'Description' : 'Desert world' },
  '1' : {'Hydrographic Percentage' : '6% - 15%',   'Description' : 'Dry world' },
  '2' : {'Hydrographic Percentage' : '16% - 25%',  'Description' : 'A few small seas' },
  '3' : {'Hydrographic Percentage' : '26% - 35%',  'Description' : 'Small seas and oceans' },
  '4' : {'Hydrographic Percentage' : '36% - 45%',  'Description' : 'Wet World' },
  '5' : {'Hydrographic Percentage' : '46% - 55%',  'Description' : 'Large oceans' },
  '6' : {'Hydrographic Percentage' : '56% - 65%',  'Description' : '' },
  '7' : {'Hydrographic Percentage' : '66% - 75%',  'Description' : 'Earth-like world' },
  '8' : {'Hydrographic Percentage' : '76% - 85%',  'Description' : 'Water world' },
  '9' : {'Hydrographic Percentage' : '86% - 95%',  'Description' : 'Only a few islands and archipelagos' },
  'A' : {'Hydrographic Percentage' : '96% - 100%', 'Description' : 'Almost entirely water' }
}


# ce srd page 171, mgt2e has B and C levels 
worldPopulation = {
  '0' : { 'Inhabitants' : 'None',                  'Range' : '0',                  'Description' : '--' }, 
  '1' : { 'Inhabitants' : 'Few',                   'Range' : '1+',                 'Description' : 'A tiny farmstead or a single family' }, 
  '2' : { 'Inhabitants' : 'Hundreds',              'Range' : '100+',               'Description' : 'A village' }, 
  '3' : { 'Inhabitants' : 'Thousands',             'Range' : '1,000+',             'Description' : '' }, 
  '4' : { 'Inhabitants' : 'Tens of thousands',     'Range' : '10,000+',            'Description' : 'Small town' }, 
  '5' : { 'Inhabitants' : 'Hundreds of thousands', 'Range' : '100,000+',           'Description' : 'Average city' }, 
  '6' : { 'Inhabitants' : 'Millions',              'Range' : '1,000,000+',         'Description' : '' }, 
  '7' : { 'Inhabitants' : 'Tens of millions',      'Range' : '10,000,000+',        'Description' : 'Large city' }, 
  '8' : { 'Inhabitants' : 'Hundreds of millions',  'Range' : '100,000,000+',       'Description' : '' }, 
  '9' : { 'Inhabitants' : 'Billions',              'Range' : '1,000,000,000+',     'Description' : 'Present day Earth' }, 
  'A' : { 'Inhabitants' : 'Tens of billions',      'Range' : '10,000,000,000+',    'Description' : '' }, 
}

# ce srd page 170-1
starportQuality = {
 'A' : { 'Descriptor' : 'Excellent',
         'Fuel' : 'Refined', 
         'Annual Maintenance' : 'Yes',
         'Shipyard' : 'Can construct starships and non-starships',
         'Possible Bases' : 'Naval, Scout' 
         },
 'B' : { 'Descriptor' : 'Good',
         'Fuel' : 'Refined',
         'Annual Maintenance' : 'Yes',
         'Shipyard' : 'Can construct non-starships',
         'Possible Bases' : 'Naval, Scout' 
         },
 'C' : { 'Descriptor' : 'Routine',
         'Fuel' : 'Unrefined', 
         'Annual Maintenance' : 'No',
         'Shipyard' : 'Can perform reasonable repairs',
         'Possible Bases' : 'Scout' 
         },
 'D' : { 'Descriptor' : 'Poor',
         'Fuel' : 'Unrefined', 
         'Annual Maintenance' : 'No',
         'Shipyard' : 'None', 
         'Possible Bases' : 'Scout' 
         },
 'E' : { 'Descriptor' : 'Frontier', 
         'Fuel': 'Unrefined',  
         'Annual Maintenance' : 'No',
         'Shipyard' : 'None', 
         'Possible Bases' : 'None' 
         },
 'X' : { 'Descriptor' : 'None',
         'Fuel': 'None',
         'Annual Maintenance' : 'No',
         'Shipyard' : 'None',
         'Possible Bases' : 'None' 
         }
 }

# ce srd page 172
worldGovernment = {
  '0' : {'Government Type' : 'None' },
  '1' : {'Government Type' : 'Company/Corporation' },
  '2' : {'Government Type' : 'Participating Democracy' },
  '3' : {'Government Type' : 'Self-Perpetuating Oligarchy' },
  '4' : {'Government Type' : 'Representative Democracy' },
  '5' : {'Government Type' : 'Feudal Technocracy' },
  '6' : {'Government Type' : 'Captive Government' },
  '7' : {'Government Type' : 'Balkanisation' },
  '8' : {'Government Type' : 'Civil Service Bureaucracy' },
  '9' : {'Government Type' : 'Impersonal Bureaucracy' },
  'A' : {'Government Type' : 'Charismatic Dictator' },
  'B' : {'Government Type' : 'Non-Charismatic Dictator' },
  'C' : {'Government Type' : 'Charismatic Oligarchy' },     
  'D' : {'Government Type' : 'Religious Dictatorship' },
  'E' : {'Government Type' : 'Religious Autocracy' },
  'F' : {'Government Type' : 'Totalitarian Oligarchy' }
}

# ce srd page 172-3
worldLawLevel = {
  '0' : { 'Descriptor' : 'No Law',      'Not Allowed' : 'No restrictions', 'Amber Zone' : 'Candidate' },
  '1' : { 'Descriptor' : 'Low Law',     'Not Allowed' : 'Poison gas, explosives, undetectable weapons, weapons of mass desctruction' },
  '2' : { 'Descriptor' : 'Low Law',     'Not Allowed' : 'Portable energy weapons (except ship-mounted)' },
  '3' : { 'Descriptor' : 'Low Law',     'Not Allowed' : 'Heavy weapons' },
  '4' : { 'Descriptor' : 'Medium Law',  'Not Allowed' : 'Light assault weapons and submachine guns' },
  '5' : { 'Descriptor' : 'Medium Law',  'Not Allowed' : 'Personal concealable weapons' },
  '6' : { 'Descriptor' : 'Medium Law',  'Not Allowed' : 'All firearms except shotguns and stunners; carrying weapons discouraged' },
  '7' : { 'Descriptor' : 'High Law',    'Not Allowed' : 'Shotguns'},
  '8' : { 'Descriptor' : 'High Law',    'Not Allowed' : 'All bladed weapons,stunners' },
  '9' : { 'Descriptor' : 'High Law',    'Not Allowed' : 'Any weapons outside one\'s residence', 'Amber Zone' : 'Candidate' }
  'A' : { 'Descriptor' : 'Extreme Law', 'Not Allowed' : 'Any weapons allowed at all', 'Amber Zone' : 'Candidate' }
}

# ce srd page 66
worldTechLevel = {
  '0' : { 
    'Level' : 'Primitive', 
    'Description' : 'No technology.'
    },
  '1' : { 
    'Level' : 'Primitive', 
    'Description' : 'Roughly on a par with Bronze or Iron age technology.'
    },
  '2' : { 
      'Level' : 'Primitive', 
      'Description' : 'Renaissance technology.'
      },
  '3' : { 
      'Level' : 'Primitive', 
      'Description' : 'Mass production allows for product standardization, bringing the germ of industrial revolution and steam power.'
      },
  '4' : { 
      'Level' : 'Industrial', 
      'Description' : 'Transition to industrial revolution is complete, bringing plastics, radio and other such inventions.'
      },
  '5' : { 
      'Level' : 'Industrial', 
      'Description' : 'Widespread electrification, tele-communications and internal combustion.'
      },
  '6' : { 
      'Level' : 'Industrial', 
      'Description' : 'Development of fission power and more advanced computing.'
      },
  '7' : { 
      'Level' : 'Pre-Stellar', 
      'Description' : 'Can reach orbit reliably and has telecommunications satellites.'
      },
  '8' : { 
      'Level' : 'Pre-Stellar', 
      'Description' : 'Possible to reach other worlds in the same star system, terraforming or full colonisation are not within the culture’s capacity.'
      },
  '9' : { 
      'Level' : 'Pre-Stellar', 
      'Description' : 'Development of gravity manipulation, which makes space travel vastly safer and faster; first steps into Jump Drive technology'
      },
  'A' : { 
      'Level' : 'Early Stellar', 
      'Description' : 'With the advent of Jump, nearby systems are opened up.'
      },
  'B' : { 
      'Level' : 'Early Stellar', 
      'Description' : 'The first primitive (non-creative) artificial intelligences become possible in the form of "low autonomous" interfaces, as computers begin to model synaptic networks'
      },
  'C' : { 
      'Level' : 'Average Stellar', 
      'Description' : 'Weather control revolutionises terraforming and agriculture.'
      },
  'D' : { 
      'Level' : 'Average Stellar', 
      'Description' : 'Battle dress appears on the battlefield in response to new weapons."High autonomous" interfaces allow computers to become self-actuating and self-teaching'
      },
  'E' : { 
      'Level' : 'Average Stellar', 
      'Description' : 'Fusion weapons become man-portable.'
      },
  'F' : { 
      'Level' : 'High Stellar', 
      'Description' : 'Black globe generators suggest a new direction for defensive technologies, while the development of synthetic anagathics means that human lifespan is now vastly increased'
      }
}

# ce srd page 174
readableTradeCodes = { 
 'Ag' : 'Agricultural',     'As' : 'Asteroid',       'Ba' : 'Barren',     'De' : 'Desert',     'Fl' : 'Fluid Oceans',   'Ga' : 'Garden', 
 'Hi' : 'High Pop',         'Ht' : 'High Tech',      'Ic' : 'Ice Capped', 'In' : 'Industrial', 'Lo' : 'Low Pop',        'Lt' : 'Low Tech', 
 'Na' : 'Non Agricultural', 'Ni' : 'Non Industrial', 'Po' : 'Poor',       'Ri' : 'Rich',       'Va' : 'Vacuum',         'Wa' : 'Water World'
  }


# ce srd page 116 
commonGoods = {
  'Basic Consumable Goods'   : { 'Cost' : 1000,  'Tons' : '2D6x5' },
  'Basic Elextronics'        : { 'Cost' : 25000, 'Tons' : '2D6x5' },
  'Basic Machine Parts'      : { 'Cost' : 10000, 'Tons' : '2D6x5' },
  'Basic Manufactured Goods' : { 'Cost' : 20000, 'Tons' : '2D6x5' },
  'Basic Raw MAterials'      : { 'Cost' : 5000,  'Tons' : '2D6x5' },
  'Basic Unrefined Ore'      : { 'Cost' : 2000,  'Tons' : '2D6x5' }
  }

# ce srd page 116 
tradeGoods = {
  11 : { 'Advanced Electronics',        'base price' : 100000,  'tons' : '1D6x5',
    'purchase DM' : { 'Industrial' : 2, 'High Tech' : 3, 'Rich' : 1 }, 
    'sale DM'     : { 'Non Inudstrial' : 2, 'Low Tech' : 1, 'Poor' : 1},
    },
  12 : { 'Advanced Manufactured Goods', 'base price' : 200000,   'tons' : '1D6x5',
    'purchase DM' : { 'Industrial' : 2, 'High Tech' : 3, 'Rich' : 1 }, 
    'sale DM'     : { 'Non Inudstrial' : 2, 'Low Tech' : 1, 'Poor' : 1},
    },
  13 : { 'Agricultural Equipment',      'base price' : 150000,   'tons' : '1D6',
    'purchase DM' : { 'Industrial' : 2, 'High Tech' : 3, 'Rich' : 1 }, 
    'sale DM'     : { 'Non Inudstrial' : 2, 'Low Tech' : 1, 'Poor' : 1},
    },
  14 : { 'Animal Products',             'base price' : 1500,     'tons' : '4D6x5',
    'purchase DM' : { 'Industrial' : 2, 'High Tech' : 3, 'Rich' : 1 }, 
    'sale DM'     : { 'Non Inudstrial' : 2, 'Low Tech' : 1, 'Poor' : 1},
    },
  15 : { 'Collectibles',                'base price' : 20000,    'tons' : '1D x 5', 
    'purchase DM' : { 'Industrial' : 2, 'High Tech' : 3, 'Rich' : 1 }, 
    'sale DM'     : { 'Non Inudstrial' : 2, 'Low Tech' : 1, 'Poor' : 1},
    },
  16 : { 'Computers & Parts'            'base price' : 20000,    'tons' : '1D x 5',
    'purchase DM' : { 'Industrial' : 2, 'High Tech' : 3, 'Rich' : 1 }, 
    'sale DM'     : { 'Non Inudstrial' : 2, 'Low Tech' : 1, 'Poor' : 1},
    },
  21 : { 'Crystals & Gems',             'base price' : 20000,    'tons' : '1D',
    'purchase DM' : { 'Industrial' : 2, 'High Tech' : 3, 'Rich' : 1 }, 
    'sale DM'     : { 'Non Inudstrial' : 2, 'Low Tech' : 1, 'Poor' : 1},
    },
  22 : { 'Cybernetic Parts',            'base price' : 20000,    'tons' : '1D x 10',
    'purchase DM' : { 'Industrial' : 2, 'High Tech' : 3, 'Rich' : 1 }, 
    'sale DM'     : { 'Non Inudstrial' : 2, 'Low Tech' : 1, 'Poor' : 1},
    },
  23 : { 'Food Service Equip.',         'base price' : 20000,    'tons' : '1D x 10',
    'purchase DM' : { 'Industrial' : 2, 'High Tech' : 3, 'Rich' : 1 }, 
    'sale DM'     : { 'Non Inudstrial' : 2, 'Low Tech' : 1, 'Poor' : 1},
    },
  24 : { 'Furniture',                   'base price' : 20000,    'tons' : '1D',
    'purchase DM' : { 'Industrial' : 2, 'High Tech' : 3, 'Rich' : 1 }, 
    'sale DM'     : { 'Non Inudstrial' : 2, 'Low Tech' : 1, 'Poor' : 1},
    },
  25 : { 'Gambling Devices & Equip.',   'base price' : 20000,    'tons' : '1D x 5',
    'purchase DM' : { 'Industrial' : 2, 'High Tech' : 3, 'Rich' : 1 }, 
    'sale DM'     : { 'Non Inudstrial' : 2, 'Low Tech' : 1, 'Poor' : 1},
    },
  26 : { 'Grav Vehicles' ,              'base price' : 20000,    'tons' : '1D x 10',
    'purchase DM' : { 'Industrial' : 2, 'High Tech' : 3, 'Rich' : 1 }, 
    'sale DM'     : { 'Non Inudstrial' : 2, 'Low Tech' : 1, 'Poor' : 1},
    },
  31 : { 'Grocery Prodcuts',            'base price' : 20000,    'tons' : '1D',
    'purchase DM' : { 'Industrial' : 2, 'High Tech' : 3, 'Rich' : 1 }, 
    'sale DM'     : { 'Non Inudstrial' : 2, 'Low Tech' : 1, 'Poor' : 1},
    },
  32 : { 'Household Appliances',        'base price' : 20000,    'tons' : '1D x 10',
    'purchase DM' : { 'Industrial' : 2, 'High Tech' : 3, 'Rich' : 1 }, 
    'sale DM'     : { 'Non Inudstrial' : 2, 'Low Tech' : 1, 'Poor' : 1},
    },
  33 : { 'Industrial Supplies',         'base price' : 20000,    'tons' : '1D',
    'purchase DM' : { 'Industrial' : 2, 'High Tech' : 3, 'Rich' : 1 }, 
    'sale DM'     : { 'Non Inudstrial' : 2, 'Low Tech' : 1, 'Poor' : 1},
    },
  34 : { 'Liquor & Intoxicants',        'base price' : 20000,    'tons' : '1D',
    'purchase DM' : { 'Industrial' : 2, 'High Tech' : 3, 'Rich' : 1 }, 
    'sale DM'     : { 'Non Inudstrial' : 2, 'Low Tech' : 1, 'Poor' : 1},
    },
  35 : { 'Luxury Goods',                'base price' : 20000,    'tons' : '1D x 5',
    'purchase DM' : { 'Industrial' : 2, 'High Tech' : 3, 'Rich' : 1 }, 
    'sale DM'     : { 'Non Inudstrial' : 2, 'Low Tech' : 1, 'Poor' : 1},
    },
  36 : { 'Manufacturing Equip.',        'base price' : 20000,    'tons' : '1D x 10',
    'purchase DM' : { 'Industrial' : 2, 'High Tech' : 3, 'Rich' : 1 }, 
    'sale DM'     : { 'Non Inudstrial' : 2, 'Low Tech' : 1, 'Poor' : 1},
    },
  41 : { 'Medical Equip.',              'base price' : 20000,    'tons' : '1D x 20',
    'purchase DM' : { 'Industrial' : 2, 'High Tech' : 3, 'Rich' : 1 }, 
    'sale DM'     : { 'Non Inudstrial' : 2, 'Low Tech' : 1, 'Poor' : 1},
    },
  42 : { 'Petrochemicals',              'base price' : 20000,    'tons' : '1D x 20',
    'purchase DM' : { 'Industrial' : 2, 'High Tech' : 3, 'Rich' : 1 }, 
    'sale DM'     : { 'Non Inudstrial' : 2, 'Low Tech' : 1, 'Poor' : 1},
    },
  43 : { 'Pharmaceuticals',             'base price' : 20000,    'tons' : '1D x 10',
    'purchase DM' : { 'Industrial' : 2, 'High Tech' : 3, 'Rich' : 1 }, 
    'sale DM'     : { 'Non Inudstrial' : 2, 'Low Tech' : 1, 'Poor' : 1},
    },
  44 : { 'Polymers',                    'base price' : 20000,    'tons' : '1D x 20',
    'purchase DM' : { 'Industrial' : 2, 'High Tech' : 3, 'Rich' : 1 }, 
    'sale DM'     : { 'Non Inudstrial' : 2, 'Low Tech' : 1, 'Poor' : 1},
    },
  45 : { 'Precious Metals',             'base price' : 20000,    'tons' : '1D x 10',
    'purchase DM' : { 'Industrial' : 2, 'High Tech' : 3, 'Rich' : 1 }, 
    'sale DM'     : { 'Non Inudstrial' : 2, 'Low Tech' : 1, 'Poor' : 1},
    },
  46 : { 'Radioactives',                'base price' : 20000,    'tons' : '1D x 5',
    'purchase DM' : { 'Industrial' : 2, 'High Tech' : 3, 'Rich' : 1 }, 
    'sale DM'     : { 'Non Inudstrial' : 2, 'Low Tech' : 1, 'Poor' : 1},
    },
  51 : { 'Robots & Drones',             'base price' : 20000,    'tons' : '1D',
    'purchase DM' : { 'Industrial' : 2, 'High Tech' : 3, 'Rich' : 1 }, 
    'sale DM'     : { 'Non Inudstrial' : 2, 'Low Tech' : 1, 'Poor' : 1},
    },
  52 : { 'Scientific Equipment',        'base price' : 20000,    'tons' : '1D',
    'purchase DM' : { 'Industrial' : 2, 'High Tech' : 3, 'Rich' : 1 }, 
    'sale DM'     : { 'Non Inudstrial' : 2, 'Low Tech' : 1, 'Poor' : 1},
    },
  53 : { 'Survival Gear',               'base price' : 20000,    'tons' : '1D',
    'purchase DM' : { 'Industrial' : 2, 'High Tech' : 3, 'Rich' : 1 }, 
    'sale DM'     : { 'Non Inudstrial' : 2, 'Low Tech' : 1, 'Poor' : 1},
    },
  54 : { 'Textiles',                    'base price' : 20000,    'tons' : '1D x 5',
    'purchase DM' : { 'Industrial' : 2, 'High Tech' : 3, 'Rich' : 1 }, 
    'sale DM'     : { 'Non Inudstrial' : 2, 'Low Tech' : 1, 'Poor' : 1},
    },
  55 : { 'Uncommon Raw Materials',      'base price' : 20000,    'tons' : '2D x 10',
    'purchase DM' : { 'Industrial' : 2, 'High Tech' : 3, 'Rich' : 1 }, 
    'sale DM'     : { 'Non Inudstrial' : 2, 'Low Tech' : 1, 'Poor' : 1},
    }
  56 : { 'Uncommon Unrefined Ore',      'base price' : 20000,    'tons' : '2D x 10',
    'purchase DM' : { 'Industrial' : 2, 'High Tech' : 3, 'Rich' : 1 }, 
    'sale DM'     : { 'Non Inudstrial' : 2, 'Low Tech' : 1, 'Poor' : 1},
    }
}


# from mgt2e core rules page 243
modifiedPrice = {
  -3 : { 'Purchase Price' : 3.0, 'Sale Price' : .10 },
  -2 : { 'Purchase Price' : 2.5, 'Sale Price' : .20 },
  -1 : { 'Purchase Price' : 2.0, 'Sale Price' : .30 },
  0 : { 'Purchase Price' : 1.75, 'Sale Price' : .40 },
  1 : { 'Purchase Price' : 1.50, 'Sale Price' : .45 },
  2 : { 'Purchase Price' : 1.35, 'Sale Price' : .50 },
  3 : { 'Purchase Price' : 1.25, 'Sale Price' : .55 },
  4 : { 'Purchase Price' : 1.20, 'Sale Price' : .60 },
  5 : { 'Purchase Price' : 1.15, 'Sale Price' : .65 },
  6 : { 'Purchase Price' : 1.10, 'Sale Price' : .70 },
  7 : { 'Purchase Price' : 1.05, 'Sale Price' : .75 },
  8 : { 'Purchase Price' : 1.00, 'Sale Price' : .80 },
  9 : { 'Purchase Price' : .95, 'Sale Price' : .85 },
  10 : { 'Purchase Price' : .90, 'Sale Price' : .90 },
  11 : { 'Purchase Price' : .85, 'Sale Price' : 1.0 },
  12 : { 'Purchase Price' : .80, 'Sale Price' : 1.05 },
  13 : { 'Purchase Price' : .75, 'Sale Price' : 1.10 },
  14 : { 'Purchase Price' : .70, 'Sale Price' : 1.15 },
  15 : { 'Purchase Price' : .65, 'Sale Price' : 1.20 },
  16 : { 'Purchase Price' : .60, 'Sale Price' : 1.25 },
  17 : { 'Purchase Price' : .55, 'Sale Price' : 1.30 },
  18 : { 'Purchase Price' : .50, 'Sale Price' : 1.40 },
  19 : { 'Purchase Price' : .45, 'Sale Price' : 1.50 },
  20 : { 'Purchase Price' : .40, 'Sale Price' : 1.60 },
  21 : { 'Purchase Price' : .35, 'Sale Price' : 1.75 },
  22 : { 'Purchase Price' : .30, 'Sale Price' : 2.0 },
  23 : { 'Purchase Price' : .25, 'Sale Price' : 2.5 },
  24 : { 'Purchase Price' : .20, 'Sale Price' : 3.0 },
  25 : { 'Purchase Price' : .15, 'Sale Price' : 4.0 }
}

# from mgt2e core rules, pg 163, solar is homebrew but it is less than mercury's distance from the sun
distances = {
  "solar" : 50000000, "primary world" : 150000000, "close neighbor world" : 45000000, 
  "far neighbor world" : 255000000, "close gas giant" : 600000000, "far gas giant" : 900000000
  }


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


