import subnetcalc
import pwdgen


def main():
    while True:
        match menu():
            case 1:
                pwdgen.generate()
            case 2:
                subnetcalc.calculate()
            case 3:
                print(" ", end = "")
                break


def menu():
    val = 0

    while True:
        print("\n1. Generera lösenord\n2. Räkna Subnet\n3. Avsluta")

        try:
            val = int(input("\nVal: "))

            if val not in range(1,4):
                raise ValueError 
                
            else:
                break     

        except ValueError:
            print("\nAnge ett heltal mellan 1-3")
            continue

    return val
 

main()

