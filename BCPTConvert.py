#It was race enum in C#, but now it's not needed for a while
class BcptRace():

    @staticmethod
    def GetRace(o):
        return(1)


__UNKNOWN = "UNKNOWN"
__UDERSCORE = "__"
__EMPTY = ""
__YES = "YES"
__NO = "NO"
__NA = "NA"
__0BIRTHS = "0 BIRTHS"

def GetCurrentAge(o):
    o = str(o).upper()

    if  (o == __UNKNOWN or 
        o == __UDERSCORE or  
        o == __EMPTY or  
        o == __NA):
        rval = 90
    elif str(o).upper() == "< 35" or str(o).upper() == "<35":
        rval = 34
    else:
        rval = int(float(o))
    return rval


def GetProjectionAge(o):

    o = o.strip().upper()

    if (o == __UNKNOWN or 
        o == __UDERSCORE or 
        o == __EMPTY or 
        o == __NA):
        rval = 90
    else:
        rval = int(float(o))
    return rval

def GetMenarcheAge(o):
    o = o.strip().upper()

    if  (o == __UNKNOWN or 
    o == __UDERSCORE or 
    o == __EMPTY or 
    o == __NA or 
    o == __0BIRTHS):
        rval = 99
    elif o == "7 TO 11":
        rval = 10
    elif o == "12 TO 13":
        rval = 13
    elif o == "> 13":
        rval = 15
    else:
        rval = int(float(o))
    return rval


def GetFirstLiveBirthAge(o):
    o = str(o).upper()

    if (o == __UNKNOWN or 
    o == __UDERSCORE or 
    o == __EMPTY or 
    o == __NA):
        rval = 99
    elif o == "0":
        rval = 0
    elif o == "< 20":
        rval = 15
    elif o == "20 TO 24":
        rval = 22
    elif o == "25 TO 30":
        rval = 27
    elif o == "> 30":
        rval = 31
    else:
        rval = int(float(o))

    return rval

def GetFirstDegRelatives(o):
    o = str(o).upper()

    if (o == __UNKNOWN or 
        o == __UDERSCORE or 
        o == __EMPTY or 
        o == __NA):
        rval = 99
    elif o == "0":
        rval = 0
    elif o == "1":
        rval = 1
    elif o == "> 1":
        rval = 2
    else:
        rval = int(float(o))
    return rval

    
def GetEverHadBiopsy(o):
    o = str(o).upper()

    rval = 99
    if (o == __UNKNOWN or 
        o == __UDERSCORE or 
        o == __EMPTY or 
        o == __NA):
        rval = 99
    elif o == __NO or o == "0":
        rval = 0
    elif o == __YES or o == "1":
        rval = 1

    return rval

def GetNumberOfBiopsy(o):
    o = str(o).upper()
        
    if (o == __UNKNOWN or 
        o == __UDERSCORE or 
        o == __EMPTY or 
        o == __NA):
        rval = 99
    elif o == "1":
        rval = 1
    elif o == "> 1":
        rval = 2
    else:
        rval = int(float(o))
    return rval


def GetHyperPlasia(o):
    o = str(o).upper()

    if (o == __UNKNOWN or 
       o == __UDERSCORE or 
       o == __EMPTY or 
       o == __NA):
        rval = 99
    elif o == __NO:
        rval = 0
    elif o == __YES:
        rval = 1
    else:
        rval = int(float(o))
    return rval

def GetRace(o):

    rval = BcptRace.GetRace(o)
    return rval


def CurrentAgeIndicator(currentAge):
    currentAge = int(currentAge)
    rval = 0
    if currentAge < 50:
        rval = 0
    elif currentAge >= 50:
        rval = 1
    return rval


def MenarcheAge(menarcheAge):
    menarcheAge = int(menarcheAge)
    rval = 0
    if menarcheAge >= 7 and menarcheAge < 12:
        rval = 2
    elif menarcheAge >= 12 and menarcheAge < 14:
        rval = 1
    elif menarcheAge >= 14 and menarcheAge <= 39 or menarcheAge == 99:
        rval = 0
    return rval


def FirstLiveBirthAge(firstLiveBirthAge):
    firstLiveBirthAge = int(firstLiveBirthAge)
    rval = 0
    if firstLiveBirthAge == 0:
        # no live birth
        rval = 2
    elif firstLiveBirthAge > 0:
        if firstLiveBirthAge < 20 or firstLiveBirthAge == 99: # includes unknown
            rval = 0
        elif firstLiveBirthAge >= 20 and firstLiveBirthAge < 25:
            rval = 1
        elif firstLiveBirthAge >= 25 and firstLiveBirthAge < 30:
            rval = 2
        elif firstLiveBirthAge >= 30 and firstLiveBirthAge <= 55:
            rval = 3
    return rval


def FirstDegRelatives(firstDegRelatives):
    firstDegRelatives = int(firstDegRelatives)

    rval = 0
    if firstDegRelatives == 0 or firstDegRelatives == 99:
        rval = 0
    elif firstDegRelatives == 1:
        rval = 1
    elif firstDegRelatives >= 2 and firstDegRelatives <= 31:
        rval = 2
    return rval


def FirstDegRelativesByRace(firstDegRelatives, race):
    firstDegRelatives = int(firstDegRelatives)
    race = int(race)

    rval = 0
    if firstDegRelatives == 0 or firstDegRelatives == 99:
        rval = 0
    elif firstDegRelatives == 1:
        rval = 1
    elif firstDegRelatives >= 2 and firstDegRelatives <= 31 and race < 7:
        rval = 2
    elif firstDegRelatives >= 2 and race >= 7:
        rval = 1
    return rval


def EverHadBiopsy(everHadBiopsy):
    everHadBiopsy = int(everHadBiopsy)

    rval = 0
    if everHadBiopsy == 99:
        #case 0:
        rval = 0
    else:
        rval = everHadBiopsy
    return rval


def NumberOfBiopsy(numberOfPreviousBiopsy, everHadBiopsy):
    numberOfPreviousBiopsy = int(numberOfPreviousBiopsy)
    everHadBiopsy = int(everHadBiopsy)

    rval = 0
    if everHadBiopsy == 99:
        rval = 99
    elif numberOfPreviousBiopsy == 0 or (numberOfPreviousBiopsy == 99 and everHadBiopsy == 99):
        rval = 0
    elif numberOfPreviousBiopsy == 1 or (numberOfPreviousBiopsy == 99 and everHadBiopsy == 1):
        rval = 1
    elif numberOfPreviousBiopsy > 1 and numberOfPreviousBiopsy <= 30:
        rval = 2
    return rval


def Hyperplasia(hyperplasia, everHadBiopsy):
    hyperplasia = int(hyperplasia)
    everHadBiopsy = int(everHadBiopsy)

    if everHadBiopsy == 0:
        rval = 99
    else:
        rval = hyperplasia
    return rval


def RHyperplasia(hyperplasia, everHadBiopsy):
    hyperplasia = int(hyperplasia)
    everHadBiopsy = int(everHadBiopsy)

    #if (everHadBiopsy == 0) hyperplasia = 0;
    if hyperplasia == 1: # hyperplasia=yes
        rval = 1.82
    elif hyperplasia == 0: # hyperplasia=no
        rval = 0.93
    else: # hyperplasia=never had biopsy
        rval = 1.0
    return rval

