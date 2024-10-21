import os 
import os.path
import pickle
import getpass
import time
from datetime import datetime
import random

#----------------------------------------GRAPHICS-------------------------------------#
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
                   
          PLEASE CHOOSE ONE OPTION:  (1) REGISTER   (2) LOG IN   (3) EXIT PROGRAM   (4) ACTIVATE\n
       ''') 

def regScreen ():
       print ('''
            ████████████████████████████████████████████████████████████████
            ██                                                            ██
            ██       Select the type of Account  to register:             ██
            ██                                                            ██
            ██       1. STUDENT                                           ██
            ██                                                            ██
            ██       2. MODERATOR                                         ██
            ██                                                            ██
            ██       0. CANCEL                                            ██
            ██                                                            ██
            ████████████████████████████████████████████████████████████████
            ''')

def AdmMen ():
    print ('''
           ████████████████████████████████████████████████████████████████
           ██                                                            ██
           ██    1. MANAGE USERS                                         ██
           ██        a.ELIMINATE USER                                    ██
           ██        b.RETURN                                            ██
           ██                                                            ██
           ██    2. MANAGE REPORTS                                       ██
           ██        a.CHECK REPORTS                                     ██
           ██        b.RETURN                                            ██
           ██                                                            ██
           ██    3. STADISTIC REPORTS                                    ██
           ██                                                            ██
           ██    0. EXIT                                                 ██
           ██                                                            ██
           ████████████████████████████████████████████████████████████████
        ''')

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
           ██        b.RETURN                                            ██
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

def YoN():
    print('''\n
            ████████████████████████████████████████
            ██                                    ██
            ██          1. YES     2. NO          ██
            ██                                    ██
            ████████████████████████████████████████
            ''')


#------------------------------CLASSES------------------------------------#
class User:
    def __init__(self):
        self.userId = 0
        self.userEmail = " ".ljust(32," ")
        self.userName = " ".ljust(32, " ")
        self.userPassword = " ".ljust(32," ")
        self.userState = True
        self.userHobbies = " ".ljust(255," ")
        self.userBiography = " ".ljust(255," ")
        self.userDateBirth = " ".ljust(10," ")

class Mod:
    def __init__(self):
        self.modId = 0
        self.modEmail = " ".ljust(32," ")
        self.modPassword = " ".ljust(32," ")
        self.modState = False

class Admin:
    def __init__(self):
        self.adminId = 0
        self.adminEmail = " ".ljust(32," ")
        self.adminPassword = " ".ljust(32," ")

class Likes:
    def __init__(self):
        self.sender = 0
        self.receiver = 0

#------------------------------Files------------------------------------#
regUser = User()
PFUser = "C:\\ayed\\user.dat"
if os.path.exists(PFUser):
	LFUser= open(PFUser,"r+b")
else:
	LFUser= open(PFUser,"w+b")

regMod = Mod()
PFMod = "C:\\ayed\\mod.dat"
if os.path.exists(PFMod):
	LFMod= open(PFMod,"r+b")
else:
	LFMod= open(PFMod,"w+b")

regAdmin = Admin()
PFAdmin = "C:\\ayed\\admin.dat"
if os.path.exists(PFAdmin):
	LFAdmin= open(PFAdmin,"r+b")
else:
	LFAdmin= open(PFAdmin,"w+b")

regLikes = Likes()
PFLikes = "C:\\ayed\\likes.dat"
if os.path.exists(PFLikes):
	LFLikes= open(PFLikes,"r+b")
else:
	LFLikes= open(PFLikes,"w+b")

#------------------------------VARIABLES-------------------------------------#
currentDate = datetime.now()
currentYear= currentDate.year
fSizeU = os.path.getsize (PFUser)
fSizeM = os.path.getsize (PFMod)
fSizeA= os.path.getsize (PFAdmin)

#------------------------------ADMIN-------------------------------------#
def adminBuilder():
    fSizeA= os.path.getsize (PFAdmin)
    if fSizeA == 0:
        regAdmin.adminId = 0
        regAdmin.adminEmail = "a@gmail.com".ljust(32," ")
        regAdmin.adminPassword = "123".ljust(32," ")
        checkPos("admin")
        pickle.dump(regAdmin, LFAdmin)
        checkPos("admin")
        LFAdmin.flush
        LFAdmin.close

#-----------------------------------MODULES-----------------------------------#
def clears ():
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(2)

def checkPos(userType):
    global LFUser,LFMod,LFAdmin,LFLikes
    if userType ==  "user":
        lastPos = LFUser.tell()
        fSeek = LFUser.seek(lastPos)
        return lastPos
    elif userType == "mod":
        lastPos = LFMod.tell()
        fSeek = LFMod.seek(lastPos)
        return lastPos
    elif userType == "admin":
        lastPos = LFAdmin.tell()
        fSeek = LFAdmin.seek(lastPos)
        return lastPos
    elif userType == "like":
        lastPos = LFLikes.tell()
        fSeek = LFLikes.seek(lastPos)
        return lastPos  

def idSearcher(userType):
    global LFMod,LFUser,fSizeU,fSizeM
    if userType == "user":
        LFUser = open(PFUser,"r+b")
        while LFUser.tell() < fSizeU:
            regUser = pickle.load(LFUser)
            lastId = regUser.userId
            newId = int(lastId)+1
            return newId
    elif userType == "mod":
        LFMod = open(PFMod,"r+b")
        while LFMod.tell() < fSizeM:
            regMod = pickle.load(LFMod)
            lastId = regMod.modId
            newId = int(lastId)+1
            return newId

def searchMandP(email,psw):
    global LFUser,LFMod,LFAdmin,fSizeU,fSizeM,fSizeA,userID
    accExists = 0
    userID = -1
    LFUser = open(PFUser,"r+b")
    LFMod = open(PFMod,"r+b")
    LFAdmin = open(PFAdmin,"r+b")
    LFUser.seek(0)
    LFMod.seek(0)
    LFAdmin.seek(0)
    while LFUser.tell() < fSizeU:
        regUser = pickle.load(LFUser)
        lastEmailU = regUser.userEmail
        lastPswU = regUser.userPassword
        lastIdU = regUser.userId
        if email == lastEmailU and psw == lastPswU:
            accExists = 1
            userID = lastIdU
            return accExists
    while LFMod.tell() < fSizeM:
        regMod = pickle.load(LFMod)
        lastEmailM = regMod.modEmail
        lastPswM = regMod.modPassword
        lastIdM = regMod.modId
        print(lastEmailM,lastPswM)
        if email == lastEmailM and psw == lastPswM:
            accExists = 2
            userID = lastIdM
            return accExists
    while LFAdmin.tell() < fSizeA:
        regAdmin = pickle.load(LFAdmin)
        lastEmailA = regAdmin.adminEmail
        lastPswA = regAdmin.adminPassword
        print(lastEmailA,lastPswA)
        if email == lastEmailA and psw == lastPswA:
            accExists = 3
            return accExists

def searchName(userN):
    global LFUser,LFLikes,fSizeU,userID
    LFUser = open(PFUser,"r+b")
    while LFUser.tell() < fSizeU:
        regUser = pickle.load(LFUser)
        lastId = regUser.userId
        lastName = regUser.userName
        if lastName == userN and lastId == userID:
            return False
        elif userN == lastName:
            LFLikes = open(PFUser,"w+b")
            regLikes.sender = userID
            regLikes.receiver = lastId
            checkPos("like")
            pickle.dump(regLikes, LFLikes)
            checkPos("like")
            LFLikes.flush
            LFLikes.close
            return True
        else:
            return False

def loginPossible():
    LFUser = open(PFUser,"r+b")
    LFMod = open(PFMod,"r+b")
    LFAdmin = open(PFAdmin,"r+b")
    fSizeU = os.path.getsize (PFUser)
    fSizeM = os.path.getsize (PFMod)
    fSizeA= os.path.getsize (PFAdmin)
    lastIdU = 0
    lastIdM = 0
    lastIdA = 0
    while LFUser.tell() < fSizeU:
        regUser = pickle.load(LFUser)
        lastIdU = regUser.userId
    while LFMod.tell() < fSizeM:
        regMod = pickle.load(LFMod)
        lastIdM = regMod.modId
    while LFAdmin.tell() < fSizeA:
        regAdmin = pickle.load(LFAdmin)
        lastIdA = regAdmin.adminId
    if lastIdU >= 1 and lastIdM >= 0 and lastIdA >= 0:
        return True
    else:
        return False

def delUser(ID):
    global LFUser,fSizeU
    LFUser = open(PFUser,"r+b")
    while LFUser.tell() < fSizeU:
        regUser = pickle.load(LFUser)
        lastId = regUser.userId
        if ID == lastId:
            LFUser = open(PFUser,"w+b")
            regUser.state = False
            checkPos("user")
            pickle.dump(regUser, LFUser)
            checkPos("user")
            LFUser.flush
            LFUser.close

def changeModState(modId):
    global LFMod,fSizeM
    LFMod = open(PFMod,"r+b")
    while LFMod.tell() < fSizeM:
        regMod = pickle.load(LFMod)
        lastId = regMod.modId
        if modId == lastId:
            LFMod = open(PFMod,"w+b")
            regMod.state = True
            checkPos("mod")
            pickle.dump(regMod, LFMod)
            checkPos("mod")
            LFMod.flush
            LFMod.close
        else:
            print("MOD NOT FOUND")

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

def bonus1TP2():
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

def bonus2TP2():
    print("~"*50, "|Bonus track 2|", "~"*50)
    ''''
    i= 0
    contador = 0
    for i in range(SRT):
        if (students[i][SCT-1] == ASTA): no funciona porque no se usan arrays
    cant_matcheos = factorial(contador)/ (factorial(2) * factorial(contador - 2))
    print("la cantidad de matcheos posibles es", cant_matcheos)
    time.sleep(2)'''

#-----------------------------------MAIN PROGRAM-----------------------------------#
def regMenu():
    optRegister=" "
    while optRegister != "0":
        clears()
        regScreen ()
        optRegister = input("\t\t\tENTER OPTION: ")
        if optRegister == "1":
            registerUser()
        elif optRegister == "2":
            registerMod()
        elif optRegister == "0":
            print("RETURNING TO MAIN SCREEN")
            time.sleep(2)
        elif optRegister != "1" or optRegister != "2" or optRegister != "0":
            print("THE OPTION YOU CHOSE ISN'T VALID")
            time.sleep(2)

def registerUser():
    global LFUser,PFUser,regUser,fSizeU
    regFlag = False
    clears ()
    print("\t\t\t\t FIELDS CAN'T BE LONGER THAN 32 CHARACTERS")
    while regFlag == False:
        regUser.userName = input("\t\t\t\t ENTER NAME: ")
        regUser.userEmail = input("\t\t\t\t ENTER EMAIL: ")
        regUser.userPassword = input("\t\t\t\t ENTER PASSWORD: ")
        clears ()
        print('''\t\t\t\t ARE YOU SURE THESE FIELDS ARE CORRECT?
            NAME: {}
            EMAIL: {}
            PASSWORD: {}
            '''.format(regUser.userName,regUser.userEmail,regUser.userPassword))
        YoN()
        optRegYoN = input("\t\t\t\t ENTER THE OPTION: ")
        if optRegYoN == "1":
            if len(regUser.userName) > 32 or len(regUser.userEmail) > 32 or len(regUser.userPassword) > 32:
                print("\t\t\t\t FIELD/S LONGER THAN 32 CHARACTERS")
                time.sleep (2)
            elif regUser.userName == "" or regUser.userEmail == "" or regUser.userPassword == "":
                print("\t\t\t\t FIELD/S CAN'T BE BLANK")
            else:
                if checkPos("user") == 0:
                    regUser.userId = 0
                else:
                    regUser.userId = idSearcher("user")
                regUser.userName = regUser.userName.ljust(32)
                regUser.userEmail = regUser.userEmail.ljust(32)
                regUser.userPassword = regUser.userPassword.ljust(32)
                regUser.userState = True
                checkPos("user")
                pickle.dump(regUser, LFUser)
                checkPos("user")
                print("YOU HAVE REGISTERED SUCCESSFULLY")
                regFlag = True
                time.sleep(2)
        else:
            print("\t\t\t\t ENTER FIELDS AGAIN")
    LFUser.flush
    LFUser.close

def registerMod():
    global LFMod,PFMod,regMod,fSizeM
    regFlag = False
    clears()
    print("\t\t\t\t FIELDS CAN'T BE LONGER THAN 32 CHARACTERS")
    while regFlag == False:
        regMod.modEmail = input("\t\t\t\t ENTER EMAIL: ")
        regMod.modPassword = input("\t\t\t\t ENTER PASSWORD: ")
        clears ()
        print('''\t\t\t\t ARE YOU SURE THESE FIELDS ARE CORRECT?
            EMAIL: {}
            PASSWORD: {}
            '''.format(regMod.modEmail,regMod.modPassword))
        YoN()
        optRegYoN = input("\t\t\t\t ENTER THE OPTION: ")
        if optRegYoN == "1":
            if len(regMod.modEmail) > 32 or len(regMod.modPassword) > 32:
                print("\t\t\t\t FIELD/S LONGER THAN 32 CHARACTERS")
                time.sleep (2)
            elif regMod.modEmail == "" or regMod.modPassword == "":
                print("\t\t\t\t FIELD/S CAN'T BE BLANK")
            else:
                if checkPos("mod") == 0:
                    regMod.modId = 0
                else:
                    regMod.modId = idSearcher("user")
                regMod.modEmail = regMod.modEmail.ljust(32)
                regMod.modPassword = regMod.modPassword.ljust(32)
                regMod.modState = True
                checkPos("mod")
                pickle.dump(regMod, LFMod)
                checkPos("mod")
                LFMod.flush
                LFMod.close
                print("YOU HAVE REGISTERED SUCCESSFULLY")
                regFlag = True
                time.sleep(2)
        else:
            print("\t\t\t\t ENTER FIELDS AGAIN")

def login():
    global exit
    clears()
    loginPossible()
    failat = 0
    exit = True
    while exit and failat != 3 and loginPossible() == True:
        email = input("\t\t\tENTER USERNAME: ")
        adjEmail = email.ljust(32)
        pasw = getpass.getpass(prompt = "\t\t\tENTER PASSWORD:***********", stream=None)
        adjPasw = pasw.ljust(32)
        clears()
        usExists = searchMandP(adjEmail,adjPasw)
        if usExists == 1:
            userMainMenu()
        elif usExists == 2:
            modMainMenu()
        elif usExists == 3:
            adminMainMenu()
        else:
            failat += 1
            clears()
            if failat == 3:
                clears()

def userMainMenu():
    global exit
    optUserMaM = " "
    clears()
    while optUserMaM != "0":
        userMen()
        optUserMaM = input("\t\t\t\t ENTER THE OPTION: ")
        if optUserMaM == "1":
            userMenuManP()
        elif optUserMaM == "2":
            userMenuManC()
        elif optUserMaM == "3":
            print("\t\t\t\tUNDER CONSTRUCTION")
        elif optUserMaM == "4":
            print("a")
        elif optUserMaM == "5":
            roulette()
        elif optUserMaM != "0" and optUserMaM != "1" and optUserMaM != "2" and optUserMaM != "3" and optUserMaM != "4" and optUserMaM != "5":
            clears ()
        if optUserMaM == "0":
            clears()
            exit = False

def userMenuManP():
    global userID
    clears ()
    optUserManP = " "
    while optUserManP != "c":
        userMen ()
        optUserManP = input("\t\t\tSUBSELECT AN OPTION FROM MENU 1: ")
        optUserManP = optUserManP.lower()
        if optUserManP == "a":
            userMenuEditData()
        elif optUserManP == "b":
            userDeleteProf(userID)
        elif optUserManP != "a" and optUserManP != "b" and optUserManP != "c":
            clears ()
        elif optUserManP == "c":
            clears()

def userMenuEditData():
    global userID
    clears ()
    optUserEdiD = " "
    while optUserEdiD != "4":
        ChDataMen ()
        optUserEdiD = input("\t\t\tSELECT AN OPTION TO ADD INFORMATION: ")
        if optUserEdiD == "1":
            userEditDate(userID)
        elif optUserEdiD == "2":
            userEditBio(userID)
        elif optUserEdiD == "3":
            userEditHobby(userID)
        elif optUserEdiD == "4":
            clears ()

def userEditDate(ID):
    clears()
    dateFlag = False
    while dateFlag == False:
        newYear = input("\t\t\tENTER YOUR YEAR OF BIRTH: ")
        newMonth = input("\t\t\tENTER YOUR MONTH OF BIRTH: ")
        newDay= input("\t\t\tENTER YOUR DAY OF BIRTH: ")
        if newYear.isnumeric() == True and len(newYear) == 4 and int(newYear) <= 2007 and int(newYear) >= 1914 and newMonth.isnumeric() == True and int(newMonth) >= 1 and int(newMonth) <= 12:
            newYear = datetime.strptime(newYear, "%Y")
            newMonth = datetime.strptime(newMonth, "%m")
            if int(newMonth)<= 7 and int(newMonth) != 2 and int(newMonth) % 2 == 1:
                if newDay.isnumeric() == True and int(newDay) >= 1 and int(newDay) <= 31:
                    newDay = datetime.strptime(newDay, "%d")
                else:
                    print("DAY IS INCORRECT")
                    time.sleep(1)
            elif int(newMonth)<= 7 and int(newMonth) != 2 and int(newMonth) % 2 == 0:
                if newDay.isnumeric() == True and int(newDay) >= 1 and int(newDay) <= 30:
                    newDay = datetime.strptime(newDay, "%d")
                else:
                    print("DAY IS INCORRECT")
                    time.sleep(1)
            elif int(newMonth)>= 8:
                if int(newMonth) % 2 == 1: 
                    if newDay.isnumeric() == True and int(newDay) >= 1 and int(newDay) <= 30:
                        newDay = datetime.strptime(newDay, "%d")
                    else:
                        print("DAY IS INCORRECT")
                        time.sleep(1)
                elif int(newMonth) % 2 == 0:
                    if newDay.isnumeric() == True and int(newDay) >= 1 and int(newDay) <= 31:
                        newDay = datetime.strptime(newDay, "%d")
                    else:
                        print("DAY IS INCORRECT")
                        time.sleep(1)
            elif int(newMonth) == 2 and newDay.isnumeric() == True and int(newDay) >= 1 and int(newDay) <= 28:
                newDay = datetime.strptime(newDay, "%d")
        else:
            print("DAY OR MONTH ARE INCORRECT")
    while LFUser.tell < fSizeU:
        lastId = regUser.userId
        lastDate = regUser.userDateBirth
        if lastId == ID and newYear != " " and newMonth != " " and newDay != " ":
            lastDate = f"{newYear.year}/{newMonth.month}/{newDay.day}"
            checkPos("user")
            pickle.dump(regUser, LFUser)
            checkPos("user")
            LFUser.flush
            LFUser.close

def userEditBio(ID):
    clears()
    newBio = input("\t\t\tENTER YOUR BIOGRAPHY: ")
    while LFUser.tell < fSizeU:
        lastId = regUser.userId
        lastBio = regUser.userBiography
        if lastId == ID:
            lastBio = newBio.ljust(255," ")
            checkPos("user")
            pickle.dump(regUser, LFUser)
            checkPos("user")
            LFUser.flush
            LFUser.close

def userEditHobby(ID):
    global LFUser,fSizeU
    clears()
    newHobby = input("\t\t\tENTER YOUR HOBBIES: ")
    while LFUser.tell < fSizeU:
        lastId = regUser.userId
        lastHobby = regUser.userHobbies
        if lastId == ID:
            lastHobby = newHobby.ljust(255," ")
            checkPos("user")
            pickle.dump(regUser, LFUser)
            checkPos("user")
            LFUser.flush
            LFUser.close

def userDeleteProf(userId):
    clears()
    print("\t\t\t ARE YOU SURE YOU WANT TO DELETE YOUR PROFILE?")
    YoN()
    optUserDelP = input("\t\t\t ENTER THE OPTION: ")
    if optUserDelP == "1":
        delUser(userId)
        print("\t\t\t USER DELETED")
    else:
        clears()

def userMenuManC():
    clears ()
    optUserManC = " "
    while optUserManC != "c":
        userMen ()
        optUserManC = input("\t\t\tSUBSELECT AN OPTION FROM MENU 2: ")
        optUserManC = optUserManC.lower()
        if optUserManC == "a":
            userCheckCand()
        elif optUserManC == "b":
            userReportCand()
        elif optUserManC != "a" and optUserManC != "b" and optUserManC != "c":
            clears ()

def userCheckCand():
    global LFUser,fSizeU
    clears()
    LFUser = open(PFUser,"r+b")
    while LFUser.tell() < fSizeU:
        regUser = pickle.load(LFUser)
        lastName = regUser.userName
        lastHobbies = regUser.userHobbies
        lastBiography = regUser.userBiography
        lastDateBirth = regUser.userDateBirth
        print("\t\t\t NAME:",lastName,"HOBBIES:",lastHobbies,"BIOGRAPHY:",lastBiography,"DATE OF BIRTH:",lastDateBirth)
    print("IS THERE A USER YOU WOULD LIKE TO MATCH WITH?")
    YoN
    optUserLike = input("ENTER THE OPTION: ")
    if optUserLike == "1":
        iLiked = input("ENTER THE NAME OF THE CANDIDATE: ")
        searchName(iLiked)
        if searchName == True:
            print("MATCH SAVED")
            time.sleep(2)
            clears()
        else:
            clears()
    else:
        clears()

def userReportCand():
    clears()

def modMainMenu():
    global exit
    clears()
    optModMaM = " "
    while optModMaM != "0":
        modMen()
        optModMaM = input("\t\t\t\t ENTER THE OPTION: ")
        if optModMaM == "1":
            modManageUser()
        elif optModMaM == "2":
            modManageRep()
        elif optModMaM != "1" and optModMaM != "2" and optModMaM != "3" and optModMaM != "0":
                clears()
        elif optModMaM == "0":
            clears()
            exit = False

def modManageUser():
    clears ()
    optModManU = " "
    while optModManU != "b":
        modMen ()
        optModManU = input("\t\t\t\t ENTER THE OPTION: ")
        optModManU = optModManU.lower()
        if optModManU == "a":
            optModWhoDeact = input("ENTER THE ID OF THE USER YOU WANT TO DEACTIVATE")
            modDeactUser(optModWhoDeact)
        elif optModManU != "a" and optModManU != "b":
            clears()

def modDeactUser(optModWhoDeact):
    clears()
    delUser(optModWhoDeact)

def modManageRep():
    clears ()

def adminMainMenu():
    global exit
    optAdminMaM = " "
    clears()
    while optAdminMaM != "0":
        AdmMen()
        optAdminMaM = input("\t\t\t\t ENTER THE OPTION: ")
        if optAdminMaM == "1":
            adminMenuManU()
        elif optAdminMaM == "2":
            print("UNDER CONSTRUCTION")
        elif optAdminMaM == "3":
            adminStadRep()
        elif optAdminMaM == "0":
            clears()
            exit = False
        elif optAdminMaM != "0" and optAdminMaM != "1" and optAdminMaM != "2" and optAdminMaM != "3":
            clears()

def adminMenuManU():
    clears()
    optAdminManU = " "
    while optAdminManU != "d":
        AdmMen()
        optAdminManU = input("\t\t\tSUBSELECT AN OPTION FROM MENU 2: ")
        optAdminManU = optAdminManU.lower()
        if optAdminManU == "a":
            adminDelU()
        elif optAdminManU == "b":
            modId = input("\t\t\t\t ENTER THE ID OF THE MOD YOU WANT TO CHANGE STATE OF: ")
            adminChangeStateM(modId)
        elif optAdminManU != "c":
            print("UNDER CONSTRUCTION")
        elif optAdminManU != "a" and optAdminManU != "b" and optAdminManU != "c" and optAdminManU != "d":
            clears()

def adminDelU():
    clears()

def adminChangeStateM(modId):
    clears()
    changeModState(modId)

def adminStadRep():
    clears()

adminBuilder()
optMainScreen = " "
clears()
while optMainScreen != "3":
    logo()
    mainmenu()
    optMainScreen = input("\t\t\t\t   ENTER OPTION: ")
    clears()
    if optMainScreen == "1":
        regMenu()
    elif optMainScreen == "2":
        login()
    elif optMainScreen == "3":
        clears()
    elif optMainScreen == "4":
        clears()
    elif optMainScreen != "1" and optMainScreen != "2" and optMainScreen != "3" and optMainScreen == "4":
        clears()