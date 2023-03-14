import requests
import datetime
import os


def calculate():
    print("\n==== Subnet API =======================")
    
    while True:
        try: 
            addr = str(input("\nAnge nät (med prefix: x.x.x.x/yy): "))
            req = requests.request("GET", " https://networkcalc.com/api/ip/" + addr + "?binary=true")
            data = req.json()
            subnetFull = "" # Sträng där all formaterad data sparas för att kunna skriva allt samtidigt, möjligör mindre loopanvändningar
            
            if req.status_code == 200 and data["status"] == "OK":
                print("\n\n", end = "")

                for i in data["address"]: # Varje fält under addreses (namnet)
                    
                    if i != "binary":
                        value = str(data["address"][i]) # Aktuella fältdatan fast till str
                        subnetFull = subnetFull + subnetData(i, value)    

                    else: # Binary fältet har nested värden så den behöver loopa igenom dem för att skriva ut dem rätt, annars skrivs alla bara ut i json format.
                        subnetFull = subnetFull + "\n"

                        for j in data["address"]["binary"]:
                            value = str(data["address"]["binary"][j])
                            subnetFull = subnetFull + subnetData(j, value)

                print(subnetFull)
                break # Går ur inmatnings whileloopen vid lyckad körning

            elif req.status_code == 400 or data["status"] == "NO_ADDRESS_SPECIFIED":
                print("\nOgiltig address och/eller subnetmask")
                continue

            else:
                raise Exception
        
        except ConnectionError:
            print("\nAnslutningen misslyckades")
            continue
    
    while True:
        try:
            saveFile = str(input("\nVill du spara subnetdatan till en textfil(y/n): "))
            if saveFile not in ["y", "Y", "n", "N"]:
                raise ValueError 
                
            else:
                if saveFile in ["y", "Y"]:
                    try:
                        currentTime = datetime.datetime.now()
                        subnetFile = open("./subnetoutput.txt", "a") #open(os.environ['USERPROFILE'] + "/desktop/subnetoutput.txt", "a")
                        subnetFile.write("\n=======================================\n" + currentTime.strftime("%Y-%m-%d %H:%M:%S") + "\n\n")
                        subnetFile.write(subnetFull)
                        
                        print(f"\nFilen sparad till {os.path.dirname(os.getcwd())}\subnetoutput.txt")
                    
                    except OSError:
                        print("\nGick inte att spara filen")

                    break  

                else:
                    break

        except ValueError:
            print("\nAnge (y/n)")
            continue
    
    print("\n=======================================")


def subnetData(index, value):
    iterations = 0
    temp = index.split("_") # Delar upp "i" till arrayn temp_i vars värden skiljs åt vid _
    full = ""   
  
    for i in temp:         

        if i == "cidr": # CIDR är en akronym där alla bokstäver ska vara stora
            i = i.upper()
        
        else:
            i = i.capitalize()

        if iterations != len(temp) - 1: 
            full = full + i + " "
        
        else:
            full = full + i + ": "

        iterations = iterations + 1

    subnetPair = f"{full:30s} {value:30s}" + "\n"
    return subnetPair