# Model of absolute risk for breast cancer

This model is based on Gail risk model, however it uses Russian mortality and BC incidence to fit model.  Russians are treated as one more race in Gail model. 

## Files
* **BCPT.py** - Risk calculation script
* **BCPTConvert.py** - Input values converter
* **Constants.py** -  Population model constants
* **GailConstants.py** - Gail model constants
* **Helper.py** - Risk Calculation wrapper
* **PopModel.py** - Population model that's used to fit Russian data for Gail model
* **TestScript.py** - Test script and model fitting (tuning) function 

## Example of function Helper.RiskCalc

``` python 
import Helper as hlp
import BCPTConvert as bc

riskIndex = 0 #Uselss
currentAge = bc.GetCurrentAge("50")
finalAge = 90
menarcheAge = bc.GetMenarcheAge("12")
firstLiveBirthAge = bc.GetFirstLiveBirthAge("-1")
firstDegreeRel = bc.GetFirstDegRelatives("0")
hadBiopsy = bc.GetEverHadBiopsy("1")
numBiopsy = bc.GetNumberOfBiopsy("1")
hyperPlasia = bc.GetHyperPlasia("0")
race = bc.GetRace("1")
absRisk = 0

# Calculate whole life year risk.
absRisk, avgRisk = hlp.RiskCalc(riskIndex, currentAge, finalAge, 
                                menarcheAge, firstLiveBirthAge, hadBiopsy, 
                                numBiopsy, hyperPlasia, firstDegreeRel, race)
# Whole life risk to percent format
absRiskPctg, avgRiskPctg = hlp.CalcPercentage(absRisk, avgRisk)

# Calculate 5-year year risk.
absRisk, avgRisk = hlp.RiskCalc(riskIndex, currentAge, currentAge+5, 
                                menarcheAge, firstLiveBirthAge, hadBiopsy, 
                                numBiopsy, hyperPlasia, firstDegreeRel, race)
# 5-year risk to percent format
absRiskPctg, avgRiskPctg = hlp.CalcPercentage(absRisk, avgRisk)

```
 
 
## Outputs

* **absRisk** - absolute risk 
* **avgRisk** - average risk
     
## Inputs

Most of the parameters are transformed with BCPTConvert script

* **riskIndex** - usless parameter which was used to choose between avg and abs risk. Now it calculates both
* **currentAge** - from 20 to 90
* **finalAge** - Greater than  **currentAge**. Less than 90.
* **menarcheAge** - 7 to 18
* **firstLiveBirthAge** - 0 to 50
* **hadBiopsy** -  0 - no, 1- yes
* **numBiopsy** - integer greater than 0
* **hyperPlasia** - 0 - no, 1- yes
* **firstDegreeRel** - integer
* **race** - always = 1 

