import string
import random
import datetime
import os


def generate():
    print("\n==== Lösenordsgenerator ===============")
    symbols = "!?-_$#%&="
    
    while True:
        try:
            pwdLength = int(input("\nLösenordslängd(8-50 tecken): "))

            if pwdLength not in range(8,51):
                raise ValueError

            else:
                passwords = []
                break     

        except ValueError:
            print("\nAnge ett heltal mellan 8-50")
            continue

    while True:
        try:
            pwdModeChoice = str(input("\nInkludera specialtecken i lösenordet(y/n): "))
            if pwdModeChoice not in ["y", "Y", "n", "N"]:
                raise ValueError
                
            else:
                if pwdModeChoice in ["y", "Y"]:
                    pwdSymbolMode = True
                    break
                
                else:
                    pwdSymbolMode = False
                    break   

        except ValueError:
            print("\nAnge (y/n)")
            continue

    while True:
        try:
            pwdCount = int(input("\nAntal lösenord som ska genereras: "))

            if pwdCount not in range(1,51):
                raise ValueError

            else:
                break     

        except ValueError:
            print("\nAnge ett heltal mellan 1-50")
            continue

    for _ in range(0,pwdCount):
        if pwdSymbolMode == True:
            passwords.append(random.choices(string.ascii_letters + string.digits + symbols, k = pwdLength))
        
        else:
            passwords.append(random.choices(string.ascii_letters + string.digits, k = pwdLength))

    print("\n", end = "")    

    for i in range (len(passwords)):
        passwords[i] = "".join(passwords[i])
        print("\n", passwords[i], end = "", sep = "")
    
    print("\n\n", end = "")    

    while True:
        try:
            saveFile = str(input("\nVill du spara lösenorden till en textfil(y/n): "))
            if saveFile not in ["y", "Y", "n", "N"]:
                raise ValueError 
                
            else:
                if saveFile in ["y", "Y"]:
                    try:
                        currentTime = datetime.datetime.now()
                        pwdFile = open("./passwords.txt", "a")
                        pwdFile.write("\n=======================================\n" + currentTime.strftime("%Y-%m-%d %H:%M:%S") + "\n\n")
                        
                        for i in range (len(passwords)):
                            pwdFile.write(passwords[i] + "\n")
                        
                        print(f"\nFilen sparad till {os.path.dirname(os.getcwd())}\passwords.txt")
                    
                    except OSError:
                        print("\nGick inte att spara filen")

                    break  

                else:
                    break

        except ValueError:
            print("\nAnge (y/n)")
            continue

    print("\n=======================================")