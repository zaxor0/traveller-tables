#!/usr/bin/python3

import json
import requests
import sys

# queries for a world
# https://travellermap.com/api/search?q=exact:regina

# example of worlds within a jump radius of 4
# specifies sector and hex within that sector
# https://travellermap.com/api/jumpworlds?sector=Spinward%20Marches&hex=1910&jump=4

# query the specific coordinates
# https://travellermap.com/api/credits?sx=-4&sy=-1&hx=19&hy=10


world = sys.argv[1]
searchUrl = "https://travellermap.com/api/search?q=exact:" + world
response = requests.get(searchUrl)
data = json.loads(response.text)
# expected data:
# {'HexX': 21, 'HexY': 10, 'Sector': 'Spinward Marches', 'Uwp': 'C560757-A', 'SectorX': -4, 'SectorY': -1, 'Name': 'Yori', 'SectorTags': 'Official OTU'}
worldDetails = False
for result in data['Results']['Items']:
  try:
    worldDetails = result['World']
    break
  except:
    print("not a world")

if worldDetails:
  sectorX = worldDetails['SectorX'] 
  sectorY = worldDetails['SectorY'] 
  hexX = worldDetails['HexX'] 
  hexY = worldDetails['HexY'] 
  worldDetailURL = 'https://travellermap.com/api/credits?sx=' + str(sectorX) + '&sy=' + str(sectorY) + '&hx=' + str(hexX) + '&hy=' + str(hexY)
  response = requests.get(worldDetailURL)
  print(response.text)

# world uwp example : A788899-C
# Starport quality          A
# Size                      7
# Atmosphere type           8
# Hydrographic percentage   8
# Population                8
# Government type           9
# Law Level                 9
# Tech Level                C

starportQuality = {
 'A' : { 'Quality' : 'Excellent', 'Berthing Cost' : '1D x Cr1000', 'Fuel' : 'Refined', 
         'Facilities' : 'Shipyard (all), Repair, Highport 6+', 'Bases' : 'Military  8+, Naval 8+, Scout 10+' },
 'B' : { 'Quality' : 'Good', 'Berthing Cost' : '1D x Cr500' , 'Fuel', 'Refined', 
         'Facilities' : 'Shipyard (spacecraft), Repair, Highport 8+', 'Bases' : 'Military 8+, Naval 8+, Scout 9+' },
 'C' : { 'Quality' : 'Routine', 'Berthing Cost' : '1D x Cr100', 'Fuel' : 'Unrefined',
         'Facilities' : 'Shipyard (small craft), Repair, Highport 10+', 'Bases' : 'Military 10+ Scout 9+' },


