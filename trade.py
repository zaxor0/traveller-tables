#!/usr/bin/python3

from mechanics import *
from spaceMap import *
from tables import *
from possibleWorlds import *

import getch
import locale

def calcTradeCodes(system, sector):
  world = worldSearch(system, sector)
  world = worldDetailed(world)
  uwp = world['WorldUwp']
  # convert from travellers "hex" codes
  uwpArray = [ uwp[0], uwp[1], uwp[2], uwp[3], uwp[4], uwp[5], uwp[6], uwp[8] ]
  hexValues = { 'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15 }
  position = 0
  for value in uwpArray:
    for lett in hexValues:
      num = hexValues[lett]
      if value == lett:
        uwpArray[position] = num
    position += 1

  starport = uwpArray[0]
  size = int(uwpArray[1])
  atmo = int(uwpArray[2])
  hydro = int(uwpArray[3])
  pop = int(uwpArray[4])
  gov = int(uwpArray[5])
  law = int(uwpArray[6])
  tech = int(uwpArray[7])

  tradeCodes = []
  if atmo in range(4,9) and hydro in range(4,8) and pop in range(5,7):
    tradeCodes.append('Ag') # Agricultural
  if size == 0 and atmo == 0 and hydro == 0:
    tradeCodes.append('As') # Asteroid
  if pop == 0 and gov == 0 and law == 0:
    tradeCodes.append('Ba') # Barren
  if atmo in range(2,9) and hydro == 0:
    tradeCodes.append('De') # Desert
  if atmo >= 10 and hydro >= 1:
    tradeCodes.append('Fl') # Fluid Oceans
  if size in range(6,8) and atmo in range(5,8) and atmo != 7 and hydro in range(5,7):
    tradeCodes.append('Ga') # Garden
  if pop >= 9:
    tradeCodes.append('Hi') # High Population
  if tech >= 12:
    tradeCodes.append('Ht') # High Tech 
  if atmo in range(0,1) and hydro >= 1:
    tradeCodes.append('Ic') # Ice-Capped 
  if atmo in [0,1,2,4,7,9,10,11,12] and pop >= 9:
    tradeCodes.append('In') # Industrial
  if pop in range(1,3):
    tradeCodes.append('Lo') # Low Population
  if pop >= 1 and tech <= 5:
    tradeCodes.append('Lt') # Low Tech
  if atmo in range(0,3) and hydro in range(0,3) and pop >=6:
    tradeCodes.append('Na') # Low Tech
  if atmo in range(2,5) and hydro in range(0,3):
    tradeCodes.append('Po') # Poor
  if atmo in range(6,8) and pop in range(6,8) and gov in range(4,9):
    tradeCodes.append('Ri') # Rich
  if atmo == 0:
    tradeCodes.append('Va') # Vacuum
  if (atmo in range(3,9) or atmo >= 13) and hydro >= 10:
    tradeCodes.append('Wa') # Waterworld
 
  readableCodes = []
  for code in tradeCodes:
    readableCodes.append(readableTradeCodes[code]) 
  return readableCodes

# mgt2e 242 to 245
def goodsAvailable(good, population, readableTradeCodes):
  # gather trade good details
  for dieVal in tradeGoods:
    if tradeGoods[dieVal]['type'] == good:
      tons = tradeGoods[dieVal]['tons'] 
      price = tradeGoods[dieVal]['base price'] 
      purchaseMods = tradeGoods[dieVal]['purchase DM'] 
      saleMods = tradeGoods[dieVal]['sale DM'] 
  
  # calc tons available
  if ' x ' in tons:
    tonsDieCount = tons.split(' x ')[0]
    tonsDieCount = int(tonsDieCount[:-1])
    tonsMulti = int(tons.split(' x ')[1])
  else:
    tonsDieCount = tons
    tonsDieCount = int(tonsDieCount[:-1])
    tonsMulti = int(1)
  tonsRoll = diceRoll(tonsDieCount, 6) 
  tonsAvailable = tonsRoll * tonsMulti

  ## calc purchase price
  # inital 3d6 dice roll
  basePurchaseRoll = diceRoll(3,6)
  diceModTotal = 0
  # add any DM from purchase DM column
  for diceMod in purchaseMods: 
    if diceMod in readableTradeCodes:
      diceModTotal += purchaseMods[diceMod] 
  # subtract any DM from the sale DM column
  for diceMod in saleMods: 
    if diceMod in readableTradeCodes:
      diceModTotal -= saleMods[diceMod] 
  # subtract suppliers/seller broker skill, default of 2 (this would be an NPC)
  brokerSkill = 2
  diceModTotal -= brokerSkill

  modifiedResult =  basePurchaseRoll + diceModTotal
  # modifiedPrice is in tables.py sourced from page 243 of mgt2e
  purchasePrice = modifiedPrice[modifiedResult]['Purchase Price'] * price

  return tonsAvailable, purchasePrice

def sellGoods(good, readableTadecodes):
  # gather trade good details
  for dieVal in tradeGoods:
    if tradeGoods[dieVal]['type'] == good:
      price = tradeGoods[dieVal]['base price'] 
      purchaseMods = tradeGoods[dieVal]['purchase DM'] 
      saleMods = tradeGoods[dieVal]['sale DM'] 
  
  ## calc sale price
  # inital 3d6 dice roll
  basePurchaseRoll = diceRoll(3,6)
  diceModTotal = 0
  # subtract any DM from purchase DM column
  for diceMod in purchaseMods: 
    if diceMod in readableTradeCodes:
      diceModTotal -= purchaseMods[diceMod] 
  # add any DM from the sale DM column
  for diceMod in saleMods: 
    if diceMod in readableTradeCodes:
      diceModTotal += saleMods[diceMod] 
  # subtract suppliers/seller broker skill, default of 2 (this would be the PLAYER)
  brokerSkill = 2
  diceModTotal -= brokerSkill

  modifiedResult =  basePurchaseRoll + diceModTotal
  # modifiedPrice is in tables.py sourced from page 243 of mgt2e
  sellPrice = modifiedPrice[modifiedResult]['Sale Price'] * price

  return sellPrice

def tradeMenu(currentSystem, sector, ship, saveFile):
  jumpRange = ship['jump']
  reachableSystems = jumpSearch(currentSystem,jumpRange)
  reachableWorlds = []
  for rSystem in reachableSystems['Worlds']:
    if rSystem['Name'] != currentSystem['WorldName']:
      reachableWorlds.append(rSystem)
  uwp = uwpTranslator(currentSystem['WorldUwp'])
  population = currentSystem['WorldUwp'][4]
  codes = calcTradeCodes(currentSystem['WorldName'],currentSystem['SectorName'])
  header = '# You are in: ' + str(currentSystem['WorldName']) + ' # has trade codes: ' + str(codes)

  # create purchaseable goods dict
  goodsPurchase = {}
  count = 0
  for code in codes:
    for goods in tradeGoods:
      if code in tradeGoods[goods]['availability']:
        letter = letters[count]
        namedGood = tradeGoods[goods]['type']
        tonsAvail, perTonBuy = goodsAvailable(namedGood, population, codes)
        purchasePrice = int(tonsAvail * perTonBuy)
        goodsPurchase.update( { namedGood : { 'letter' : letter, 'tons' : tonsAvail, 'purchase' : purchasePrice } })
        count += 1

  # create sellable goods dict
  goodsToSell = {}
  count = 0
  cargo = ship['cargo']['stored']
  for good in cargo:
    letter = letters[count]
    tonsAvail = cargo[good]['tons']
    originalCost = cargo[good]['cost']
    perTonSell = sellGoods(good, codes)
    sellPrice = int(tonsAvail * perTonSell)
    goodsToSell.update( { good : { 'letter' : letter, 'tons' : tonsAvail, 'sell' : sellPrice, 'cost' : originalCost } })
    count += 1
  nextAvailLetter = count

  trading = True
  while trading:
    money = saveFile['credits']

    # print out
    clear()
    print(header)
    print('---[ Goods for Purchase (p) ]---')
    goodStrings = []
    for good in goodsPurchase:
      goodStrings.append(good)

    rows = 5
    columns = int(len(goodStrings) / rows)
    if len(goodStrings) % rows != 0:
      columns += 1
    for i in range(rows):
      pos = i
      rowString = ' '
      for j in range(columns):
        if len(goodStrings[pos]) > 22:
          tab = '\t'
        elif len(goodStrings[pos]) < 15:
          tab = '\t\t\t'
        else:
          tab = '\t\t'
        rowString = rowString + goodStrings[pos] + tab
        try:
          goodStrings[pos + rows]
          pos = pos + rows
        except:
          break
      print(rowString)

    print('\n---[   Goods to Sell  (s)   ]---')
    for good in goodsToSell:
      print(good)

    # recalc cargo space
    maxCargo = ship['cargo']['max']
    availCargo = 0
    usedCargo = 0
    for storedGood in ship['cargo']['stored']:
      tonnage = ship['cargo']['stored'][storedGood]['tons']
      usedCargo += tonnage
    availCargo = maxCargo - usedCargo
    print('\nYou currently have',maxCargo,'max and',availCargo,'available')

    print('\nWould you like to: (P) purchase a good, (S) view offers on your goods, (Q) Return to main')
    playerKey = getch.getch()
    if playerKey in [ 'p', 's', 'q']:
      if playerKey == 'p':
        clear()
        print(header)
        print('Goods Availble for Purchase:')
        for good in goodsPurchase:
          letter = goodsPurchase[good]['letter']
          tonsAvail = goodsPurchase[good]['tons']
          price = goodsPurchase[good]['purchase']
          stringPrice = str('Cr ' + locale.format_string('%d',price,True))
          if len(good) >= 26:
            tabs = ''
          elif len(good) >= 19 and len(good) < 26:
            tabs = '\t'
          elif len(good) >=11 and len(good) < 19:
            tabs = '\t\t'
          elif len(good) < 11:
            tabs = '\t\t\t'
          print(letter,'-',good,tabs,tonsAvail,'tons \t\t', stringPrice)
        print('Which good would you like to purchase?')
        selectedGood = getch.getch()
        message = 'That is not a good you can purchase'
        for good in goodsPurchase:
          letter = goodsPurchase[good]['letter']
          tons = goodsPurchase[good]['tons']
          price = goodsPurchase[good]['purchase']
          stringPrice = str('Cr ' + locale.format_string('%d',price,True))
          if selectedGood == letter:
            if tons <= availCargo and price <= money:
              purchaseMade = True
              goodsPurchase.pop(good)
              message = 'Congratulations you purchased ' + str(tons) + ' of '  + good + ' for a total of ' + stringPrice
              if good in ship['cargo']['stored']:
                origTons = ship['cargo']['stored'][good]['tons']
                origCost = ship['cargo']['stored'][good]['cost']
                cost = int((origCost / origTons) + (price / tons))
                tons = tons + origTons
              else:
                cost = price
              saveFile['credits'] =  money - price
              ship['cargo']['stored'].update( { good : { 'tons' : tons, 'cost' : cost }} )
              goodsToSell.update( { good : { 'letter' : letters[nextAvailLetter], 'tons' : tons, 'sell' : price, 'cost' : cost } })
              nextAvailLetter +=1
              #goodsPurchase.pop(good)
            elif tons > availCargo and price <= money:
              message = 'You do not have enough cargo space'
            elif tons <= availCargo and price > money:
              message = 'You do not have enough credits'
            elif tons > availCargo and price > money:
              message = 'You do not have enough credits and you do not have enough cargo space'
            break
        print(message)
        input('\n press any key to continue')
      if playerKey == 's':
        clear()
        print(header)
        print('Goods Available to Sell:')
        for good in goodsToSell:
          letter = goodsToSell[good]['letter']
          tonsAvail = goodsToSell[good]['tons']
          sellPrice = goodsToSell[good]['sell']
          origCost = ship['cargo']['stored'][good]['cost']
          stringPrice = str('Cr ' + locale.format_string('%d',sellPrice,True))
          if len(good) >= 26:
            tabs = ''
          elif len(good) >= 19 and len(good) < 26:
            tabs = '\t'
          elif len(good) >=11 and len(good) < 19:
            tabs = '\t\t'
          elif len(good) < 11:
            tabs = '\t\t\t'
          print(letter,'-',good,tabs,tonsAvail,'tons\t',stringPrice,' - cost of',origCost)
        print('Which good would you like to sell?')
        selectedGood = getch.getch()
        message = 'That is not a good you can purchase'
        for good in goodsToSell:
          letter = goodsToSell[good]['letter']
          tonsAvail = goodsToSell[good]['tons']
          sellPrice = goodsToSell[good]['sell']
          origCost = ship['cargo']['stored'][good]['cost']
          profit = sellPrice - origCost
          if selectedGood == letter:
            sellString = 'Are you sure you want to sell ' + good + ' for ' + str(sellPrice) + '? Profit of ' + str(profit) +'\n> '
            toSell = input(sellString)
            if toSell in yesses:
              ship['cargo']['stored'].pop(good)
              goodsToSell.pop(good)
              newMoney = money + sellPrice
              print('Credits',str(money),'->',str(newMoney))
              saveFile['credits'] =  newMoney
            break
        input('\n press any key to continue')
      if playerKey == 'q':
        trading = False

  return saveFile



  # a planet has all its trade code goods AND common goods
  # additionally, it has "random goods" equal to the worlds population good

  # all common goods are available, roll amount per the "tons" column for a given type
  # trade goods are only present if the planet has that trade code

  # for worlds with pop 3 or less, roll DM-3, if 9 or higher, DM+3

  # per the world population code (0 to 9), roll that many 2d6 to get that many d66 values
  # those values will tell you additional goods that are available
