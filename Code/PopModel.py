import numpy as np
import Constants as pc
import BCPTConvert as btcv
import Helper as hlp
from tqdm import tqdm
from multiprocessing import Pool
import time

def Rnd():
    return np.random.rand()

deaths = []


def GenerateOne(a):
    incidenceAges =  np.array([ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ])
    deaths = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ])

    for i in range(1,100):
        answers = GenerateAnswers()
        IncDeath = np.zeros(2)
        IncDeath, isDeath = FemaleBio(answers)
        if IncDeath[1] < 100:
            deaths[int((IncDeath[1] / 5) - 4)] += 1
        if IncDeath[0] > 0:
            incidenceAges[int((IncDeath[0] / 5) - 4)] += 1

    return(incidenceAges,deaths)

def GeneratePopulationResultInt(size):

    incidenceAges =  np.array([ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ])
    DeathDistr =  np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ])
    deaths = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ])

    learntok = []
    lext = learntok.append
    pool = Pool(6)
    for res in  tqdm(pool.imap(GenerateOne, range(int(size/100)),2)):
        lext(res)
    pool.close()
    pool.join()

    for slice in learntok:
        incidenceAges += np.array(slice[0])
        deaths += np.array(slice[1])

    i = 0
    #print(incidenceAges)
    #print(deaths)

    while i < len(deaths):
        sumDeaths = np.sum(deaths[:i])
        incidenceAges[i] = incidenceAges[i] * 100000 / (5 * (size - sumDeaths))
        DeathDistr[i] = deaths[i] * 100000 / (5 * (size - sumDeaths))
        i += 1
    return incidenceAges


def FemaleBio(answers):
    isDeath = False
    IncDeath = [0,0]
    i = 20
    while i < 90:
        risk = processFemale(answers, i)
        if risk >= Rnd() and IncDeath[0] == 0:
            IncDeath[0] = i
        drisk = pc.MortalityOld[int((i / 5) - 4)]
        if IncDeath[0] != 0 and i < 70:
            drisk = 0.4
        if drisk >= Rnd():
            isDeath = True
            IncDeath[1] = i
            return (IncDeath, isDeath)
        i = i + 5
    IncDeath[1] = 100
    return (IncDeath, isDeath)


def processFemale(answers, age):
    
    currentAge = age
    menarcheAge = answers[1]
    firstLiveBirthAge = answers[2]
    firstDegreeRel = btcv.GetFirstDegRelatives(str(answers[3]))
    hadBiopsy = btcv.GetEverHadBiopsy(str(answers[4]))
    numBiopsy = btcv.GetNumberOfBiopsy("1")
    hyperPlasia = btcv.GetHyperPlasia(str(answers[5]))
    race = btcv.GetRace("1")
    absRisk = 0
    # Calculate 5 year risk.
    #   BreastRiskModel.Helper.RiskCalc(0, currentAge, currentAge + 5, menarcheAge, firstLiveBirthAge, hadBiopsy, numBiopsy,
    #       hyperPlasia, firstDegreeRel, race, true, out absRisk, out avgRisk);
    
    absRisk, avgRisk = hlp.RiskCalc(0, currentAge, currentAge + 5, menarcheAge, firstLiveBirthAge, hadBiopsy, numBiopsy, hyperPlasia, firstDegreeRel, race)
   
   
    
    return absRisk


def GenerateAnswersSpCase():
    answers = np.zeros(6)
    answers[0] = 10.0
    answers[1] = 40.0
    answers[2] = 1.0
    answers[3] = 2.0
    answers[4] = 0.0
    answers[5] = 0.0
    return answers

def GenerateAnswers():
    answers = np.zeros(6)
    i = 0
    while i < 6:
        answers[i] = GenerateRandom(pc.GetArrayByIndex(i, True), pc.GetArrayByIndex(i, False))
        # Возраст рождения первого ребенка случайно сдвигаем назад до 5  лет. (хотя там, конечно, не равномерно)
        if i == 1:
            answers[i] = np.round(answers[i] - (Rnd() * 5),0)
        #Моделируем, что может быть более одного родстввенника с раком. у 5 %
        if i == 3:
            if answers[i] == 1 and Rnd() < 0.05:
                answers[i] = 2
        i += 1
    return answers


def GenerateRandom(Disribution, Values):
    prob = 0
    rand = Rnd()
    j = 0
    while j < len(Disribution):
        prob += Disribution[j]
        if prob >= rand:
            return Values[j]
        j += 1
    return 0
