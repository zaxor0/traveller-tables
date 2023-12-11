#!/usr/bin/python3

import json
import requests
import sys

# mgt2e pg 257
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

def worldSearch(world):
  searchUrl = "https://travellermap.com/api/search?q=exact:" + world
  response = requests.get(searchUrl)
  data = json.loads(response.text)
  worldFound = False
  for result in data['Results']['Items']:
    try:
      worldFound = result['World']
    except:
      False
  if worldFound:
    return worldFound
  else:
    return 0

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
  travellerWorld = worldSearch(world)
  if travellerWorld:
    fullWorld = worldDetailed(travellerWorld)
    #print(fullWorld['WorldName'],'located in sector',fullWorld['SectorName'],'in hex', fullWorld['WorldHex'])
    nearbyWorlds = jumpSearch(fullWorld, jump)
    planetsArray = []
    for planet in nearbyWorlds['Worlds']:
      if planet['Name'] != world:
        planetsArray.append(planet['Name'])
    return planetsArray, nearbyWorlds

def worldPoster(world):
  world = worldSearch(world)
  if world:
    world = worldDetailed(world)
    url = 'https://travellermap.com/print/world?sector=' + str(world['SectorName']) + '&hex=' + str(world['WorldHex']) + '&style=poster'
    return url
  else:
    return 0

def jumpMap(world):
  world = worldSearch(world)
  if world:
    world = worldDetailed(world)
    url = 'https://travellermap.com/api/jumpmap?sector=' + str(world['SectorName']) + '&hex=' + str(world['WorldHex']) + '&style=poster&options=33008&jump=6'
    return url
  else:
    return 0


