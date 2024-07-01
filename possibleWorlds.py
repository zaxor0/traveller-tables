#!/usr/bin/python3

from tables import *

import json
import requests
import sys
import time

def worldSearch(world, sectorName=False):
  # first try world name 
  world = world.replace(' ','%20')
  searchUrl = 'https://travellermap.com/api/search?q=' + world 
  response = requests.get(searchUrl)
  data = json.loads(response.text)
  results = []
  for result in data['Results']['Items']:
    try:
      results.append(result['World'])
    except:
      pass
  if len(results) > 1:
    # if we have more than 1 result, try again with the sector to be more specific
    if sectorName:
      sectorName = sectorName.replace(' ','%20')
      query = str(world + "%20in:" + sectorName)
      searchUrl = 'https://travellermap.com/api/search?q="' + query
      response = requests.get(searchUrl)
      data = json.loads(response.text)
      results = []
      for result in data['Results']['Items']:
        try:
          results.append(result['World'])
        except:
          pass
      return results[0]
    else:
      selected = False
      while selected == False:
        position = 0
        print('Possible Sectors:')
        for world in results:
          print(' ',str(position + 1),'-',world['Sector'])
          position += 1
        selection = int(input('Which sector are you in? ')) - 1
        try:
          world = results[selection]
          selected = True
        except:
          print('not a valid number')
      return world
  else:
    return results[0]

def worldDetailed(world): 
  sectorX = world['SectorX'] 
  sectorY = world['SectorY'] 
  hexX = world['HexX'] 
  hexY = world['HexY'] 
  worldDetailedURL = 'https://travellermap.com/api/credits?sx=' + str(sectorX) + '&sy=' + str(sectorY) + '&hx=' + str(hexX) + '&hy=' + str(hexY)
  response = requests.get(worldDetailedURL)
  return json.loads(response.text)

def jumpSearch(world, jump):
  jumpRange = jump
  jumpUrl = 'https://travellermap.com/api/jumpworlds?sector=' + str(world['SectorName']) + '&hex=' + str(world['WorldHex']) + '&jump=' + str(jumpRange)
  response = requests.get(jumpUrl)
  return json.loads(response.text)

def nearbyPlanets(world, jump):
  nearbyWorlds = jumpSearch(world, jump)
  planetsArray = []
  for planet in nearbyWorlds['Worlds']:
    if planet['Name'] != world:
      planetsArray.append(planet['Name'])
  return planetsArray, nearbyWorlds

def nearbyPlanetsCoords(world, jump):
  nearbyWorlds = jumpSearch(world, jump)
  planetsDict = {}
  for planet in nearbyWorlds['Worlds']:
    if planet['Name'] != world:
      planetsDict[planet['Name']] = planet['Hex']
  return planetsDict, nearbyWorlds

def worldPoster(world):
  try: # data format provided by the world detailed results (called credits in the api)
    sectorName = str(world['SectorName']) 
    worldHex = str(world['WorldHex']) 
  except:
    pass
  try:  # data format provided by the jump search results
    sectorName = str(world['Sector'])
    worldHex = str(world['Hex'])
  except:
    pass
  sectorName = sectorName.replace(' ','%20')
  url = 'https://travellermap.com/print/world?sector=' + sectorName + '&hex=' + worldHex + '&style=poster'
  return url

def jumpMap(world):
  try: # data format provided by the world detailed results (called credits in the api)
    sectorName = str(world['SectorName']) 
    worldHex = str(world['WorldHex']) 
  except:
    pass
  try:  # data format provided by the jump search results
    sectorName = str(world['Sector'])
    worldHex = str(world['Hex'])
  except:
    pass
  sectorName = sectorName.replace(' ','%20')
  url = 'https://travellermap.com/api/jumpmap?sector=' + sectorName + '&hex=' + str(world['WorldHex']) + '&style=poster&options=33008&jump=6'
  return url

def travellerMap(world):
  try: # data format provided by the world detailed results (called credits in the api)
    sectorName = str(world['SectorName']) 
    worldHex = str(world['WorldHex']) 
  except:
    pass
  try:  # data format provided by the jump search results
    sectorName = str(world['Sector'])
    worldHex = str(world['Hex'])
  except:
    pass
  sectorName = sectorName.replace(' ','%20')
  url = 'https://travellermap.com/go/' + sectorName + '/' + worldHex 
  return url

def remarksTranslator(remarks):
  print('translate')

def uwpTranslator(uwp):
  starport = starportQuality[uwp[0]]
  if starport['Quality'] == 'No Starport':
    starport = str('None')
  else:
    starport = str(
      starport['Quality'] + 
     '\n  Berthing Cost - ' + starport['Berthing Cost'] +
     '\n  Fuel Available - ' + starport['Fuel'] + 
     '\n  Facilities - ' + starport['Facilities'] +
     '\n  Bases - ' + starport['Bases'] )
  size = worldSize[uwp[1]]
  atmo = worldAtmosphere[uwp[2]]
  hydro = worldHydrographics[uwp[3]]
  pop = worldPopulation[uwp[4]]
  gov = worldGovernment[uwp[5]]
  law = worldLawLevel[uwp[6]]
  tech = worldTechLevel[uwp[8]]
  description = {
    'Starport Quality' : starport,
    'World Size' : str(size['Size'] + ' diameter with gravity at ' + size['Gravity']),
    'Atmosphere' : str(atmo['Atmosphere'] + ', Pressure: ' + atmo['Pressure'] + ', Required gear: ' + atmo['Required Gear']),
    'Hydrographics' : str(hydro['Hydrographic Percentage'] + ' water coverage, ' + hydro['Description']),
    'Population' : pop['Inhabitants'],
    'Government' : gov['Government Type'],
    'Law Level' : str('Weapons banned - ' + law['Weapons Banned']),
    'Tech Level' : str(tech['Level'] + '\n  ' + tech['Description'])
    }
  return description
