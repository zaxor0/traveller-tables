#!/usr/bin/python3


def tradeCodes(system, sector):
  world = worldSearch(system, sector)
  world = worldDetailed(world)
  uwp = uwpTranslator(world['WorldUwp'])
  starport = starportQuality[uwp[0]]
  size = worldSize[uwp[1]]
  atmo = worldAtmosphere[uwp[2]]
  hydro = worldHydrographics[uwp[3]]
  pop = worldPopulation[uwp[4]]
  gov = worldGovernment[uwp[5]]
  law = worldLawLevel[uwp[6]]
  tech = worldTechLevel[uwp[8]]

  tradeCodes = []
  if atmo in range(4,9) and hydro in range(4,8) and pop in range(5,7):
    tradeCodes.append['Ag'] # Agricultural
  if size == 0 and atmo == 0 and hydro == 0:
    tradeCodes.append['As'] # Asteroid
  if pop == 0 and gov == 0 and law == 0:
    tradeCodes.append['Ba'] # Barren
  if atmo in range(2,9) and hydro == 0:
    tradeCodes.append['De'] # Desert
  if atmo >= 10 and hydro >= 1:
    tradeCodes.append['Fl'] # Fluid Oceans
  if size in range(6,8) and atmo in range(5,8) and atmo != 7 and hydro in range(5,7):
    tradeCodes.append['Ga'] # Garden
  if pop >= 9:
    tradeCodes.append['Hi'] # High Population
  if tech >= 12:
    tradeCodes.append['Ht'] # High Tech 
