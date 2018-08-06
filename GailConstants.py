﻿import numpy as np


NumCovPattInGailModel = 216
rftuned = 0.4
rf50tuned = 0.55
bet2 = np.zeros((8, 12))
bet = np.zeros(8)
rf = np.zeros(2)
abs = np.zeros(216)
rlan = np.zeros(14)
rmu = np.zeros(14)
sumb = np.zeros(216)
sumbb = np.zeros(216)
t = np.zeros(15)
rmu2 = np.zeros((14, 12))
rlan2 = np.zeros((14, 12))
rf2 = np.zeros((2, 13))

## of covariate patterns in GAIL model
# matrix 50
#this is to store beta values
#private double[,] bet2 = new double[8, 3];
#private double[,] rmu2 = new double[14, 6];//[14,6];
#private double[,] rlan2 = new double[14, 6]; //[14,6];[84] #[14,6]; #[14,6];[84] #[12] 


r8iTox2PreCalc = [[1, 0, 0, 0, 0, 0, 0, 0, 1 ],
[1, 0, 0, 0, 0, 1, 0, 0, 1 ],
[1, 0, 0, 0, 0, 2, 0, 0, 1 ],
[1, 0, 0, 0, 1, 0, 0, 0, 1 ],
[1, 0, 0, 0, 1, 1, 0, 1, 1 ],
[1, 0, 0, 0, 1, 2, 0, 2, 1 ],
[1, 0, 0, 0, 2, 0, 0, 0, 1 ],
[1, 0, 0, 0, 2, 1, 0, 2, 1 ],
[1, 0, 0, 0, 2, 2, 0, 4, 1 ],
[1, 0, 0, 0, 3, 0, 0, 0, 1 ],
[1, 0, 0, 0, 3, 1, 0, 3, 1 ],
[1, 0, 0, 0, 3, 2, 0, 6, 1 ],
[1, 0, 0, 1, 0, 0, 0, 0, 1 ],
[1, 0, 0, 1, 0, 1, 0, 0, 1 ],
[1, 0, 0, 1, 0, 2, 0, 0, 1 ],
[1, 0, 0, 1, 1, 0, 0, 0, 1 ],
[1, 0, 0, 1, 1, 1, 0, 1, 1 ],
[1, 0, 0, 1, 1, 2, 0, 2, 1 ],
[1, 0, 0, 1, 2, 0, 0, 0, 1 ],
[1, 0, 0, 1, 2, 1, 0, 2, 1 ],
[1, 0, 0, 1, 2, 2, 0, 4, 1 ],
[1, 0, 0, 1, 3, 0, 0, 0, 1 ],
[1, 0, 0, 1, 3, 1, 0, 3, 1 ],
[1, 0, 0, 1, 3, 2, 0, 6, 1 ],
[1, 0, 0, 2, 0, 0, 0, 0, 1 ],
[1, 0, 0, 2, 0, 1, 0, 0, 1 ],
[1, 0, 0, 2, 0, 2, 0, 0, 1 ],
[1, 0, 0, 2, 1, 0, 0, 0, 1 ],
[1, 0, 0, 2, 1, 1, 0, 1, 1 ],
[1, 0, 0, 2, 1, 2, 0, 2, 1 ],
[1, 0, 0, 2, 2, 0, 0, 0, 1 ],
[1, 0, 0, 2, 2, 1, 0, 2, 1 ],
[1, 0, 0, 2, 2, 2, 0, 4, 1 ],
[1, 0, 0, 2, 3, 0, 0, 0, 1 ],
[1, 0, 0, 2, 3, 1, 0, 3, 1 ],
[1, 0, 0, 2, 3, 2, 0, 6, 1 ],
[1, 0, 1, 0, 0, 0, 0, 0, 1 ],
[1, 0, 1, 0, 0, 1, 0, 0, 1 ],
[1, 0, 1, 0, 0, 2, 0, 0, 1 ],
[1, 0, 1, 0, 1, 0, 0, 0, 1 ],
[1, 0, 1, 0, 1, 1, 0, 1, 1 ],
[1, 0, 1, 0, 1, 2, 0, 2, 1 ],
[1, 0, 1, 0, 2, 0, 0, 0, 1 ],
[1, 0, 1, 0, 2, 1, 0, 2, 1 ],
[1, 0, 1, 0, 2, 2, 0, 4, 1 ],
[1, 0, 1, 0, 3, 0, 0, 0, 1 ],
[1, 0, 1, 0, 3, 1, 0, 3, 1 ],
[1, 0, 1, 0, 3, 2, 0, 6, 1 ],
[1, 0, 1, 1, 0, 0, 0, 0, 1 ],
[1, 0, 1, 1, 0, 1, 0, 0, 1 ],
[1, 0, 1, 1, 0, 2, 0, 0, 1 ],
[1, 0, 1, 1, 1, 0, 0, 0, 1 ],
[1, 0, 1, 1, 1, 1, 0, 1, 1 ],
[1, 0, 1, 1, 1, 2, 0, 2, 1 ],
[1, 0, 1, 1, 2, 0, 0, 0, 1 ],
[1, 0, 1, 1, 2, 1, 0, 2, 1 ],
[1, 0, 1, 1, 2, 2, 0, 4, 1 ],
[1, 0, 1, 1, 3, 0, 0, 0, 1 ],
[1, 0, 1, 1, 3, 1, 0, 3, 1 ],
[1, 0, 1, 1, 3, 2, 0, 6, 1 ],
[1, 0, 1, 2, 0, 0, 0, 0, 1 ],
[1, 0, 1, 2, 0, 1, 0, 0, 1 ],
[1, 0, 1, 2, 0, 2, 0, 0, 1 ],
[1, 0, 1, 2, 1, 0, 0, 0, 1 ],
[1, 0, 1, 2, 1, 1, 0, 1, 1 ],
[1, 0, 1, 2, 1, 2, 0, 2, 1 ],
[1, 0, 1, 2, 2, 0, 0, 0, 1 ],
[1, 0, 1, 2, 2, 1, 0, 2, 1 ],
[1, 0, 1, 2, 2, 2, 0, 4, 1 ],
[1, 0, 1, 2, 3, 0, 0, 0, 1 ],
[1, 0, 1, 2, 3, 1, 0, 3, 1 ],
[1, 0, 1, 2, 3, 2, 0, 6, 1 ],
[1, 0, 2, 0, 0, 0, 0, 0, 1 ],
[1, 0, 2, 0, 0, 1, 0, 0, 1 ],
[1, 0, 2, 0, 0, 2, 0, 0, 1 ],
[1, 0, 2, 0, 1, 0, 0, 0, 1 ],
[1, 0, 2, 0, 1, 1, 0, 1, 1 ],
[1, 0, 2, 0, 1, 2, 0, 2, 1 ],
[1, 0, 2, 0, 2, 0, 0, 0, 1 ],
[1, 0, 2, 0, 2, 1, 0, 2, 1 ],
[1, 0, 2, 0, 2, 2, 0, 4, 1 ],
[1, 0, 2, 0, 3, 0, 0, 0, 1 ],
[1, 0, 2, 0, 3, 1, 0, 3, 1 ],
[1, 0, 2, 0, 3, 2, 0, 6, 1 ],
[1, 0, 2, 1, 0, 0, 0, 0, 1 ],
[1, 0, 2, 1, 0, 1, 0, 0, 1 ],
[1, 0, 2, 1, 0, 2, 0, 0, 1 ],
[1, 0, 2, 1, 1, 0, 0, 0, 1 ],
[1, 0, 2, 1, 1, 1, 0, 1, 1 ],
[1, 0, 2, 1, 1, 2, 0, 2, 1 ],
[1, 0, 2, 1, 2, 0, 0, 0, 1 ],
[1, 0, 2, 1, 2, 1, 0, 2, 1 ],
[1, 0, 2, 1, 2, 2, 0, 4, 1 ],
[1, 0, 2, 1, 3, 0, 0, 0, 1 ],
[1, 0, 2, 1, 3, 1, 0, 3, 1 ],
[1, 0, 2, 1, 3, 2, 0, 6, 1 ],
[1, 0, 2, 2, 0, 0, 0, 0, 1 ],
[1, 0, 2, 2, 0, 1, 0, 0, 1 ],
[1, 0, 2, 2, 0, 2, 0, 0, 1 ],
[1, 0, 2, 2, 1, 0, 0, 0, 1 ],
[1, 0, 2, 2, 1, 1, 0, 1, 1 ],
[1, 0, 2, 2, 1, 2, 0, 2, 1 ],
[1, 0, 2, 2, 2, 0, 0, 0, 1 ],
[1, 0, 2, 2, 2, 1, 0, 2, 1 ],
[1, 0, 2, 2, 2, 2, 0, 4, 1 ],
[1, 0, 2, 2, 3, 0, 0, 0, 1 ],
[1, 0, 2, 2, 3, 1, 0, 3, 1 ],
[1, 0, 2, 2, 3, 2, 0, 6, 1 ],
[1, 1, 0, 0, 0, 0, 0, 0, 1 ],
[1, 1, 0, 0, 0, 1, 0, 0, 1 ],
[1, 1, 0, 0, 0, 2, 0, 0, 1 ],
[1, 1, 0, 0, 1, 0, 0, 0, 1 ],
[1, 1, 0, 0, 1, 1, 0, 1, 1 ],
[1, 1, 0, 0, 1, 2, 0, 2, 1 ],
[1, 1, 0, 0, 2, 0, 0, 0, 1 ],
[1, 1, 0, 0, 2, 1, 0, 2, 1 ],
[1, 1, 0, 0, 2, 2, 0, 4, 1 ],
[1, 1, 0, 0, 3, 0, 0, 0, 1 ],
[1, 1, 0, 0, 3, 1, 0, 3, 1 ],
[1, 1, 0, 0, 3, 2, 0, 6, 1 ],
[1, 1, 0, 1, 0, 0, 1, 0, 1 ],
[1, 1, 0, 1, 0, 1, 1, 0, 1 ],
[1, 1, 0, 1, 0, 2, 1, 0, 1 ],
[1, 1, 0, 1, 1, 0, 1, 0, 1 ],
[1, 1, 0, 1, 1, 1, 1, 1, 1 ],
[1, 1, 0, 1, 1, 2, 1, 2, 1 ],
[1, 1, 0, 1, 2, 0, 1, 0, 1 ],
[1, 1, 0, 1, 2, 1, 1, 2, 1 ],
[1, 1, 0, 1, 2, 2, 1, 4, 1 ],
[1, 1, 0, 1, 3, 0, 1, 0, 1 ],
[1, 1, 0, 1, 3, 1, 1, 3, 1 ],
[1, 1, 0, 1, 3, 2, 1, 6, 1 ],
[1, 1, 0, 2, 0, 0, 2, 0, 1 ],
[1, 1, 0, 2, 0, 1, 2, 0, 1 ],
[1, 1, 0, 2, 0, 2, 2, 0, 1 ],
[1, 1, 0, 2, 1, 0, 2, 0, 1 ],
[1, 1, 0, 2, 1, 1, 2, 1, 1 ],
[1, 1, 0, 2, 1, 2, 2, 2, 1 ],
[1, 1, 0, 2, 2, 0, 2, 0, 1 ],
[1, 1, 0, 2, 2, 1, 2, 2, 1 ],
[1, 1, 0, 2, 2, 2, 2, 4, 1 ],
[1, 1, 0, 2, 3, 0, 2, 0, 1 ],
[1, 1, 0, 2, 3, 1, 2, 3, 1 ],
[1, 1, 0, 2, 3, 2, 2, 6, 1 ],
[1, 1, 1, 0, 0, 0, 0, 0, 1 ],
[1, 1, 1, 0, 0, 1, 0, 0, 1 ],
[1, 1, 1, 0, 0, 2, 0, 0, 1 ],
[1, 1, 1, 0, 1, 0, 0, 0, 1 ],
[1, 1, 1, 0, 1, 1, 0, 1, 1 ],
[1, 1, 1, 0, 1, 2, 0, 2, 1 ],
[1, 1, 1, 0, 2, 0, 0, 0, 1 ],
[1, 1, 1, 0, 2, 1, 0, 2, 1 ],
[1, 1, 1, 0, 2, 2, 0, 4, 1 ],
[1, 1, 1, 0, 3, 0, 0, 0, 1 ],
[1, 1, 1, 0, 3, 1, 0, 3, 1 ],
[1, 1, 1, 0, 3, 2, 0, 6, 1 ],
[1, 1, 1, 1, 0, 0, 1, 0, 1 ],
[1, 1, 1, 1, 0, 1, 1, 0, 1 ],
[1, 1, 1, 1, 0, 2, 1, 0, 1 ],
[1, 1, 1, 1, 1, 0, 1, 0, 1 ],
[1, 1, 1, 1, 1, 1, 1, 1, 1 ],
[1, 1, 1, 1, 1, 2, 1, 2, 1 ],
[1, 1, 1, 1, 2, 0, 1, 0, 1 ],
[1, 1, 1, 1, 2, 1, 1, 2, 1 ],
[1, 1, 1, 1, 2, 2, 1, 4, 1 ],
[1, 1, 1, 1, 3, 0, 1, 0, 1 ],
[1, 1, 1, 1, 3, 1, 1, 3, 1 ],
[1, 1, 1, 1, 3, 2, 1, 6, 1 ],
[1, 1, 1, 2, 0, 0, 2, 0, 1 ],
[1, 1, 1, 2, 0, 1, 2, 0, 1 ],
[1, 1, 1, 2, 0, 2, 2, 0, 1 ],
[1, 1, 1, 2, 1, 0, 2, 0, 1 ],
[1, 1, 1, 2, 1, 1, 2, 1, 1 ],
[1, 1, 1, 2, 1, 2, 2, 2, 1 ],
[1, 1, 1, 2, 2, 0, 2, 0, 1 ],
[1, 1, 1, 2, 2, 1, 2, 2, 1 ],
[1, 1, 1, 2, 2, 2, 2, 4, 1 ],
[1, 1, 1, 2, 3, 0, 2, 0, 1 ],
[1, 1, 1, 2, 3, 1, 2, 3, 1 ],
[1, 1, 1, 2, 3, 2, 2, 6, 1 ],
[1, 1, 2, 0, 0, 0, 0, 0, 1 ],
[1, 1, 2, 0, 0, 1, 0, 0, 1 ],
[1, 1, 2, 0, 0, 2, 0, 0, 1 ],
[1, 1, 2, 0, 1, 0, 0, 0, 1 ],
[1, 1, 2, 0, 1, 1, 0, 1, 1 ],
[1, 1, 2, 0, 1, 2, 0, 2, 1 ],
[1, 1, 2, 0, 2, 0, 0, 0, 1 ],
[1, 1, 2, 0, 2, 1, 0, 2, 1 ],
[1, 1, 2, 0, 2, 2, 0, 4, 1 ],
[1, 1, 2, 0, 3, 0, 0, 0, 1 ],
[1, 1, 2, 0, 3, 1, 0, 3, 1 ],
[1, 1, 2, 0, 3, 2, 0, 6, 1 ],
[1, 1, 2, 1, 0, 0, 1, 0, 1 ],
[1, 1, 2, 1, 0, 1, 1, 0, 1 ],
[1, 1, 2, 1, 0, 2, 1, 0, 1 ],
[1, 1, 2, 1, 1, 0, 1, 0, 1 ],
[1, 1, 2, 1, 1, 1, 1, 1, 1 ],
[1, 1, 2, 1, 1, 2, 1, 2, 1 ],
[1, 1, 2, 1, 2, 0, 1, 0, 1 ],
[1, 1, 2, 1, 2, 1, 1, 2, 1 ],
[1, 1, 2, 1, 2, 2, 1, 4, 1 ],
[1, 1, 2, 1, 3, 0, 1, 0, 1 ],
[1, 1, 2, 1, 3, 1, 1, 3, 1 ],
[1, 1, 2, 1, 3, 2, 1, 6, 1 ],
[1, 1, 2, 2, 0, 0, 2, 0, 1 ],
[1, 1, 2, 2, 0, 1, 2, 0, 1 ],
[1, 1, 2, 2, 0, 2, 2, 0, 1 ],
[1, 1, 2, 2, 1, 0, 2, 0, 1 ],
[1, 1, 2, 2, 1, 1, 2, 1, 1 ],
[1, 1, 2, 2, 1, 2, 2, 2, 1 ],
[1, 1, 2, 2, 2, 0, 2, 0, 1 ],
[1, 1, 2, 2, 2, 1, 2, 2, 1 ],
[1, 1, 2, 2, 2, 2, 2, 4, 1 ],
[1, 1, 2, 2, 3, 0, 2, 0, 1 ],
[1, 1, 2, 2, 3, 1, 2, 3, 1 ],
[1, 1, 2, 2, 3, 2, 2, 6, 1 ]]




def Initialize():
    # age categories boundaries
    t[0] = 20.0
    t[1] = 25.0
    t[2] = 30.0
    t[3] = 35.0
    t[4] = 40.0
    t[5] = 45.0
    t[6] = 50.0
    t[7] = 55.0
    t[8] = 60.0
    t[9] = 65.0
    t[10] = 70.0
    t[11] = 75.0
    t[12] = 80.0
    t[13] = 85.0
    t[14] = 90.0
    # 
    # age specific competing hazards (h2) - BCPT model or STAR model
    # ages [20:25), [25:30), [30:35) .... [70:74), [75:80), [80:85), [85:90)
    #Русская h2 другой расчет через вероятности
    rmu2[0][0] = 98.46063 * 0.00001 # [20:25) race=white,other
    rmu2[1][0] = 165.321023333333 * 0.00001 # [25:30) race=white,other
    rmu2[2][0] = 210.158063333333 * 0.00001 # [30:35) race=white,other
    rmu2[3][0] = 259.971343333333 * 0.00001 # [35:40) race=white,other
    rmu2[4][0] = 330.969866666667 * 0.00001 # [40:45) race=white,other
    rmu2[5][0] = 453.608976666667 * 0.00001 # [45:50) race=white,other
    rmu2[6][0] = 684.431956666667 * 0.00001 # [50:55) race=white,other
    rmu2[7][0] = 1028.54793333333 * 0.00001 # [55:60) race=white,other
    rmu2[8][0] = 1437.97675 * 0.00001 # [60:65) race=white,other
    rmu2[9][0] = 2213.28054 * 0.00001 # [65:70) race=white,other
    rmu2[10][0] = 3737.00936333333 * 0.00001 # [70:75) race=white,other
    rmu2[11][0] = 6078.75755 * 0.00001 # [75:80) race=white,other
    rmu2[12][0] = 8886.43341666666 * 0.00001 # [80:85) race=white,other
    rmu2[13][0] = 12164.01425 * 0.00001 # [85:90) race=white,other
    # 
    # age specific competing hazards (h2) for "average woman"
    # (NCHS mortality 1992:95, excluding death from breast cancer - white, African American)
    # (US   mortality 1990:95, excluding death from breast cancer -     hispanic)
    # ages [20:25), [25:30), [30:35) .... [70:74), [75:80), [80:85), [85:90)
    # 
    #rmu2[0, 3] = 44.12 * 0.00001;         // [20,25) race=white,other 11/21
    #rmu2[1, 3] = 52.54 * 0.00001;         // [24,30) race=white,other
    #rmu2[2, 3] = 67.46 * 0.00001;         // [30,35) race=white,other
    #rmu2[3, 3] = 90.92 * 0.00001;         // [34,40) race=white,other
    #rmu2[4, 3] = 125.34 * 0.00001;         // [40,45) race=white,other
    #rmu2[5, 3] = 195.70 * 0.00001;         // [44,50) race=white,other
    #rmu2[6, 3] = 329.84 * 0.00001;         // [50,55) race=white,other
    #rmu2[7, 3] = 546.22 * 0.00001;         // [54,60) race=white,other
    #rmu2[8, 3] = 910.35 * 0.00001;         // [60,65) race=white,other
    #rmu2[9, 3] = 1418.54 * 0.00001;         // [64,70) race=white,other
    #rmu2[10, 3] = 2259.35 * 0.00001;         // [70,75) race=white,other
    #rmu2[11, 3] = 3611.46 * 0.00001;         // [74,80) race=white,other
    #rmu2[12, 3] = 6136.26 * 0.00001;         // [80,84) race=white,other
    #rmu2[13, 3] = 14206.63 * 0.00001;         // [84,90) race=white,other
    # 
    # age specific breast cancer composite incidence (h1*)
    # ages [20:25), [25:30), [30:35) .... [70:74), [75:80), [80:85), [85:90)


    














    #Русская h1 по статистике. 
    rlan2[0][0] = 0.575863269 * 0.00001 # [20:25) race=white,other
    rlan2[1][0] = 5.185842058 * 0.00001 # [25:30) race=white,other
    rlan2[2][0] = 19.20419941 * 0.00001 # [30:35) race=white,other
    rlan2[3][0] = 36.41587806 * 0.00001 # [35:40) race=white,other
    rlan2[4][0] = 64.84441892 * 0.00001 # [40:45) race=white,other
    rlan2[5][0] = 99.49296199 * 0.00001 # [45:50) race=white,other
    rlan2[6][0] = 123.5385995 * 0.00001 # [50:55) race=white,other
    rlan2[7][0] = 168.5181297 * 0.00001 # [55:60) race=white,other
    rlan2[8][0] = 213.6869914 * 0.00001 # [60:65) race=white,other
    rlan2[9][0] = 230.8909749 * 0.00001 # [65:70) race=white,other
    rlan2[10][0] = 201.1473947 * 0.00001 # [70:75) race=white,other
    rlan2[11][0] = 187.2180714 * 0.00001 # [75:80) race=white,other
    rlan2[12][0] = 163.8033785 * 0.00001 # [80:85) race=white,other
    rlan2[13][0] = 158.129053 * 0.00001 # [85:90) race=white,other
    #rlan2[0, 0] = 2.32007429188145 * 0.00001;        // [20:25) race=white,other        
    #rlan2[1, 0] = 8.58762696340737 * 0.00001;        // [25:30) race=white,other        
    #rlan2[2, 0] = 22.4760697297105 * 0.00001;        // [30:35) race=white,other        
    #rlan2[3, 0] = 40.8191152078653 * 0.00001;        // [35:40) race=white,other        
    #rlan2[4, 0] = 73.1943405959647 * 0.00001;        // [40:45) race=white,other        
    #rlan2[5, 0] = 110.742727775146 * 0.00001;        // [45:50) race=white,other        
    #rlan2[6, 0] = 145.294002396037 * 0.00001;        // [50:55) race=white,other        
    #rlan2[7, 0] = 192.311107556151 * 0.00001;        // [55:60) race=white,other        
    #rlan2[8, 0] = 134.116503746375 * 0.00001;        // [60:65) race=white,other        
    #rlan2[9, 0] = 171.520943759574 * 0.00001;        // [65:70) race=white,other        
    #rlan2[10, 0] = 135.656859996828 * 0.00001;        // [70:75) race=white,other        
    #rlan2[11, 0] = 127.827087087738 * 0.00001;        // [75:80) race=white,other        
    #rlan2[12, 0] = 134.932668167853 * 0.00001;        // [80:85) race=white,other        
    #rlan2[13, 0] = 172.03248235586 * 0.00001;        // [85:90) race=white,other        
    # 
    # age specific breast cancer composite incidence (h1*)-"average woman"
    # (SEER incidence 1992:96 - white, African American)
    # (SEER incidence 1990:96 -     hispanic)
    # ages [20:25), [25:30), [30:35) .... [70:74), [75:80), [80:85), [85:90)
    # 
    #rlan2[0, 3] = 1.22 * 0.00001;       // [20:25) race=white,other 11/21
    #rlan2[1, 3] = 7.41 * 0.00001;       // [25:30) race=white,other
    #rlan2[2, 3] = 22.97 * 0.00001;       // [30:35) race=white,other
    #rlan2[3, 3] = 56.49 * 0.00001;       // [35:40) race=white,other
    #rlan2[4, 3] = 116.45 * 0.00001;       // [40:45) race=white,other
    #rlan2[5, 3] = 195.25 * 0.00001;       // [45:50) race=white,other
    #rlan2[6, 3] = 261.54 * 0.00001;       // [50:55) race=white,other
    #rlan2[7, 3] = 302.79 * 0.00001;       // [55:60) race=white,other
    #rlan2[8, 3] = 367.57 * 0.00001;       // [60:65) race=white,other
    #rlan2[9, 3] = 420.29 * 0.00001;       // [65:70) race=white,other
    #rlan2[10, 3] = 473.08 * 0.00001;       // [70:75) race=white,other
    #rlan2[11, 3] = 494.25 * 0.00001;       // [75:80) race=white,other
    #rlan2[12, 3] = 479.76 * 0.00001;       // [80:85) race=white,other
    #rlan2[13, 3] = 401.06 * 0.00001;       // [85:90) race=white,other
    #11/29/2007 replaced with two dimensional array
    # 
    # bet[0] = -.74948246; // intercept                         1/1
    # bet[1] = .010808072; // age >=50 indicator
    # bet[2] = .0940103059; // age menarchy
    # bet[3] = .5292641686; // # of breast biopsy
    # bet[4] = .2186262218; // age 1st live birth
    # bet[5] = .9583027845; // # 1st degree relatives with breast ca
    # bet[6] = -.288042483; // # breast biopsy * age >=50 indicator
    # bet[7] = -.1908113865; // ** conversion factors (1-attributable risk) used in BCPT model
    # 
    # White & Other women logistic regression coefficients - GAIL model (BCDDP)
    bet2[0][0] = -0.7494824600 # intercept            1/12/99 & 11/13/07
    bet2[1][0] = 0.0108080720 # age >= 50 indicator
    bet2[2][0] = 0.0940103059 # age menarchy
    bet2[3][0] = 0.5292641686 # # of breast biopsy
    bet2[4][0] = 0.2186262218 # age 1st live birth
    bet2[5][0] = 0.9583027845 # # 1st degree relatives with breast ca
    bet2[6][0] = -0.2880424830 # # breast biopsy * age >=50 indicator
    bet2[7][0] = -0.1908113865 # age 1st live birth * # 1st degree rel
    # age 1st live birth * # 1st degree rel
    # conversion factors (1-attributable risk) used in BCPT model
    rf2[0][0] = rftuned # 0.5788413;         // age < 50, race=white,other        1/12/99
    rf2[1][0] = rf50tuned #0.5788413;         // age >=50, race=white,other
    # 11/27/2007 SRamaiah.
    # * Based on Journal(JNCI djm223 LM) published on Dec 05, 2007 by Gail and other scientists,
    # * The new values are being used for african american woman
    # * as there were some major descrenpancies between CARE model and GAIL Model
    # 
    # conversion factors (1-attributable risk) used for "average woman"
    rf2[0][3] = 1.0 # age < 50, race=white avg woman      11/21
    rf2[1][3] = 1.0
# age >=50, race=white avg woman

Initialize()