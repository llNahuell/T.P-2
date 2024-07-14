import datetime
import os 
import getpass
import time
import math
from datetime import datetime
#------------------------------CONSTANTES------------------------------------#
ESTUDIANTES=[[""],[""],[""]],[[""],[""],[""]],[[""],[""],[""]],[[""],[""],[""]],[[""],[""],[""]]*4
MODERADORES = [[]], [[]*4 for n in range(4)]
MAIL1="1"
MAIL2="estudiante2@ayed.com"
MAIL3="estudiante3@ayed.com"
MAIL4="estudiante4@ayed.com"
PASW1="1"
PASW2="333444"
PASW3="555666"
PASW4="777888"
NAME1="RAFAEL HUARTE"
NAME2="GASTON CASALIS"
NAME3="JULIAN PEREZ"
NAME4="DOMENICO DI CESARE"
DPY = 365
PER = 100
#------------------------------VARIABLES-------------------------------------#
dob1=""
dob2=""
dob3=""
bio1="I was born in Ramallo. I have a sister and my father is a vet"
bio2="I was born in Casilda. I have 8 daughters and 1 son. I'm 21 years old"
bio3="I was born in Rosario. I see myself as an 80 years old person"
hob1="I like empanadas"
hob2="I like listening to music"
hob3="I like cooking pasta"
age1=""
age2=""
age3=""
match1=""
match2=""
match3=""
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
                   
              PLEASE CHOOSE ONE OPTION:    (1) LOG IN    (2) REGISTER    (3) EXIT PROGRAM\n
       ''') 
    
def sign1():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██             HOW DO YOU WANT TO REGISTER?                   ██
           ██                                                            ██
           ██                          1.STUDENT                         ██
           ██                                                            ██  
           ██                          2.MODERATOR                       ██ ██                                                            ██
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
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
            ██                     YOUR ATTEMP {} FAILED                  ██ 
            ██                                                            ██
            ████████████████████████████████████████████████████████████████
            '''.format(failat))

def welcome1 ():
       print ('''
            ████████████████████████████████████████████████████████████████
            ██                                                            ██
            ██                   WELCOME: {}                              ██
            ██                                                            ██
            ████████████████████████████████████████████████████████████████
            '''.format(NAME1))

def welcome2 ():
       print ('''
            ████████████████████████████████████████████████████████████████
            ██                                                            ██
            ██                   WELCOME: {}                              ██
            ██                                                            ██
            ████████████████████████████████████████████████████████████████
            '''.format(NAME2)) 

def welcome3 ():
       print ('''
            ████████████████████████████████████████████████████████████████
            ██                                                            ██
                                WELCOME: {}
            ██                                                            ██
            ████████████████████████████████████████████████████████████████
            '''.format(NAME3))      

def initialscreen ():
    print ('''
           ████████████████████████████████████████████████████████████████    
           ██                                                            ██
           ██    1. MANAGE PROFILE                                       ██
           ██                                                            ██
           ██    2. MANAGE CANDIDATES                                    ██
           ██                                                            ██
           ██    3. MATCHING                                             ██
           ██                                                            ██
           ██    4. STADISTIC REPORTS                                    ██
           ██                                                            ██
           ██    5. ROULETTE                                             ██
           ██                                                            ██
           ██    0. EXIT                                                 ██
           ██                                                            ██
           ████████████████████████████████████████████████████████████████
        ''')
    
def submenu1 ():
    print ('''
           ████████████████████████████████████████████████████████████████    
           ██                                                            ██
           ██    1. MANAGE PROFILE                                       ██
           ██        a.EDIT MY PERSONAL DATA                             ██
           ██        b.DELETE MY PROFILE                                 ██
           ██        c.RETURN                                            ██
           ██                                                            ██
           ██    2. MANAGE CANDIDATES                                    ██
           ██                                                            ██
           ██    3. MATCHING                                             ██
           ██                                                            ██
           ██    4. STADISTIC REPORTS                                    ██
           ██                                                            ██
           ██    5. ROULETTE                                             ██
           ██                                                            ██
           ██    0. EXIT                                                 ██
           ██                                                            ██
           ████████████████████████████████████████████████████████████████

        ''')

def submenu2 ():    
    print ('''
           ████████████████████████████████████████████████████████████████    
           ██                                                            ██
           ██    1. MANAGE PROFILE                                       ██
           ██                                                            ██
           ██    2. MANAGE CANDIDATES                                    ██
           ██        a.CHECK CANDIDATES                                  ██
           ██        b.REPORT CANDIDATES                                 ██
           ██        c.RETURN                                            ██
           ██                                                            ██
           ██    3. MATCHING                                             ██
           ██                                                            ██
           ██    4. STADISTIC REPORTS                                    ██
           ██                                                            ██
           ██    5. ROULETTE                                             ██
           ██                                                            ██
           ██    0. EXIT                                                 ██
           ██                                                            ██
           ████████████████████████████████████████████████████████████████
        ''')
    
def submenu3 ():
        print ('''
           ████████████████████████████████████████████████████████████████    
           ██                                                            ██
           ██    1. MANAGE PROFILE                                       ██
           ██                                                            ██
           ██    2. MANAGE CANDIDATES                                    ██
           ██                                                            ██
           ██    3. MATCHING                                             ██
           ██        a.CHECK MATCHES                                     ██
           ██        b.DELETE MATCHIN                                    ██
           ██        c.RETURN                                            ██
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
    
def submenu1a ():
    print ('''
           ████████████████████████████████████████████████████████████████    
           ██                                                            ██
           ██    1. DATE OF BIRTH                                        ██
           ██                                                            ██
           ██    2. GENDER                                               ██
           ██                                                            ██
           ██    3. BIOGRAPHY                                            ██
           ██                                                            ██
           ██    4. HOBBIES                                              ██
           ██                                                            ██
           ██    0. EXIT                                                 ██
           ██                                                            ██
           ████████████████████████████████████████████████████████████████
            ''')

def invaliddate ():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██                    THE DATE IS INVALID                     ██
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            ''')
    
def validdate ():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██                     THE DATE IS VALID                      ██
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            ''')
    
def changedate():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██             WOULD YOU LIKE TO UPDATE THE DATE?             ██
           ██                                                            ██
           ██                          1.YES                             ██
           ██                                                            ██  
           ██                          2.NO                              ██             
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            ''')

def changebio():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██           WOULD YOU LIKE TO UPDATE THE BIOGRAPHY?          ██
           ██                                                            ██
           ██                          1.YES                             ██
           ██                                                            ██  
           ██                          2.NO                              ██             
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            ''')

def changehob():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██            WOULD YOU LIKE TO UPDATE THE HOBBIES?           ██
           ██                                                            ██
           ██                          1.YES                             ██
           ██                                                            ██  
           ██                          2.NO                              ██             
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            ''')          

def currentdate1():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
                        THE CURRENT DATE IS: {}                      
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            '''.format(dob1))

def currentdate2():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
                        THE CURRENT DATE IS: {}                      
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            '''.format(dob2))

def currentdate3():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
                        THE CURRENT DATE IS: {}                      
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            '''.format(dob3))      

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

def enterbio():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██      ENTER YOUR BIOGRAPHY - NO MORE THAN 255 CHARACTER     ██   
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            ''')

def longbio():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██           BIOGRAPHY HAS MORE THAN 255 CHARACTERS           ██   
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            ''')

def shortbio():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██           BIOGRAPHY HAS LESS THAN 255 CHARACTERS           ██   
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            ''')            

def enterhob():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██       ENTER YOUR HOBBIES - NO MORE THAN 255 CHARACTER      ██   
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            ''')

def longhob():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██            HOBBIES HAS MORE THAN 255 CHARACTERS            ██   
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            ''')

def shorthob():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██            HOBBIES HAS MORE THAN 255 CHARACTERS            ██   
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            ''')

def candidate1():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
                                  {}                       
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
           
                        DATE OF BIRTH:    {}\n
           
                        AGE:              {}\n
           
                        BIOGRAPHY:        {}\n

                        HOBBIES:          {}\n
            '''.format(NAME1,dob1,age1,bio1,hob1))
    
def candidate2():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
                                   {}                         
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
           
                        DATE OF BIRTH:    {}\n
           
                        AGE:              {}\n
           
                        BIOGRAPHY:        {}\n

                        HOBBIES:          {}\n
            '''.format(NAME2,dob2,age2,bio2,hob2))

def candidate3():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
                                   {}                            
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
           
                        DATE OF BIRTH:    {}\n
           
                        AGE:              {}\n
           
                        BIOGRAPHY:        {}\n

                        HOBBIES:          {}\n         
            '''.format(NAME3,dob3,age3,bio3,hob3))    

def invalidname ():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██                    THE NAME IS INVALID                     ██
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            ''')

def validname ():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██                     THE NAME IS VALID                      ██
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            ''')

def entername0 ():
    print ('''\n
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██       ENTER THE NAME OF THE PERSON YOU WANT TO MATCH       ██
           ██                                                            ██
           ████████████████████████████████████████████████████████████████\n
            ''')


def entername ():
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

def initialmoderatorscreen ():
    print ('''
           ████████████████████████████████████████████████████████████████    
           ██                                                            ██
           ██    1. MANAGE USERS                                         ██
           ██                                                            ██
           ██    2. MANAGE REPORTS                                       ██ 
           ██                                                            ██
           ██    3. STATISTICAL REPORTS                                  ██
           ██                                                            ██
           ██    0. EXIT                                                 ██
           ██                                                            ██
           ████████████████████████████████████████████████████████████████
        ''')

def moderatorsubmenu1 ():
    print ('''
           ████████████████████████████████████████████████████████████████    
           ██                                                            ██
           ██    1. MANAGE USERS                                         ██
           ██        a.DEACTIVATE USER                                   ██
           ██        b.RETURN                                            ██
           ██                                                            ██
           ██    2. MANAGE REPORTS                                       ██
           ██                                                            ██
           ██    3. STATISTICAL REPORTS                                  ██
           ██                                                            ██
           ██    0. EXIT                                                 ██
           ██                                                            ██
           ████████████████████████████████████████████████████████████████

        ''')

def moderatorsubmenu2 ():    
    print ('''
           ████████████████████████████████████████████████████████████████    
           ██                                                            ██
           ██    1. MANAGE USERS                                         ██
           ██                                                            ██
           ██    2. MANAGE REPORTS                                       ██
           ██        a.CHECK REPORTS                                     ██
           ██        b.RETURN                                            ██
           ██                                                            ██
           ██    3. STATISTICAL REPORTS                                  ██
           ██                                                            ██
           ██    0. EXIT                                                 ██
           ██                                                            ██
           ████████████████████████████████████████████████████████████████
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

def invaliddate1():
    invaliddate()
    time.sleep(2)

def invalidopt():
    invalidoption ()
    time.sleep(2)

#-----------------------------------MODULOS-----------------------------------#

def greetings():
    if email == MAIL1:
        welcome1()
        time.sleep (2)
    elif email == MAIL2:
        welcome2()
        time.sleep (2)
    elif email == MAIL3:
        welcome3()
        time.sleep (2)

def displaydob():
    if email == MAIL1:
        currentdate1()
    elif email == MAIL2:
        currentdate2()
    elif email == MAIL3:
        currentdate3()


def validate_date():
    global dob1, dob2, dob3, age1, age2, age3, dd, mm, year

    if dd.isdigit() and mm.isdigit() and year.isdigit():
        dd = int(dd)
        mm = int(mm)
        year = int(year)
        if 1920 < year < 2024:
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
                    date = str(dd) + "-" + str(mm) + "-" + str(year)
                    if email == MAIL1:
                        dob1 = datetime.strptime(date, "%d-%m-%Y").date()
                        age1 = datetime.now().date() - dob1
                        age1 = math.floor(age1.days / DPY)
                    elif email == MAIL2:
                        dob2 = datetime.strptime(date, "%d-%m-%Y").date()
                        age2 = datetime.now().date() - dob2
                        age2 = math.floor(age2.days / DPY)
                    elif email == MAIL3:
                        dob3 = datetime.strptime(date, "%d-%m-%Y").date()
                        age3 = datetime.now().date() - dob3
                        age3 = math.floor(age3.days / DPY)
                else:
                    invaliddate1()
            else:
                invaliddate1()
        else:
            invaliddate1()

def matching ():
    global match1, match2, match3

    exit = True
    while exit:
        if email == MAIL1:
            clears ()
            candidate2()
            candidate3()
            entername0()
            match1 = str(input("\t\t\t ENTER NAME: "))
            match1 = match1.upper()
            if match1 == NAME2 or match1 == NAME3:
                validname()
                time.sleep(2)
                exit = False
            else:
                clears()
                invalidname()
                time.sleep(2)
        elif email == MAIL2:
            clears ()
            candidate1()
            candidate3()
            entername0()
            match2 = str(input("\t\t\t ENTER NAME: "))
            match2 = match2.upper()
            if match2 == NAME1 or match2 == NAME3:
                validname()
                time.sleep(2)
                exit = False
            else:
                clears()
                invalidname()
                time.sleep(2)
        elif email == MAIL3:
            clears ()
            candidate1()
            candidate2()
            entername0()
            match3 = str(input("\t\t\t ENTER NAME: "))
            match3 = match3.upper()
            if match3 == NAME1 or match3 == NAME2:
                validname()
                time.sleep(2)
                exit = False
            else:
                clears()
                invalidname()
                time.sleep(2)

def displaybio():
    if email == MAIL1:
        print (f" THE CURRENT BIOGRAPHY IS {bio1}")
    elif email == MAIL2:
        print (f" THE CURRENT BIOGRAPHY IS {bio2}")
    elif email == MAIL3:
        print (f" THE CURRENT BIOGRAPHY IS {bio3}")

def biovalidator():
    global bio1, bio2, bio3

    if len(bio) <255:
        shortbio()
    if email == MAIL1:
        bio1 = bio
    elif email == MAIL2:
        bio2 = bio
    elif email == MAIL3:
        bio3 = bio
    else:
        longbio()

def displayhob():
    if email == MAIL1:
        print (f" THE CURRENT HOBBIES IS {hob1}")
    elif email == MAIL2:
        print (f" THE CURRENT HOBBIES IS {hob2}")
    elif email == MAIL3:
        print (f" THE CURRENT HOBBIES IS {hob3}")

def hobvalidator():
    global hob1, hob2, hob3

    if len(hob) <255:
        shorthob()
    if email == MAIL1:
            hob1 = hob
    elif email == MAIL2:
            hob2 = hob
    elif email == MAIL3:
            hob3 = hob
    else:
        longhob()

def seednumber():

    global seedn

    currentdate = datetime.datetime.now()
    cyear = currentdate.year
    cmonth = currentdate.month
    cday = currentdate.day
    chour = currentdate.hour
    cmin = currentdate.minute
    csec = currentdate.second
    calc = cyear*cmonth*cday*chour*cmin*csec
    seedn = int(str(calc)[:2])
    return seedn

def roulette():

    mname1 = str(input("\t\t\t ENTER THE NUMBER OF THE STUDENT: "))
    mnum1 = str(input("\t\t\t ENTER AN INTEGER PERCENTAGE FOR MATCHING: "))
    if mname1.isdigit() and mnum1.isdigit():
        mname1 = int(mname1)
        mnum1 = int(mnum1)
        per = PER - mnum1
        if (mname1 != std) and (1 <= mname1 <= 4) and (mnum1 == PER) and (per == 0):
            print (f"\n\t\t\t THE PERSON TO MATCH IS: {mname1}")
            time.sleep(2)
        elif (mname1 != std) and (1 <= mname1 <= 4) and (0 <= mnum1 < 100) and (0 <= per <= 100):
            print (f"\t\t\t THE PERCENTAGE LEFT TO ASSIGN IS:{per}\n")
            mname2 = str(input("\t\t\t ENTER THE NUMBER OF THE STUDENT: "))
            mnum2 = str(input("\t\t\t ENTER AN INTEGER PERCENTAGE FOR MATCHING: "))
            if mname2.isdigit() and mnum2.isdigit():
                mname2 = int(mname2)
                mnum2 = int(mnum2)
                per = per - mnum2
                if (mname2 != std) and (mname2 != mname1) and (1 <= mname2 <= 4) and\
                    (mnum2 == PER) and (per == 0):
                    print (f"\n\t\t\t THE PERSON TO MATCH IS: {mname2}")
                    time.sleep(2)
                elif (mname2 != std) and (mname2 != mname1) and (1 <= mname2 <= 4) and\
                    (0 <= mnum2 < 100) and (0 <= per <= PER):
                    print (f"\t\t\t THE PERCENTAGE LEFT TO ASSIGN IS:{per}\n")
                    mname3 = str(input("\t\t\t ENTER THE NUMBER OF THE STUDENT: "))
                    mnum3 = str(input("\t\t\t ENTER AN INTEGER PERCENTAGE FOR MATCHING: "))
                    if mname3.isdigit() and mnum3.isdigit():
                        mname3 = int(mname3)
                        mnum3 = int(mnum3)
                        per = per - mnum3
                        if (mname3 != std) and (mname3 != mname1 != mname2) and (1 <= mname3 <= 4) and\
                            (mnum3 == PER) and (per == 0):
                            print (f"\n\t\t\t THE PERSON TO MATCH IS: {mname3}")
                            time.sleep(2)
                        elif (mnum1 == 0) and (mnum2 == 0) and (mnum3 == 0):
                            print (f"\n\t\t\t THERE IS NOT A MATCH WITH SOMEONE")
                            time.sleep(2)
                        elif (mname3 != std) and (mname3 != mname1 != mname2) and (1 <= mname3 <= 4) and\
                            (0 <= mnum3 < 100) and (per == 0):
                            rand = seednumber()
                            if (0 < rand <= mnum1):
                                print (f"\n\t\t\t THE PERSON TO MATCH IS: {mname1}")
                                time.sleep(2)
                            elif (mnum1 < rand <= (mnum1+mnum2)):
                                print (f"\n\t\t\t THE PERSON TO MATCH IS: {mname2}")
                                time.sleep(2)
                            elif ((mnum1+mnum2) < rand <= (mnum1+mnum2+mnum3)):
                                print (f"\n\t\t\t THE PERSON TO MATCH IS: {mname3}")
                                time.sleep(2)
                            else:
                                invalidopt()
                        else:
                            invalidopt()
                    else:
                        invalidopt()
                else:
                    invalidopt()
            else:
                invalidopt()
        else:
            invalidopt()
    else:
        invalidopt()



#-------------------------------PROGRAMA--------------------------------------#

failat = 0
opt = ""
while opt != "2" and failat != 3:
    exit1 = True
    clears()
    logo()
    mainmenu()
    opt = str(input("\t\t\t\t   ENTER OPTION: "))
    if opt == "1":
        s_opt = ""
        while s_opt != "0" and failat != 3:
            clearnscreen()
            email = str(input("\t\t\tENTER USERNAME: "))
            clearnscreen()
            epasw = getpass.getpass(prompt = "\t\t\tENTER PASSWORD:***********", stream=None)
            clears()
            if ((email == MAIL1) and (epasw == PASW1)) or\
               ((email == MAIL2) and (epasw == PASW2)) or\
               ((email == MAIL3) and (epasw == PASW3)):
                failat = 0
                username = email
                clearnscreen()
                accessgranted()
                clears()
                greetings()
                while s_opt != "0":
                    clears()
                    initialscreen()
                    s_opt = str(input("\t\t\t\t ENTER THE OPTION: "))
                    if s_opt == "1":
                        s_opt1 = ""
                        while s_opt1 != "c":
                            clears ()
                            submenu1 ()
                            s_opt1 = str(input("\t\t\tSUBSELECT AN OPTION FROM MENU 1: "))
                            s_opt1 = s_opt1.lower()
                            if s_opt1 == "a":
                                s_opt11 = ""
                                while s_opt11 != "4":
                                    clears ()
                                    submenu1a ()
                                    s_opt11 = str(input("\t\t\tSELECT AN OPTION TO ADD INFORMATION: "))
                                    if s_opt11 == "1":
                                        s_opt12 = ""
                                        while s_opt12 != "2":
                                            clears ()
                                            displaydob()
                                            changedate()
                                            s_opt12 = str(input("\t\t\t ENTER THE OPTION:  "))
                                            if s_opt12 == "1":
                                                clears()
                                                enterdays()
                                                dd = input("\t\t\t ENTER NUMBER: ")
                                                clears()
                                                entermonth()
                                                mm = input("\t\t\t ENTER NUMBER: ")
                                                clears()
                                                enteryear()
                                                year = input("\t\t\t ENTER NUMBER: ")
                                                clears()
                                                validate_date()
                                            elif s_opt12 != "1" and s_opt12 != "2":
                                                clears()
                                                invalidoption()
                                                time.sleep(2)
                                    elif s_opt11 == "2":
                                        s_opt21 = ""
                                        while s_opt21 != "2":
                                            clears()
                                            displaybio()
                                            changebio()
                                            s_opt21 = str(input("\t\t\t ENTER THE OPTION: "))
                                            if s_opt21 == "1":
                                                clears()
                                                enterbio()
                                                bio = str(input("\t\t\t WRITE YOUR BIOGRAPHY: "))
                                                biovalidator()
                                            elif s_opt21 != "1" and s_opt21 !="2":
                                                invalidoption()
                                                time.sleep (2)
                                    elif s_opt11 == "3":
                                        s_opt3 = ""
                                        while s_opt3 != "2":
                                            clears()
                                            displayhob()
                                            changehob()
                                            s_opt3 = str(input("\t\t\t ENTER THE OPTION:  "))
                                            if s_opt3 == "1":
                                                clears()
                                                enterhob()
                                                hob = str(input("\t\t\t WRITE YOUR HOBBIES: "))
                                                hobvalidator()
                                            elif s_opt3 != "2" and s_opt3 != "1":
                                                invalidoption()
                                                time.sleep (2)
                            elif s_opt1 == "b":
                                clears ()
                                submenu1 ()
                                underconstruction ()
                                time.sleep (2)
                            elif s_opt1 != "a" and s_opt1 != "b" and s_opt1 != "c":
                                clears ()
                                submenu1 ()
                                invalidoption()
                                time.sleep (2)                                   
                    elif s_opt == "2":
                        s_opt21 = ""
                        while s_opt21 != "c":
                            clears ()
                            submenu2 ()
                            s_opt21 = str(input("\t\t\tSUBSELECT AN OPTION FROM MENU 2: "))
                            s_opt21 = s_opt21.lower()
                            if s_opt21 == "a":
                                matching ()
                            elif s_opt21 == "b":
                                clears ()
                                submenu2 ()
                                underconstruction ()
                                time.sleep (2)
                            elif s_opt21 != "a" and s_opt21 != "b" and s_opt21 != "c":
                                clears ()
                                submenu2 ()
                                invalidoption ()
                                time.sleep (2)
                    elif s_opt == "3":
                        s_opt32 = ""
                        while s_opt32 != "c":
                            clears ()
                            submenu3 ()
                            s_opt32 = str(input("\t\t\tSUBSELECT AN OPTION FROM MENU 3: "))
                            if s_opt32 == "a":
                                clears ()
                                submenu3 ()
                                underconstruction ()
                                time.sleep (2)
                            elif s_opt32 == "b":
                                clears ()
                                submenu3 ()
                                underconstruction ()
                                time.sleep (2)
                            elif s_opt32 != "a" and s_opt32 != "b" and s_opt32 != "c":
                                clears ()
                                submenu3 ()
                                invalidoption ()
                                time.sleep (2)              
                    elif s_opt == "4":
                                clears ()
                                initialscreen()
                                underconstruction ()
                                time.sleep (2)
                    elif s_opt == "5":
                                s_opt5 = ""
                                while s_opt5 != "2":
                                    clears ()
                                    entername()
                                    seednumber()
                                    nameavailable()
                                    if (email == MAIL1):
                                        std = 1
                                        roulette()
                                    elif (email == MAIL2):
                                        std = 2
                                        roulette()
                                    elif (email == MAIL3):
                                        std = 3
                                        roulette()
                                    clears()
                                    onemoreround()
                                    s_opt5 = str(input("\t\t\tSELECT AN OPTION FROM MENU: "))
                                    if s_opt5 == "2":
                                        clears()
                                    elif s_opt5 == "1":
                                        clears()
                                    elif s_opt5 != "1" and s_opt5 != "2":
                                        invalidoption()
                    elif s_opt != "0" and s_opt != "1" and s_opt != "2" and s_opt != "3" and s_opt != "4" and s_opt != "5":
                                clears ()
                                initialscreen()
                                invalidoption()
                                time.sleep (2)
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
        P
    elif opt == "3":
        clearnscreen()
        exitscreen()
        time.sleep (2)
        clears()
    elif opt != "1" and opt != "2":
        clearnscreen()
        invalidoption()
        time.sleep (2)
        clears()
