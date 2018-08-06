import numpy as np
from GailConstants import *

def CalculateAbsoluteRisk(CurrentAge, ProjectionAge, AgeIndicator, NumberOfBiopsy, MenarcheAge, FirstLiveBirthAge, FirstDegRelatives, EverHadBiopsy, ihyp, rhyp, irace):
    return CalculateRisk(1, CurrentAge, ProjectionAge, AgeIndicator, NumberOfBiopsy, MenarcheAge, FirstLiveBirthAge, EverHadBiopsy, FirstDegRelatives, ihyp, rhyp, irace)

def CalculateAeverageRisk(CurrentAge, ProjectionAge, AgeIndicator, NumberOfBiopsy, MenarcheAge, FirstLiveBirthAge, FirstDegRelatives, EverHadBiopsy, ihyp, rhyp, irace):
    return CalculateRisk(2, CurrentAge, ProjectionAge, AgeIndicator, NumberOfBiopsy, MenarcheAge, FirstLiveBirthAge, EverHadBiopsy, FirstDegRelatives, ihyp, rhyp, irace)

def CalculateRisk(riskindex, CurrentAge, ProjectionAge, AgeIndicator, NumberOfBiopsy, MenarcheAge, FirstLiveBirthAge, EverHadBiopsy, FirstDegRelatives, ihyp, rhyp, irace):
    #  RiskIndex           [1 Abs, 2 Avg]
    #, CurrentAge            //[t1]
    #, ProjectionAge        //[t2]
    #, AgeIndicator        //[i0]
    #, NumberOfBiopsy        //[i2]
    #, MenarcheAge            //[i1]
    #, FirstLiveBirthAge   //[i3]
    #, EverHadBiopsy        //[iever]
    #, HyperPlasia            //[ihyp]
    #, FirstDegRelatives   //[i4]
    #, RHyperPlasia        //[rhyp]
    #, Race                //[race]

    retval = 0.0
    # Local variables
    r8iTox2 = np.zeros((216, 9))
    #double[] r8iTox2 = new double[1944]; //[216,9];
    n = 216 # ** age categories boundaries
    r = 0.0
    #HACK
    ni = 0
    ns = 0
    ti = CurrentAge
    ts = ProjectionAge
    # 11/29/2007 SR: setting BETA to race specific lnRR
    # Это все не очень надо, потому что у нас только белая раса
    i = 0
    while i < 8:
        bet[i] = bet2[i][irace - 1]
        i += 1 #index starts from 0 hence irace-1 
    #поиск индексов возраста
    ni = FindIndex(t, ti) + 1
    ns = FindIndex(t, ts)
    incr = 0
    if riskindex == 2 and irace < 7:
        #HACK CHECK THIS
        incr = 3
    # for race specific "avg women"
    # otherwise use cols 1,2,3 depen
    # on users race                5
    # use cols 4,5,6 from rmu, rla
    #TODO Check this
    # select race specific
    cindx = 0 #column index
    cindx = incr + irace - 1
    #print("------------------Contents of rmu");
    i = 0
    while i < 14:
        rmu[i] = rmu2[i][0] # competeing baseline h
        rlan[i] = rlan2[i][0]
        i += 1 # br ca composite incid
    #print(string.Format("{0} {1} {2}", i, cindx, rmu[i].ToString("F")));
    #print("ns={0}", ns);
    #PrintArray(rlan, "rlan");
    #PrintArray(rmu, "rmu");
    rf[0] = rf2[0][incr + irace - 1] # selecting correct fac
    rf[1] = rf2[1][incr + irace - 1] # based on race
    if riskindex == 2 and irace >= 7:
        rf[0] = rf2[0][12] # selecting correct fac
        rf[1] = rf2[1][12] # based on race
    if riskindex >= 2: #&& irace < 7)
        # set risk factors to
        MenarcheAge = 0 # baseline age menarchy 
        NumberOfBiopsy = 0 # # of previous biop 
        FirstLiveBirthAge = 0 # age 1st live birth 
        FirstDegRelatives = 0 # # 1st degree relat 
        rhyp = 1.0 # set hyperplasia to 1.0 
    ilev = AgeIndicator * 108 + MenarcheAge * 36 + NumberOfBiopsy * 12 + FirstLiveBirthAge * 3 + FirstDegRelatives + 1 # matrix of
    # covariate
    # range of 1
    # AgeIndicator: age ge 50 ind  0=[20, 50)
    # 1=[50, 85)
    # MenarcheAge: age menarchy   0=[14, 39] U 99 (unknown)
    # 1=[12, 14)
    # 2=[ 7, 12)
    # NumberOfBiopsy: # biopsy       0=0 or (99 and ever had biopsy=99
    # 1=1 or (99 and ever had biopsy=1 y
    # 2=[ 2, 30]
    # FirstLiveBirthAge: age 1st live   0=<20, 99 (unknown)
    # 1=[20, 25)
    # 2=[25, 30) U 0
    # 3=[30, 55]
    # FirstDegRelatives: 1st degree rel 0=0, 99 (unknown)
    # 1=1
    # 2=[2, 31]
    # **  Correspondence between exposure level and covariate factors X
    # **  in the logistic model
    # **  i-to-X correspondence
    # r8iTox2 = BuildCovariateMat(r8iTox2);
    # PrintArray2(r8iTox2,"Name");
    r8iTox2 = r8iTox2PreCalc
    # **  Computation of breast cancer risk
    # **  sum(bi*Xi) for all covariate patterns
    i = 0
    while i < 216:
        # ln relative risk from BCDDP
        sumb[i] = 0.0
        j = 0
        while j < 8:
            sumb[i] += bet[j] * r8iTox2[i][j]
            j += 1
        i += 1
    i = 1
    while i <= 108:
        # eliminate int
        sumbb[i - 1] = sumb[i - 1] - bet[0]
        i += 1
    i = 109
    while i <= 216:
        # eliminate intercept
        sumbb[i - 1] = sumb[i - 1] - bet[0] - bet[1]
        i += 1
    j = 1
    while j <= 6:
        # age specific baseline hazard
        rlan[j - 1] *= rf[0]
        j += 1
    j = 7
    while j <= 14:
        # age specific baseline hazard a
        rlan[j - 1] *= rf[1]
        j += 1
    i = ilev # index ilev of range 1-
    # setting i to covariate p
    #HACK CHECK LOG VALUE
    sumbb[i - 1] += np.log(rhyp)
    if i <= 108:
        sumbb[i + 107] += np.log(rhyp)
    #print("sumbb  0th Elmnt {0} 107th Elmnt{1}", sumbb[0], sumbb[107]);
    #  var h1r = rlan[ni - 1] * np.Exp(sumbb[i - 1]);
    #  var SurvivalHazard = (h1r + rmu[ni - 1]);
    if ts <= t[ni]:
        # Если только  первые 5 лет смотрим
        abs[i - 1] = (1.0 - ExpDt3(ni - 1, ns, i)) * h1rSurv(ni - 1, i - 1)
    else:
        # 5 year age risk interval  calculate risk from  1st age interval  age & projection age not i
        abs[i - 1] = (1.0 - ExpDt2(ni, i)) * h1rSurv(ni - 1, i - 1) # age in
        # Если разница начального и конечного возрастов больше или равна 10 годам
        if ns - ni > 0:
            abs[i - 1] = First5Years(i, ns, ni, ProjectionAge, CurrentAge, MenarcheAge, t, abs[i - 1])
        # Если разница начального и конечного возрастов больше или равна 15 годам
        if ns - ni > 1:
            abs[i - 1] = FivePlusYears(i, ns, ni, ProjectionAge, CurrentAge, MenarcheAge, NumberOfBiopsy, t, abs[i - 1])
    #print("abs 0th Elmnt {0} 215th Elmnt{1}", abs[0], abs[215]);
    #print("abss=", abss);
    abss = abs[i - 1] * 1000.0
    #HACK CHECK THIS
    if abss - np.round(abss) >= 0.5:
        #abss = dint(abss) + 1.0 ;
        abss = np.round(abss) + 1.0
    else:
        abss = np.round(abss)
    abss /= 10.0 # ** write the results to screen and output file
    retval = abs[i - 1]
    return retval

def First5Years(i, ns, ni, ProjectionAge, CurrentAge, MenarcheAge, t, abs):
    r = 0.0
    j = 0
    ia = i
    if CurrentAge < 50 and ProjectionAge > 50:
        ia = i + 108
    r = (1.0 - ExpDt2(ns, ia)) * h1rSurv(ns - 1, ia - 1) * ExpDt2(ni, i)
    MenarcheAge = ns - 1
    j = ni + 1
    while j <= MenarcheAge:
        if t[j - 1] >= 50.0:
            r *= ExpDt2(j, ia)
        else:
            r *= ExpDt2(j, i)
        j += 1
    abs += r
    return abs

def FivePlusYears(i, ns, ni, ProjectionAge, CurrentAge, MenarcheAge, NumberOfBiopsy, t, abs):
    k = 0
    j = 0
    r = 0.0
    ia = i
    if CurrentAge < 50 and ProjectionAge > 50:
        ia = i + 108
    MenarcheAge = ns - 1
    k = ni + 1
    while k <= MenarcheAge:
        iaa = i
        if t[k - 1] >= 50.0:
            iaa = ia
        r = (1.0 - ExpDt2(k, iaa)) * h1rSurv(k - 1, iaa - 1)
        r *= ExpDt2(ni, i)
        NumberOfBiopsy = k - 1
        j = ni + 1
        while j <= NumberOfBiopsy:
            iaa = i
            if t[j - 1] >= 50.0:
                iaa = ia
            r *= ExpDt2(j, iaa)
            j += 1
        abs += r
        k += 1
    return abs

def ExpDt3(idxBeg, idxeEnd, idxAge):
    return np.exp(-SurvivalHazard(idxeEnd - 1, idxAge - 1) * (t[idxeEnd] - t[idxBeg]))

def ExpDt2(idxTime, idxAge):
    return ExpDt3(idxTime - 1, idxTime, idxAge)

def h1rSurv(idxTime, idxAge):
    return h1r(idxTime, idxAge) / SurvivalHazard(idxTime, idxAge)

def h1r(irlan, isummb):
    return rlan[irlan] * np.exp(sumbb[isummb])

def SurvivalHazard(irmu, isummb):
    h1r = rlan[irmu] * np.exp(sumbb[isummb])
    return (h1r + rmu[irmu])

def FindIndex(Array, value):
    ni = 0
    i = 1
    while i <= len(Array):
        # i-1=14 ==> current age=85, max for curre
        if value <= Array[i - 1]:
            #TODO CHECK THE INDEX
            ni = i - 1 # ni holds the index for current
            break
        i += 1 #goto L70;
    return ni


#но всегда одинаково, поэтому вынесено в константу, здесь просто, чтобы знать.
def BuildCovariateMat(r8iTox2):
    k = 0
    # index in r8i
    k = 0
    while k < 216:
        # col1: intercept o
        r8iTox2[k][0] = 1.0
        k += 1
    k = 0
    while k < 108:
        # col2: indicator for age
        r8iTox2[k][1] = 0.0
        r8iTox2[108 + k][1] = 1.0
        k += 1
    j = 1
    while j <= 2:
        # col3: age menarchy cate
        k = 1
        while k <= 36:
            r8iTox2[(j - 1) * 108 + k - 1][2] = 0.0
            r8iTox2[(j - 1) * 108 + 36 + k - 1][2] = 1.0
            r8iTox2[(j - 1) * 108 + 72 + k - 1][2] = 2.0
            k += 1
        j += 1
    j = 1
    while j <= 6:
        # col4: # biopsy cate
        k = 1
        while k <= 12:
            r8iTox2[(j - 1) * 36 + k - 1][3] = 0.0
            r8iTox2[(j - 1) * 36 + 12 + k - 1][3] = 1.0
            r8iTox2[(j - 1) * 36 + 24 + k - 1][3] = 2.0
            k += 1
        j += 1
    j = 1
    while j <= 18:
        # col5: age 1st live birt
        k = 1
        while k <= 3:
            r8iTox2[(j - 1) * 12 + k - 1][4] = 0.0
            r8iTox2[(j - 1) * 12 + 3 + k - 1][4] = 1.0
            r8iTox2[(j - 1) * 12 + 6 + k - 1][4] = 2.0
            r8iTox2[(j - 1) * 12 + 9 + k - 1][4] = 3.0
            k += 1
        j += 1
    j = 1
    while j <= 72:
        # col6: # 1st degree re
        r8iTox2[(j - 1) * 3 + 1 - 1][5] = 0.0
        r8iTox2[(j - 1) * 3 + 2 - 1][5] = 1.0
        r8iTox2[(j - 1) * 3 + 3 - 1][5] = 2.0
        j += 1
    i = 0
    while i < 216:
        # col8: age 1st live*# r
        # col7: age*#biop intera
        r8iTox2[i][6] = r8iTox2[i][1] * r8iTox2[i][3]
        r8iTox2[i][7] = r8iTox2[i][4] * r8iTox2[i][5]
        i += 1
    i = 0
    while i < 216:
        #HACK r8iTox2[i + 1727] = 1.0;
        r8iTox2[i][8] = 1.0
        i += 1
    return r8iTox2

def PrintArray(o, Name):
    print("------------------Contents of {}".format(Name))
    for d in o:
        print("{}".format(d))


def PrintArray2(o, Name):
    print("------------------Contents of {}".format(Name))
    print("{")
    i = 0
    while i <=  o.shape[0]:
        print("{")
        j = 0
        while j <= o.shape[0]:
            print("{}, ".format(o[i][j]))
            j += 1
        print("},\n")
        i += 1
    print("}")


