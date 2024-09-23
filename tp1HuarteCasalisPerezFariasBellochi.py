import os 
import getpass
import time
import math
from math import factorial
from datetime import datetime
import random

#----------------------------------------GMENU-------------------------------------#
def logo ():
    print ('''
       \n
        ███  ▐███▌ ███▌    ▐█████      ██████   ████████████████   ██████▄     ██████
        ▀███▄▄███▄███▀     ▐█████      ██████   ████████████████   ████████    ██████
          ▀████████▀       ▐█████      ██████        ██████        █████████▄  ██████
        ██████████████     ▐█████      ██████        ██████        ███████████ ██████
        ▀▀▀▀██████▀▀▀▀     ▐█████      ██████        ██████        ██████ ███████████
         ▄██████████▄      ▐█████▄     ██████        ██████        ██████  ▀█████████
        ████ ▐██▌ ▀███      ▀██████▄▄███████▀        ██████        ██████    ████████
       ▐██▌  ▐██▌  ███▌      ▀████████████▀          ██████        ██████     ▀██████
                                        
                             WELCOME TO UTN PYTHON CAMPUS\n  
       ''')

def mainmenu ():
    print ('''
          THE NATIONAL TECHNOLOGICAL UNIVERSITY (SPANISH: UNIVERSIDAD TECNOLÓGICA
          NACIONAL, UTN) IS A COUNTRY-WIDE NATIONAL UNIVERSITY IN ARGENTINA, AND
             CONSIDERED TO BE AMONG THE TOP ENGINEERING SCHOOLS IN THE COUNTRY.
                   
          PLEASE CHOOSE ONE OPTION:  (1) LOG IN   (2) EXIT PROGRAM  (3) ACTIVATE\n
       ''') 

def exitscreen ():
       print ('''
            ████████████████████████████████████████████████████████████████
            ██                                                            ██
            ██       THANKS FOR USING THE UTN STUDENT MATCH MAKER         ██
            ██                                                            ██
            ████████████████████████████████████████████████████████████████
            ''')

def accessgranted ():
       print ('''
            ████████████████████████████████████████████████████████████████
            ██                                                            ██
            ██                      ACCESS GRANTED                        ██
            ██                                                            ██
            ████████████████████████████████████████████████████████████████
            ''')
       
def accessinvalid ():
       print ('''
            ████████████████████████████████████████████████████████████████
            ██                                                            ██
            ██                      INVALID ACCESS                        ██
            ██                                                            ██
            ████████████████████████████████████████████████████████████████
            ''')

def accessterminated ():
       print ('''
            ████████████████████████████████████████████████████████████████
            ██                                                            ██
            ██        ALL 3 ATTEMPS FAILED. PROGRAM WILL BE CLOSED        ██
            ██                                                            ██
            ████████████████████████████████████████████████████████████████
            ''')

def accessattemp ():
       print ('''
            ████████████████████████████████████████████████████████████████
            ██                                                            ██
                                  YOUR ATTEMP {} FAILED                   
            ██                                                            ██
            ████████████████████████████████████████████████████████████████
            '''.format(failat))

def swelcome ():
       print ('''
            ████████████████████████████████████████████████████████████████
            ██                                                            ██
                                WELCOME: {}
            ██                                                            ██
            ████████████████████████████████████████████████████████████████
            '''.format(students[spos][3]))

def mwelcome ():
       print ('''
            ████████████████████████████████████████████████████████████████
            ██                                                            ██
                                WELCOME: {}
            ██                                                            ██
            ████████████████████████████████████████████████████████████████
            '''.format(moderator[mpos][3]))

def modMen ():
    print ('''
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██    1. MANAGE USERS                                         ██
           ██        a.DEACTIVATE USER                                   ██
           ██        b.RETURN                                            ██
           ██                                                            ██
           ██    2. MANAGE REPORTS                                       ██
           ██        a.CHECK REPORTS                                     ██
           ██        b.BONUS TRACK 1                                     ██
           ██        c.RETURN                                            ██
           ██                                                            ██
           ██    3. STADISTIC REPORTS                                    ██
           ██                                                            ██
           ██    0. EXIT                                                 ██
           ██                                                            ██
           ████████████████████████████████████████████████████████████████
        ''')

def userMen ():
    print ('''
           ████████████████████████████████████████████████████████████████    
           ██                                                            ██
           ██    1. MANAGE PROFILE                                       ██
           ██        a.EDIT MY PERSONAL DATA                             ██
           ██        b.DELETE MY PROFILE                                 ██
           ██        c.RETURN                                            ██
           ██                                                            ██
           ██    2. MANAGE CANDIDATES                                    ██
           ██        a.CHECK CANDIDATES                                  ██
           ██        b.REPORT CANDIDATES                                 ██
           ██        c.RETURN                                            ██
           ██                                                            ██
           ██    3. MATCHING                                             ██
           ██        a.CHECK MATCHES                                     ██
           ██        b.DELETE MATCHIN                                    ██
           ██        c.BONUS TRACK 2                                     ██
           ██        d.RETURN                                            ██
           ██                                                            ██
           ██    4. STADISTIC REPORTS                                    ██
           ██                                                            ██
           ██    5. ROULETTE                                             ██
           ██                                                            ██
           ██    0. EXIT                                                 ██
           ██                                                            ██
           ████████████████████████████████████████████████████████████████
        ''')

def invalidoption ():
    print ('''
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██                      INVALID OPTION                        ██
           ██                                                            ██
           ████████████████████████████████████████████████████████████████
            ''')

def underconstruction ():
    print ('''
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██                     UNDER CONSTRUCTION                     ██
           ██                                                            ██
           ████████████████████████████████████████████████████████████████
            ''')

def ChDataMen ():
    print ('''
           ████████████████████████████████████████████████████████████████    
           ██                                                            ██
           ██    1. DATE OF BIRTH                                        ██
           ██                                                            ██
           ██    2. BIOGRAPHY                                            ██
           ██                                                            ██
           ██    3. HOBBIES                                              ██
           ██                                                            ██
           ██    4. EXIT                                                 ██
           ██                                                            ██
           ████████████████████████████████████████████████████████████████
            ''')

def matchSubMen ():
    print ('''
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██    1. SHOW % OF MATCHES                                    ██
           ██                                                            ██
           ██    2. SHOW LIKES GIVEN TO YOU BUT DIDNT RETURN THE LIKE    ██
           ██                                                            ██
           ██    3. SHOW LIKES GIVEN BY YOU BUT DIDNT RETURN THE LIKE    ██
           ██                                                            ██
           ██    0. EXIT                                                 ██
           ██                                                            ██
           ████████████████████████████████████████████████████████████████
            ''')

def valScreen (case,valid):
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██                    THE {} IS {}                            ██
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            '''.format(case, valid))

def changeData(case):
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██             WOULD YOU LIKE TO UPDATE THE {}?               ██
           ██                                                            ██
           ██                          1.YES                             ██
           ██                                                            ██  
           ██                          2.NO                              ██             
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            '''.format(case))

def currentdate1():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
                        THE CURRENT DATE IS: {}                      
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            '''.format(students[spos][4]))


def enterdays():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
                        ENTER A TWO DIGIT NUMBER FOR DAYS - DD:                       
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            ''')

def entermonth():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
                        ENTER A TWO DIGIT NUMBER FOR MONTH - MM:                       
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            ''')

def enteryear():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
                      ENTER A FOUR DIGIT NUMBER FOR YEAR - YYYY:                       
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            ''')

def enterData(case):
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██      ENTER YOUR {} - NO MORE THAN 255 CHARACTER            ██   
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            '''.format(case))

def long(case):
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██           {} HAS MORE THAN 255 CHARACTERS                  ██   
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            '''.format(case)) 

def current(case):
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██                   THE CURRENT {} IS                        ██
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
        '''.format(case))

def entername():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██                  ENTER NAME AND SURNAME                    ██
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            ''')

def candidatelist():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
                              THE LIST OF STUDENTS IS
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            ''')

def entersexfm():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
                                CHOOSE YOUR SEX: M/F
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            ''')

def candidate():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
                                   {}
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n

                        DATE OF BIRTH:    {}\n

                        AGE:              {}\n

                        SEX:              {}\n

                        BIOGRAPHY:        {}\n

                        HOBBIES:          {}
            '''.format(students[ncand][3],students[ncand][4],students[ncand][5],students[ncand][6],students[ncand][7],students[ncand][8]))

def listofreasons():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
                                LIST OF REASONS
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n

                        REASON 1 IS:    {}\n

                        REASON 2 IS:    {}\n

                        REASON 3 IS:    {}\n

                        REASON 4 IS:    {}\n

                        REASON 5 IS:    {}\n
            '''.format(REASON1,REASON2,REASON3,REASON4,REASON5))

def enterdetails ():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██       ENTER DETAILS (NO MORE THAN 256 CHARACTERS)          ██
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            ''')

def actsucces ():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██                   ACTIVATION SUCCESSFULL                   ██
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            ''')

def nothing ():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██                    NOTHING TO UPDATE                       ██
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            ''')

def contactmod ():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██                    CONTACT MODERATOR                       ██
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            ''')

def showpercentage ():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
                            THE PERCENTAGE IS {} %
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            '''.format(sper))

def lgivennnot ():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
                      LIKES GIVEN AND NOT RETURNED ARE {}
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            '''.format(lgiven))

def lreceivednnot ():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
                     LIKES RECEIVED AND NOT RETURNED ARE {}
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            '''.format(lreceived))


def enternumber ():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██       ENTER THE NUMBER OF THE PROFILE YOU WANT TO VIEW     ██
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            ''')

def enternon ():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██   ENTER THE NUMBER OR FULLNAME OF THE PROFILE TO DELETE    ██
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            ''')

def matchrules ():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██     1) ENTER THE PERSON'S NUMBER YOU WANT TO MATCH         ██
           ██                                                            ██
           ██     2) THE TOTAL PERCENTAGE MUST BE 100%                   ██
           ██                                                            ██
           ██     3) YOU CAN'T CHOOSE YOURSELF                           ██
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            ''')

def onemoreround():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██               WOULD YOU LIKE TO MATCH AGAIN?               ██
           ██                                                            ██
           ██                          1.YES                             ██
           ██                                                            ██
           ██                          2.NO                              ██
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            ''')

def matching():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██     WOULD YOU LIKE TO VIEW A PROFILE IN ORDER TO MATCH?    ██
           ██                                                            ██
           ██                          1.YES                             ██
           ██                                                            ██
           ██                          2.NO                              ██
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            ''')

def matches():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██                 WOULD YOU LIKE TO MATCH?                   ██
           ██                                                            ██
           ██                          1.YES                             ██
           ██                                                            ██
           ██                          2.NO                              ██
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            ''')

def delprofile():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██        ARE YOU SURE YOU WANT TO DELETE THE PROFILE?        ██
           ██                                                            ██
           ██                          1.YES                             ██
           ██                                                            ██
           ██                          2.NO                              ██
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            ''')

def mdelprofile():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██        ARE YOU SURE YOU WANT TO DELETE THE PROFILE?        ██
           ██                                                            ██
           ██                          1.YES                             ██
           ██                                                            ██
           ██                          2.NO                              ██
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            ''')

def updatereports():
    print ('''\n
            ████████████████████████████████████████████████████████████████
            ██                                                            ██
            ██            WOULD YOU LIKE TO UPDATE A REPORT?              ██
            ██                                                            ██
            ██                          1.YES                             ██
            ██                                                            ██
            ██                          2.NO                              ██
            ██                                                            ██
            ████████████████████████████████████████████████████████████████\n
            ''')

def reportsome():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██              IS THERE ANYTHING TO REPORT?                  ██
           ██                                                            ██
           ██                          1.YES                             ██
           ██                                                            ██
           ██                          2.NO                              ██
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            ''')

def updatereports1():
    print ('''\n
            ████████████████████████████████████████████████████████████████
            ██                                                            ██
            ██               WOULD YOU LIKE TO UPDATE TO:                 ██
            ██                                                            ██
            ██               1.TAKEN AND DEADACTIVE USER                  ██
            ██                                                            ██
            ██               2.IGNORE THE USER REPORT                     ██
            ██                                                            ██
            ████████████████████████████████████████████████████████████████\n
            ''')

def nameavailable():
        print (f"\t\t\t  STUDENT 1 IS {NAME1}")
        print (f"\t\t\t  STUDENT 2 IS {NAME2}")
        print (f"\t\t\t  STUDENT 3 IS {NAME3}")
        print (f"\t\t\t  STUDENT 4 IS {NAME4} \n")

def clears ():
    os.system('cls' if os.name == 'nt' else 'clear')

def clearnscreen():
    clears()
    logo()

#------------------------------CONSTANTES------------------------------------#

# DPY: int #
ASTA= "A"
ISTA= "I"
NAME1="RAFAEL DUARTE"
NAME2="GASTON CASALIS"
NAME3="JULIAN PEREZ"
NAME4="FRANCISCO BELLOCHI"
MNAME1="ALFREDO FARIAS"
BIO1="I was born in Ramallo. I have a sister and my father is a vet"
BIO2="I was born in Casilda. I have 8 daughters and 1 son."
BIO3="I was born in Rosario. I see myself as an 80 years old person"
BIO4="I was born in Correa. I love playing games and basket. I'm a big fan of Manu Ginobilli"
HOB1="I like empanadas"
HOB2="I like listening to music"
HOB3="I like cooking pasta"
HOB4="I like playing basketball"
REASON1="BULLYING"
REASON2="AGEIST"
REASON3="STOLEN ACCOUNT"
REASON4="DIDN'T RETURN MY LIKE"
REASON5="OTHER"
DPY = 365

#------------------------------VARIABLES-------------------------------------#
currentdate = datetime.now()

match1=""
match2=""
match3=""

#-------------------------------------ARREGLOS-------------------------------------#

#MATRIZ LIKES#
"""tipo de dato
    TABLE: array [0..8] [0..8] of integer

Variables
A type: TABLE"""

LRT = 8
LCT = 8

likes = [ [""]*LCT for i in range(LRT) ]


#MATRIZ STUDENTS#
"""tipo de dato
    TABLE1: array [0..8] [0..10] of string

 index     0        1          2         3        4     5     6     7       8       9
██████████████████████████████████████████████████████████████████████████████████████████
██    █        █          █          █  NAME   █     █     █     █      █     █          █
██ ID █ACCOUNT █ USERNAME █ PASSWORD █   &     █ DOB █ AGE █ SEX █ BIO  █ HOB █  STATE   █
██    █  TYPE  █          █          █ SURNAME █     █     █     █      █     █          █
██████████████████████████████████████████████████████████████████████████████████████████

Variables
B type: TABLE1"""

SRT = 8
SCT = 10
students = [ [""]*SCT for i in range(SRT) ]


#MATRIZ MODERATOR#
"""tipo de dato
    TABLE1: array [0..8] [0..10] of string

 index     0        1           2          3        4
█████████████████████████████████████████████████████████
██    █        █          █          █  NAME   █        █
██ ID █ACCOUNT █ USERNAME █ PASSWORD █         █ STATE  █
██    █  TYPE  █          █          █ SURNAME █        █
█████████████████████████████████████████████████████████

Variables
C type: TABLE2"""

MRT = 4
MCT = 5
moderator = [ [""]*MCT for i in range(MRT) ]


#MATRIZ REPORTS#
"""tipo de dato
    TABLE1: array [0..8] [0..10] of string

 index     0        1           2          3        4
█████████████████████████████████████████████████████████
██    █          █          █        █         █        █
██ ID █  ISSUED  █ REPORTED █ REASON █ DETAIL  █ STATE  █
██    █          █          █        █         █        █
█████████████████████████████████████████████████████████

Variables
D type: TABLE3"""

RRT = 10
RCT = 7
reports = [ [""]*RCT for i in range(RRT) ]

#-----------------------------------MODULOS DATOS-----------------------------------#

def greetings():
        swelcome()

def mgreetings():
        mwelcome()

def displaybio():
    print (f" {students[spos][7]}")

def biovalidator(BIO):
    if len(BIO) <255:
        return BIO
    else:
        return -1

def displayhob():
    print (f" {students[spos][8]}")

def hobvalidator(HOB):
    if len(HOB) <255:
        return HOB
    else:
        return -1

def seednumber():
    global currentdate, seedn
    cyear = currentdate.year
    cmonth = currentdate.month
    cday = currentdate.day
    csec = currentdate.microsecond
    calc = cyear*cmonth*cday*csec
    seedn = int(str(calc)[:2])
    return seedn

def roulette():
    suma = 0
    while suma != 100:
        clears()
        print("~"*50,"| Roulette |","~"*50)
        print("Deberá ingresar 3 probabilidades que sumen 100")
        probabilidadMatch1 = input("Ingrese la probabilidad de matcheo de la persona A: ")
        if probabilidadMatch1.isnumeric() == True:
            probabilidadMatch1 = int(probabilidadMatch1)
            probabilidadMatch2 = input("Ingrese la probabilidad de matcheo de la persona B: ")
            if probabilidadMatch2.isnumeric() == True:
                probabilidadMatch2 = int(probabilidadMatch2)
                probabilidadMatch3 = input("Ingrese la probabilidad de matcheo de la persona C: ")
                if probabilidadMatch3.isnumeric() == True:
                    probabilidadMatch3 = int(probabilidadMatch3)
                    suma = probabilidadMatch1 + probabilidadMatch2 + probabilidadMatch3
                    if suma != 100:
                        print("Las probabilidades no suman 100, por favor ingrese valores correctos")
                        time.sleep(1)
                else:
                    print("La probabilidad 3 no es un número valido ")
                    time.sleep(1)
            else:
                print("La probabilidad 2 no es un número valido")
                time.sleep(1)
        else: 
            print("La probabilidad 1 no es un número valido ")
            time.sleep(1)
    rng = random.randint(0,100) 
    if rng <= probabilidadMatch1:
        print("Se le matcheó con la persona A")
        time.sleep(1)
    elif rng > probabilidadMatch1 and rng <= probabilidadMatch1+probabilidadMatch2:
        print("Se le matcheó con la persona B")
        time.sleep(1)
    else:
        print("Se le matcheó con la persona C")
        time.sleep(1)

def bonus1():
    edades = [21, 18, 20, 19, 23, 24]
    print("~"*50, "|Bonus track 1|", "~"*50)
    for i in range(len(edades)):
        for j in range(len(edades)):
            if edades[i] < edades[j]:
                aux = edades[j] 
                edades[j] = edades[i]
                edades[i] = aux
    print(edades)
    for i in range(len(edades)-1):
        if int(edades[i]) != int(edades[i+1]) -1:
            print(int(edades[i]) + 1, "es el numero que falta")
            time.sleep(2)

def bonus2():
    print("~"*50, "|Bonus track 2|", "~"*50)
    i= 0
    contador = 0
    for i in range(SRT):
        if (students[i][SCT-1] == ASTA):
                contador += 1
    cant_matcheos = factorial(contador)/ (factorial(2) * factorial(contador - 2))
    print("la cantidad de matcheos posibles es", cant_matcheos)
    time.sleep(2)

def validate_date(D, M, Y):
    if D.isdigit() and M.isdigit() and Y.isdigit():
        dd = int(D)
        mm = int(M)
        year = int(Y)
        if CYEARI < year < CYEARF:
            if 1 <= mm < 13:
                if mm == 2:
                    ddmax = 28
                elif mm in [4, 6, 9, 11]:
                    ddmax = 30
                else:
                    ddmax = 31
                if 1 <= dd <= ddmax:
                    validdate()
                    time.sleep(1)
                    date = str(year) + "-" + str(mm) + "-" + str(dd)
                    dobv = datetime.strptime(date, "%Y-%m-%d").date()
                    return dobv
                else:
                    invaliddate1()
    return -1

def age(DOB):
    age = datetime.now().date() - DOB
    age = math.floor(age.days / DPY)
    age = str(age)
    return age

def rdob():
    rdd = str(random.randint(1,28))
    rmm = str(random.randint(1,12))
    ryear = str(random.randint(CYEARI,CYEARF))
    rdate = str(ryear) + "-" + str(rmm) + "-" + str(rdd)
    rdate = datetime.strptime(rdate, "%Y-%m-%d").date()
    rdate = str(rdate)
    return rdate

def days():
    clears()
    enterdays()
    dd = input("\t\t\t ENTER NUMBER: ")
    return dd

def months():
    clears()
    entermonth()
    mm = input("\t\t\t ENTER NUMBER: ")
    return mm

def years():
    clears()
    enteryear()
    year = input("\t\t\t ENTER NUMBER: ")
    return year

def SHOWCANDIDATES(A, filas, columna, ancho):
    candidatelist()
    i=0
    for i in range (filas):
        if A[i][ancho-1] == ASTA:
            print (f"\t\t\t THE STUDENT {i} IS {students[i][columna]}")

def acandidate (X, filas, columnas):
    i = 0
    lcand = []
    for i in range (filas):
        if X[i][SCT-1] == ASTA:
            save = i
            lcand.append(save)
    return lcand

def LOADLIKES (A, filas, columnas):

    global number
    for i in range (filas):
        for j in range (columnas):
            fnumber = random.random()
            number = round(fnumber * 100)
            if (number % 2) == 1:
                A[i][j] = "1"
            else:
                A[i][j] = "0"

def SLOADBASICINFO(A,filas, columna):
    global ASTA, ISTA, NAME1, NAME2, NAME3, NAME4, BIO1, BIO2, BIO3, BIO4, HOB1, HOB2, HOB3, HOB4
    for i in range (filas):
        for j in range (columna):
            if j == 0:
                A[i][j] = "Student"
            elif j == 1:
                A[i][j] = "estudiante" + str(i+1) + "@ayed.com"
            elif j == 2:
                A[i][j] = str(111222 + 111111*i)
            elif j == 9:
                if (0 <= i < 4):
                    A[i][j] = ASTA
                else:
                    A[i][j] = ISTA
            elif (0 <= i < 4):
                if j == 3:
                    A[i][j] = globals()[f"NAME{i+1}"]
                elif j == 4:
                    A[i][j] = rdob()
                elif j == 5:
                    rage = datetime.now().date() - datetime.strptime(A[i][j-1], "%Y-%m-%d").date()
                    rage = math.floor(rage.days / DPY)
                    A[i][j] = str(rage)
                elif j == 6:
                    A[i][j] = "M"
                elif j == 7:
                    A[i][j] = globals()[f"BIO{i+1}"]
                elif j == 8:
                    A[i][j] = globals()[f"HOB{i+1}"]

def MLOADBASICINFO(A,filas, columna):
    global MNAME1
    for i in range (filas):
        for j in range (columna):
            if j == 0:
                A[i][j] = "Moderator"
            elif j == 1:
                A[i][j] = "estudiante" + str(i+10) + "@ayed.com"
            elif j == 2:
                A[i][j] = str(111111 + 111111*i)
            elif j == 3:
                if i == 0:
                    A[i][j] = globals()[f"MNAME{i+1}"]
            elif j == 4:
                if i == 0:
                    A[i][j] = "A"
                else:
                    A[i][j] = "I"

def RLOADBASICINFO(A,filas, columna):
    global ASTA, ISTA, NAME1, NAME2, NAME3, NAME4, REASON3, REASON4
    for i in range (filas):
        for j in range (columna):
            if  0 <= i <=1:
                if j == 0:
                    A[i][j] = "0"
                elif j == 1:
                    A[i][j] = ASTA
                elif j == 2:
                    k = str(i+1)
                    A[i][j] = k
                elif j == 3:
                    A[i][j] = ASTA
                elif j == 4:
                    A[i][j] = globals()[f"REASON{i+3}"]
                elif j == 5:
                    A[i][j] = ""
                elif j == 6:
                    A[i][j] = "0"

def reportspace(A,filas):
    j = 0
    i = 0
    for i in range (filas):
        if A[i][j] == "":
            return i
    return -1

def reason ():
    global REASON1, REASON2, REASON3, REASON4, REASON5

    i = 0
    clears()
    listofreasons()
    rea = input("\t\t\tENTER NUMBER: ")
    while rea != "1" and rea !="2" and rea != "3" and rea!="4" and rea!="5":
        invalidoption()
        time.sleep(2)
        clears()
        listofreasons()
        rea = input("\t\t\tENTER NUMBER: ")
    clears()
    rea = int (rea)
    rea = globals()[f"REASON{rea}"]
    return rea

def detail():
    clears()
    enterdetails()
    edet = input("\t\t\tENTER DETAILS: ")
    while len(edet) > 256:
        longbio()
        time.sleep(3)
        clears()
        enterdetails()
        edet = input("\t\t\tENTER DETAILS: ")
    return edet

def filler (A, filas, columnas, B, spos, rcand):
    j = 0
    for j in range (columnas):
        if j == 0:
            A[filas][j] = spos
        elif j == 1:
            A[filas][j] = B[spos][9]
        elif j == 2:
            A[filas][j] = rcand
        elif j == 3:
            A[filas][j] = B[rcand][9]
        elif j == 4:
            A[filas][j] = reason()
        elif j == 5:
            A[filas][j] = detail()
        elif j == 6:
            A[filas][j] = "0"

def namesearch (A,filas, name):
    j = 3
    i = 0
    for i in range (filas):
        if A[i][j] == name:
            return i
    return -1

def suservalidator(X, user, passw, R, C):
    i = 0
    j = 1
    while i < R and X[i][j] != user:
        i = 1 + i
    if i < R and X[i][j] == user:
        j = 2
        while i < R and X[i][j] != passw:
            i = 1 + i
        if i < R and X[i][j] == passw and X[i][C-1] == ASTA:
            pos = i
            return pos
    return -1

def muservalidator(X, user, passw, F,C):
    i = 0
    j = 1
    while i < F and X[i][j] != user:
        i = 1 + i
    if i < F and X[i][j] == user:
        j = 2
        while i < F and X[i][j] != passw:
            i = 1 + i
        if i < F and X[i][j] == passw and X[i][C-1] == ASTA:
            pos = i
            return pos
    return -1

def sactivate(X, user, passw, R, C):
    i = 0
    j = 1
    while i < R and X[i][j] != user:
        i = 1 + i
    if i < R and X[i][j] == user:
        j = 2
        while i < R and X[i][j] != passw:
            i = 1 + i
        if i < R and X[i][j] == passw and X[i][C-1] == ISTA:
            pos = i
            return pos
    return -1

def mactivate(X, user, passw, F,C):
    i = 0
    j = 1
    while i < F and X[i][j] != user:
        i = 1 + i
    if i < F and X[i][j] == user:
        j = 2
        while i < F and X[i][j] != passw:
            i = 1 + i
        if i < F and X[i][j] == passw and X[i][C-1] == ISTA:
            pos = i
            return pos
    return -1

def enterdob ():
    ndd = days()
    nmm = months()
    nyear = years()
    ndob = validate_date(ndd, nmm, nyear)
    while ndob == -1:
        clears()
        invalidoption()
        time.sleep(2)
        clears()
        ndd = days()
        nmm = months()
        nyear = years()
        ndob = validate_date(ndd, nmm, nyear)
    ndob = str(ndob)
    clears()
    return ndob

def entersex():
    clears()
    entersexfm()
    sex = input("\t\t\tENTER M/Y SEX:")
    while sex != "M" and sex != "F":
        clears()
        invalidoption()
        time.sleep(2)
        clears()
        entersexfm()
        sex = input("\t\t\tENTER M/Y SEX:")
    clears()
    return sex

def enterbio():
    enterData("BIO")
    ebio = input("\t\t\tENTER BIOGRAPHY:")
    while len(ebio) > 256:
        clears()
        long("BIO")
        time.sleep(2)
        clears()
        ebio = input("\t\t\tENTER BIOGRAPHY:")
    clears()
    return ebio

def enterhob():
    enterData("HOBBY")
    ehob = input("\t\t\tENTER HOBBIE:")
    while len(ehob) > 256:
        clears()
        invalidoption()
        time.sleep(2)
        clears()
        enterData("HOBBY")
        ehob = input("\t\t\tENTER HOBBIE:")
    clears()
    return ehob

def writename():
    entername()
    ename = input("\t\t\tENTER FULLNAME:")
    while len(ename) > 32:
        clears()
        invalidoption()
        time.sleep(2)
        clears()
        entername()
        ename = input("\t\t\tENTER FULLNAME:")
        clears()
    return ename

def SACTINFO(A,filas, columna):
    j = 3
    i = filas
    for j in range (columna):
        if j == 3:
            entername ()
            A[i][j] = str (input("\t\t\tENTER YOUR FULL NAME:"))
        elif j == 4:
            A[i][j] = enterdob()
        elif j == 5:
            rage = datetime.now().date() - datetime.strptime(A[i][j-1], "%Y-%m-%d").date()
            rage = math.floor(rage.days / DPY)
            A[i][j] = str(rage)
        elif j == 6:
            A[i][j] = entersex()
        elif j == 7:
            A[i][j] = enterbio()
        elif j == 8:
            A[i][j] = enterhob()
        elif j == 9:
            A[i][j] = ASTA

def MACTINFO(A,filas):
    i = filas
    clears()
    A[filas][3] = writename()
    A[filas][4] = ASTA

def calmatches(A, columna, pos):
    i = pos
    counter = 1
    for j in range (columna):
        if i != j:
            if A[pos][j] == A[j][pos]:
                counter = counter + 1
    percentage = (counter * 100) // (columna)
    return percentage

def givenlikes(A, columna, pos):
    i = pos
    counter = 1
    for j in range (columna):
        if i != j:
            if A[pos][j] == "1" and A[j][pos] == "0":
                counter = counter + 1
    return counter

def receivedlikes(A, columna, pos):
    i = pos
    counter = 1
    for j in range (columna):
        if i != j:
            if A[pos][j] == "0" and A[j][pos] == "1":
                counter = counter + 1
    return counter

def deadprofile(A, afila, aposicion, X, xfila):
    A[afila][aposicion-1] = ISTA
    i=0
    j=0
    k=2
    for i in range (xfila):
        if X[i][j] == str(afila):
            X[i][j+1] = ISTA
        elif X[i][k] == str(afila):
            X[i][k+1] == ISTA

def showrlist(A, filas):
    i = 0
    j = 0
    for i in range (filas):
        if A[i][j+6] == "0" and A[i][j+1] != ISTA and A[i][j+3] != ISTA:
            print ('''

                ██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████

                REPORT Nro: {}       ISSUED BY: {}  ACTIVITY: {}    STUDENT REPORTED : {}  ACTIVITY: {}   REASON: {}

                STATE: {}  DETAILS: {}

                ██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████

                    '''.format(i, A[i][j], A[i][j+1], A[i][j+2], A[i][j+3], A[i][j+4], A[i][j+6], A[i][j+5]))

def lreports (X, filas, columnas):
    i = 0
    j = 0
    lr = []
    for i in range (filas):
        if X[i][j+6] == "0" and X[i][j+1] != ISTA and X[i][j+3] != ISTA:
            save = i
            lr.append(save)
    return lr

def changendeac(X, filas, Xcolumnas, A, Acolumnas):
    X[filas][Xcolumnas-1] = "1"
    dead = int(X[filas][Xcolumnas-5])
    A[dead][Acolumnas-1] = ISTA

def ignorereport(X, filas, columnas):
    X[filas][columnas-1] = "2"

#-----------------------------------MODULOS PROGRAMA-----------------------------------#

def userMainMenu():
    userMen()
    optUserMaM = input("\t\t\t\t ENTER THE OPTION: ")
    clears()
    while optUserMaM != "0":
        if optUserMaM == "1":
            userMenuManP()
        elif optUserMaM == "2":
            userMenuManC()
        elif optUserMaM == "3":
            userMenuMatch()
        elif optUserMaM == "4":
            clears ()
            userMen()
            underconstruction ()
            time.sleep (2)
        elif optUserMaM == "5":
            roulette()
        elif optUserMaM != "0" and optUserMaM != "1" and optUserMaM != "2" and optUserMaM != "3" and optUserMaM != "4" and optUserMaM != "5":
            clears ()
            userMen()
            invalidoption()
            time.sleep (2)
        if optUserMaM == "0":
            clears()
        else:
            clears()
            userMen()
            optUserMaM = input("\t\t\t\t ENTER THE OPTION: ")

def userMenuManP():
    clears ()
    userMen ()
    optUserManP = input("\t\t\tSUBSELECT AN OPTION FROM MENU 1: ")
    optUserManP = optUserManP.lower()
    while optUserManP != "c":
        if optUserManP == "a":
            userMenuEditData()
        elif optUserManP == "b":
            userDeleteProf()
        elif optUserManP != "a" and optUserManP != "b" and optUserManP != "c":
            clears ()
            userMen ()
            invalidoption()
            time.sleep (2)
        elif optUserManP == "c":
            clears()
        clears ()
        userMen ()
        optUserManP = input("\t\t\tSUBSELECT AN OPTION FROM MENU 1: ")
        optUserManP = optUserManP.lower()

def userMenuEditData():
    clears ()
    ChDataMen ()
    optUserEdiD = input("\t\t\tSELECT AN OPTION TO ADD INFORMATION: ")
    while optUserEdiD != "4":
        if optUserEdiD == "1":
            userEditDate()
        elif optUserEdiD == "2":
            userEditBio()
        elif optUserEdiD == "3":
            userEditHobby()
        elif optUserEdiD == "4":
            clears ()
        clears ()
        ChDataMen ()
        optUserEdiD = input("\t\t\tSELECT AN OPTION TO ADD INFORMATION: ")

def userEditDate():
    clears ()
    currentdate1()
    changeData()
    optUserChDate = input("\t\t\t ENTER THE OPTION:  ")
    while optUserChDate != "2":
        if optUserChDate == "1":
            day = days()
            month = months()
            year = years()
            userDateBirth = validate_date(day, month, year)
            if userDateBirth != -1:
                students[spos][4] = str(userDateBirth)
                students[spos][5] = age(userDateBirth)
            else:
                valScreen("DATE", "INVALID")
                time.sleep(2)
        elif optUserChDate != "1" and optUserChDate != "2":
            clears()
            invalidoption()
            time.sleep(2)
        elif optUserChDate == "2":
            clears()
        clears ()
        currentdate1()
        changeData()
        optUserChDate = input("\t\t\t ENTER THE OPTION:  ")

def userEditBio():
    clears()
    current("BIO")
    displaybio()
    changeData()
    optUserChBio = input("\t\t\t ENTER THE OPTION: ")
    while optUserChBio != "2":
        if optUserChBio == "1":
            clears()
            nbio = enterbio()
            students[spos][7] = nbio
        elif optUserChBio != "1" and optUserChBio !="2":
            invalidoption()
            time.sleep (2)
            clears()
            current("BIO")
            displaybio()
            changeData()
            optUserChBio = input("\t\t\t ENTER THE OPTION: ")

def userEditHobby():
    clears()
    current("HOBBY")
    displayhob()
    changeData()
    optUserChHob = input("\t\t\t ENTER THE OPTION:  ")
    while optUserChHob != "2":
        if optUserChHob == "1":
            clears()
            enterData("HOBBY")
            nhob = input("\t\t\t WRITE YOUR HOBBIES: ")
            nhob = hobvalidator(nhob)
            if nhob != -1:
                students[spos][8] = nhob
            else:
                long("HOBBY")
        elif optUserChHob != "2" and optUserChHob != "1":
            invalidoption()
            time.sleep (2)
        clears()
        current("HOBBY")
        displayhob()
        changeData()
        optUserChHob = input("\t\t\t ENTER THE OPTION:  ")

def userDeleteProf():
    clears ()
    delprofile()
    optUserDelP = input("\t\t\tSELECT AN OPTION FROM MENU: ")
    if optUserDelP == "1":
        deadprofile(students, spos, SCT, reports, RRT)
        clears()
    elif optUserDelP == "2":
        clears()
    else:
        invalidoption()
        time.sleep(2)

def userMenuManC():
    clears ()
    userMen ()
    optUserManC = input("\t\t\tSUBSELECT AN OPTION FROM MENU 2: ")
    optUserManC = optUserManC.lower()
    while optUserManC != "c":
        if optUserManC == "a":
            userCheckCand()
        elif optUserManC == "b":
            userReportCand()
        elif optUserManC != "a" and optUserManC != "b" and optUserManC != "c":
            clears ()
            userMen ()
            invalidoption ()
            time.sleep (2)
        clears ()
        userMen ()
        optUserManC = input("\t\t\tSUBSELECT AN OPTION FROM MENU 2: ")
        optUserManC = optUserManC.lower()

def userCheckCand():
    clears()
    SHOWCANDIDATES(students,SRT,3,SCT)
    matching()
    s_opt212 = input("\n\t\t\t ENTER OPTION: ")
    while s_opt212 != "2":
        if s_opt212 == "1":
            clears()
            SHOWCANDIDATES(students,SRT,3,SCT)
            enternumber()
            alist = acandidate (students, SRT, SCT)
            ncand = input("\n\t\t\t ENTER CANDIDATE NUMBER: ")
            if ncand.isdigit():
                ncand = int(ncand)
                if (ncand in alist) and ncand != spos:
                    clears()
                    candidate()
                    matches()
                    match = input("\t\t\t ENTER OPTION: ")
                    if match == "1":
                        likes[spos][ncand] = 1
                    elif match == "0":
                        likes[spos][ncand] = 0
            else:
                invalidoption()
        if s_opt212 != "1" and s_opt212 == "2":
            clears()
            invalidoption()
        clears()
        SHOWCANDIDATES(students,SRT,3,SCT)
        matching()
        s_opt212 = input("\n\t\t\t ENTER OPTION: ")

def userReportCand():
    clears()
    reportsome()
    optUserRepC = input("\n\t\t\t ENTER OPTION: ")
    while optUserRepC != "2":
        if optUserRepC == "1":
            clears()
            SHOWCANDIDATES(students,SRT,3,SCT)
            rcand = input("\n\t\t WHO DO YOU WANT TO REPORT, CHOOSE NUMBER OR NAME: ")
            rname = namesearch (students, SRT, rcand)
            if rcand.isdigit():
                rcand = int(rcand)
                alist = acandidate (students, SRT, SCT)
                if (rcand in alist) and rcand != spos:
                    clears()
                    rpos = reportspace(reports,RRT)
                    if rpos == -1:
                        contactmod()
                    else:
                        filler(reports, rpos, RCT, students, spos, rcand)
            elif rname != -1 and rname != spos:
                    clears()
                    rpos = reportspace(reports,RRT)
                    if rpos == -1:
                        contactmod()
                    else:
                        filler(reports, rpos, RCT, students, spos, rname)
            else:
                invalidoption()
                time.sleep (2)
        elif optUserRepC != "1" and optUserRepC != "2":
                clears()
                invalidoption()
                time.sleep(2)
        if optUserRepC == "2":
            clears()
        clears()
        reportsome()
        optUserRepC = input("\n\t\t\t ENTER OPTION: ")

def userMenuMatch():
    clears ()
    userMen ()
    optUserMatch = input("\t\t\tSUBSELECT AN OPTION FROM MENU 3: ")
    while optUserMatch != "d":
        if optUserMatch == "a":
            userCheckMatch()
        elif optUserMatch == "b":
            clears ()
            userMen ()
            underconstruction ()
            time.sleep (2)
        elif optUserMatch == "c":
            clears ()
            bonus2()
        elif optUserMatch != "a" and optUserMatch != "b" and optUserMatch != "c" and optUserMatch != "d":
            clears ()
            userMen ()
            invalidoption ()
            time.sleep (2)
        clears ()
        userMen ()
        optUserMatch = input("\t\t\tSUBSELECT AN OPTION FROM MENU 3: ")

def userCheckMatch():
    global sper,lgiven,lreceived
    clears ()
    matchSubMen ()
    optUserCheckM = input("\t\t\t\t   ENTER OPTION: ")
    while optUserCheckM != "0":
        if optUserCheckM == "1":
            clears()
            matchSubMen()
            sper = calmatches (likes, LCT, spos)
            showpercentage()
            time.sleep(2)
        elif optUserCheckM == "2":
            clears()
            matchSubMen()
            lgiven = givenlikes(likes, LCT, spos)
            lgivennnot ()
            time.sleep(2)
        elif optUserCheckM == "3":
            clears()
            matchSubMen()
            lreceived = receivedlikes(likes, LCT, spos)
            lreceivednnot ()
            time.sleep(2)
        elif optUserCheckM != "1" and optUserCheckM != "2" and optUserCheckM != "3":
            invalidoption()
            time.sleep (2)
        clears ()
        matchSubMen ()
        optUserCheckM = input("\t\t\t\t   ENTER OPTION: ")

def modMainMenu():
    modMen()
    optModMaM = input("\t\t\t\t ENTER THE OPTION: ")
    if optModMaM == "0":
        exit = False
        clears()
    while optModMaM != "0":
        if optModMaM == "1":
            modManageUser()
        elif optModMaM == "2":
            modManageRep()
        elif optModMaM != "1" and optModMaM != "2" and optModMaM != "3" and optModMaM != "0":
                clears()
                modMen()
                invalidoption()
                time.sleep(2)
        elif optModMaM == "0":
            exit = False
            clears()
        else:
            clears()
            modMen()
            optModMaM = input("\t\t\t\t ENTER THE OPTION: ")

def modManageUser():
    clears ()
    modMen ()
    s_opt88 = input("\t\t\t\t ENTER THE OPTION: ")
    s_opt88 = s_opt88.lower()
    while s_opt88 != "b":
        if s_opt88 == "a":
            clears()
            SHOWCANDIDATES(students,SRT,3,SCT)
            mdelprofile()
            s_opt888 = input("\n\t\t\t ENTER OPTION: ")
            while s_opt888 != "2":
                if s_opt888 == "1":
                    clears()
                    SHOWCANDIDATES(students,SRT,3,SCT)
                    enternon()
                    alist = acandidate (students, SRT, SCT)
                    rcand = input("\n\t\t WHO DO YOU WANT TO ERASE, CHOOSE NUMBER OR NAME: ")
                    rname = namesearch (students, SRT, rcand)
                    if rcand.isdigit():
                        rcand = int(rcand)
                        alist = acandidate (students, SRT, SCT)
                        if (rcand in alist):
                            clears()
                            deadprofile(students, rcand, SCT, reports, RRT)
                    elif rname != -1 and rname != spos:
                            clears()
                            deadprofile(students, rname, SCT, reports, RRT)
                    else:
                        invalidoption()
                        time.sleep (2)
                if s_opt888 != "1" and s_opt888 == "2":
                    clears()
                    invalidoption()
                clears()
                SHOWCANDIDATES(students,SRT,3,SCT)
                mdelprofile()
                s_opt888 = input("\n\t\t\t ENTER OPTION: ")
        elif s_opt88 != "a" and s_opt88 != "b":
            clears()
            modMen()
            invalidoption()
            time.sleep(2)
        clears ()
        modMen ()
        s_opt88 = input("\t\t\t\t ENTER THE OPTION: ")

def modManageRep():
    clears ()
    modMen ()
    s_opt77 = input("\t\t\t\t ENTER THE OPTION: ")
    s_opt77 = s_opt77.lower()
    while s_opt77 != "c":
        if s_opt77 == "a":
            clears()
            showrlist(reports, RRT)
            rl = lreports (reports, RRT, RCT)
            updatereports()
            uopt = input("\t\t\t ENTER OPTION NUMBER:")
            if uopt == "1" and len(rl) == 0:
                nothing()
                time.sleep(2)
                clears()
            while uopt != "2" and len(rl) !=0:
                if uopt == "1":
                    clears()
                    showrlist(reports, RRT)
                    rl = lreports (reports, RRT, RCT)
                    ropt = input("\t\t\t\t\t\t ENTER THE REPORT NUMBER YOU WANT TO UPDATE:")
                    if ropt.isdigit():
                        ropt = int (ropt)
                        if ropt in rl:
                            clears()
                            showrlist(reports, RRT)
                            updatereports1()
                            aopt = input("\t\t\t ENTER THE ACTION NUMBER:")
                            if aopt ==  "1":
                                changendeac(reports, ropt, RCT, students, SCT)
                            elif aopt == "2":
                                ignorereport(reports, ropt, RCT)
                rl = lreports (reports, RRT, RCT)
                clears()
                showrlist(reports, RRT)
                updatereports()
                uopt = input("\t\t\t ENTER OPTION NUMBER:")
                if uopt == "1" and len(rl) == 0:
                    nothing()
                    time.sleep(2)
                    clears()
        elif s_opt77 == "b":
            clears()
            bonus1()
        elif s_opt77 != "a" and s_opt77 != "b" and s_opt77 != "c":
            clears()
            modMen()
            invalidoption()
            time.sleep(2)
        clears ()
        modMen ()
        s_opt77 = input("\t\t\t\t ENTER THE OPTION: ")


#-------------------------------PROGRAMA--------------------------------------#
CYEAR = int(currentdate.year)
CYEARF = CYEAR - 18
CYEARI = CYEAR - 60
LOADLIKES(likes, LRT, LCT)
SLOADBASICINFO(students, SRT ,SCT)
MLOADBASICINFO(moderator,MRT, MCT)
RLOADBASICINFO(reports, RRT, RCT)

students[0][1] = "1"
students[0][2] = "1"

moderator[0][1] = "2"
moderator[0][2] = "2"

failat = 0
clears()
logo()
mainmenu()
opt = input("\t\t\t\t   ENTER OPTION: ")
clears()
while opt != "2" and failat != 3:
    exit = True
    if opt == "1":
        while exit and failat != 3:
            clearnscreen()
            email = input("\t\t\tENTER USERNAME: ")
            clearnscreen()
            epasw = getpass.getpass(prompt = "\t\t\tENTER PASSWORD:***********", stream=None)
            clears()
            spos = suservalidator(students, email, epasw, SRT, SCT)
            mpos = muservalidator(moderator, email, epasw, MRT, MCT)
            if spos != -1:
                email = 0
                epasw = 0
                failat = 0
                clearnscreen()
                accessgranted()
                clears()
                greetings()
                time.sleep(2)
                clears()
                userMainMenu()
            elif mpos != -1:
                clearnscreen()
                accessgranted()
                clears()
                mgreetings()
                time.sleep(2)
                clears()
                modMainMenu()
            elif email == 0 and epasw == 0:
                clears()
            else:
                failat += 1
                clearnscreen()
                accessinvalid()
                accessattemp()
                time.sleep (2)
                clears()
                if failat == 3:
                    clearnscreen()
                    accessterminated()
                    time.sleep (2)
                    clears ()
    elif opt == "2":
        clearnscreen()
        exitscreen()
        time.sleep (2)
    elif opt == "3":
        clearnscreen()
        email = input("\t\t\tENTER USERNAME: ")
        clearnscreen()
        epasw = getpass.getpass(prompt = "\t\t\tENTER PASSWORD:***********", stream=None)
        clears()
        spos = sactivate(students, email, epasw, SRT, SCT)
        mpos = mactivate(moderator, email, epasw, MRT, MCT)
        if spos != -1:
            email = 0
            epasw = 0
            SACTINFO(students,spos, SCT)
            actsucces ()
            time.sleep(2)
            clears()
        elif mpos != -1:
            MACTINFO(moderator, mpos)
            actsucces ()
            time.sleep(2)
            clears()
        else:
            accessinvalid()
            time.sleep(2)
            clears()
    elif opt != "1" and opt != "2" and opt != "3":
        clearnscreen()
        invalidoption()
        time.sleep(2)
        clears()
    if failat == 3:
        clears()
    else:
        logo()
        mainmenu()
        opt = input("\t\t\t\t   ENTER OPTION: ")
        clears()
