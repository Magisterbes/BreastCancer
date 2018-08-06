import BCPTConvert as bco
import BCPT
import numpy as np

def RiskCalc(riskIndex, 
             currentAge, 
             projectionAge, 
             menarcheAge, 
             firstLiveBirthAge, 
             everHadBiopsy, 
             numberOfBiopsy, 
             hyperPlasia, 
             firstDegRelatives, 
             race):

    currentAge = bco.GetCurrentAge(currentAge)
    menarcheAge = bco.MenarcheAge(menarcheAge)
    firstLiveBirthAge = bco.FirstLiveBirthAge(firstLiveBirthAge)
    everHadBiopsy = bco.EverHadBiopsy(everHadBiopsy)
    numberOfBiopsy = bco.NumberOfBiopsy(numberOfBiopsy, everHadBiopsy)
    hyperPlasia = bco.Hyperplasia(hyperPlasia, everHadBiopsy)
    #firstDegRelatives = bco.FirstDegRelatives(firstDegRelatives);
    race = bco.GetRace(str(race))
    if race < 7:
        firstDegRelatives = bco.FirstDegRelatives(firstDegRelatives)
    else:
        firstDegRelatives = bco.FirstDegRelatives(firstDegRelatives, race)
    ageIndicator = bco.CurrentAgeIndicator(currentAge)
    rHyperPlasia = bco.RHyperplasia(hyperPlasia, everHadBiopsy)
    riskIndex = 1 #get absolute risk
    
    absoluteRisk = BCPT.CalculateAbsoluteRisk(currentAge, projectionAge, ageIndicator, numberOfBiopsy, menarcheAge, firstLiveBirthAge, firstDegRelatives, everHadBiopsy, hyperPlasia, rHyperPlasia, race)
    averageRisk = BCPT.CalculateAeverageRisk(currentAge, projectionAge, ageIndicator, numberOfBiopsy, menarcheAge, firstLiveBirthAge, firstDegRelatives, everHadBiopsy, hyperPlasia, rHyperPlasia, race)


    return (absoluteRisk, averageRisk)

def CalcPercentage(absoluteRisk, averageRisk):
    absoluteRisk = np.round(absoluteRisk, 6)
    averageRisk = np.round(averageRisk, 6)
    absoluteRiskPctg = np.round(absoluteRisk * 100, 1)
    averageRiskPctg = np.round(averageRisk * 100, 1)
    return (absoluteRiskPctg,averageRiskPctg)
