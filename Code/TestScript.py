import Helper as hlp
import numpy as np
import PopModel as pop
import GailConstants
import BCPT
import Constants
import BCPTConvert  
from tqdm import tqdm

def Tune():
    
    # RiskCalculator.rf_tuned = 0.4 +i * 0.01;
    # RiskCalculator.rf50_tuned = 0.52+j * 0.01;
    inc = pop.GeneratePopulationResultInt(20000)
    print(inc)
    print(Constants.IncidenceRussia)
    compare = np.linalg.norm(np.array(inc)-np.array(Constants.IncidenceRussia))
    print("Res: " + str(compare))


#def CompareResult(inc):
#    diff = 0.0
#    i = 0

#    while i < len(inc):
#        k = 1.0
#        if i < 5:
#            k = (len(inc) - i)
#        diff += np.abs(inc[i] - Constants.IncidenceRussia[i]) * k
#        i += 1
#    return diff



if __name__ == "__main__":

        #Tune()

        # This risk assessment was based on data for white females.
        # Researchers are conducting additional studies, including studies with minority populations, to gather more data and to
        # increase the accuracy of the tool for women in these populations.
        # Also, this tool cannot calculate breast cancer risk accurately for women with a medical history of any breast cancer or of DCIS or LCIS.
        # Setup Sample Data.
        currentAge = BCPTConvert.GetCurrentAge("50")
        menarcheAge = BCPTConvert.GetMenarcheAge("12")
        firstLiveBirthAge = BCPTConvert.GetFirstLiveBirthAge("-1")
        firstDegreeRel = BCPTConvert.GetFirstDegRelatives("0")
        hadBiopsy = BCPTConvert.GetEverHadBiopsy("1")
        numBiopsy = BCPTConvert.GetNumberOfBiopsy("1")
        hyperPlasia = BCPTConvert.GetHyperPlasia("0")
        race = BCPTConvert.GetRace("1")
        absRisk = 0
        # Calculate 5 year risk.
        absRisk, avgRisk = hlp.RiskCalc(0, currentAge, 90, menarcheAge, firstLiveBirthAge, hadBiopsy, numBiopsy, hyperPlasia, firstDegreeRel, race)
        absRiskPctg, avgRiskPctg = hlp.CalcPercentage(absRisk, avgRisk)
        print("5 year risk")
        print("This woman (age {}) = {:.3f}%".format(currentAge, absRiskPctg))
        print("Average woman (age {}) = {:.3f}% (нет отдельной таблицы по средней белой женщине, поэтому считается усреднением по этой же статистике. Реальный результат может быть выше.)".format(currentAge, avgRiskPctg))
        # Calculate lifetime risk.
        #absRisk, avgRisk = hlp.RiskCalc(0, currentAge, 90, menarcheAge, firstLiveBirthAge, hadBiopsy, numBiopsy,
        #    hyperPlasia, firstDegreeRel, race);
        #absRisk, avgRisk = hlp.CalcPercentage(absRisk, avgRisk);
        #print("\nLifetime risk");
        #print("This woman (to age 90): " + absRiskPctg.ToString("F1"));
        #print("Average woman (to age 90): " + avgRiskPctg.ToString("F1"));

