from socket import *
import platform  
from time import gmtime, strftime 
import random 
port = 9000

serverSocket = socket(AF_INET, SOCK_STREAM)

try:
    serverSocket.bind(('',port))
    serverSocket.listen()
    kondita = True
except:
    print("Vetem nje instance e serverit eshte e lejuar!")
    kondita = False
    pass

if kondita:
    print("FIEK TCP Serveri eshte i gatshem...\n")
else:
    print("FIEK TCP Serveri nuk mund te starohet!")

while kondita:
    try:
        connectionSocket, adresa = serverSocket.accept()
        kerkesa = connectionSocket.recv(2048)

        kushti = kerkesa.decode("ASCII")

        socketName = socket.getsockname(connectionSocket)
        print( socketName[0] + ":" + str(socketName[1]) + " Kerkesa " + kushti.split(" ")[0] + " eshte pranuar...")
    except:
        continue
        pass


    if kushti == "IP":
        pergjigja =  "IP adresa e klientit eshte " + socketName[0]
    elif kushti == "PORT":
        pergjigja = "Klienti eshte duke perdorur portin " + str(socketName[1])
    elif kushti[0:6] == "ZANORE":
        if kushti[0:7] == "ZANORE ":
            string = kushti[7:len(kushti)]
            string = string.replace(" ", "")
            numri_zanoreve = 0
            for i in string:
                if i == 'A' or i == 'E' or i == 'U' or i == 'O' or i == 'Y' or i == 'I':
                     numri_zanoreve += 1

            pergjigja = " Teksti derguar permban " + str(numri_zanoreve) + " zanore.  "
        else:
            pergjigja = "Formati: ZANORE [teksti]";
    elif kushti[0:6] == "PRINTO":
        if kushti[0:7] == "PRINTO ":
            pergjigja = kushti[7:len(kushti)].lower().capitalize()
        else:
            pergjigja = "Formati: PRINTO [teksti]";
    elif kushti[0:3] == "MAX":
        if kushti[3:4] == " ":
            kushti = kushti.split(" ")

            num1 = int(kushti[1])
            num2 = int(kushti[2])

            if (num1 > num2):
                pergjigja = kushti[1]
            else:
                pergjigja = kushti[2]
        else:
            pergjigja = "MAX [numri] [numri]"

    elif kushti[0:3] == "MIN":
        if kushti[3:4] == " ":
            kushti = kushti.split(" ")

            num1 = int(kushti[1])
            num2 = int(kushti[2])

            if (num1 < num2):
                pergjigja = kushti[1]
            else:
                pergjigja = kushti[2]
        else:
            pergjigja = "MIN [numri] [numri]"
    elif kushti == "HOST":
        try:
            h = platform.uname()[1]
            pergjigja = "Emri i klientit eshte " + h
        except:
            pergjigja = "Emri i klientit nuk dihet"
    elif kushti == "TIME":
        pergjigja = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    elif kushti == "KENO": 
        array = []
        for i in range(0, 20):
            array.append(random.randint(1,80))
        array.sort()
        pergjigja = str(array)[1:-1]
    elif kushti[0:11] == "NUMERPRIMAR":
        if kushti[11:12] == " ":
            pergjigja = ""
            for i in range(0,int(kushti[12:len(kushti)])):
                if i > 1:
                     for j in range(2,i):
                            if (i % j) == 0:
                            break
                        else:
                        pergjigja += "\n" + str(i)
        else:
            pergjigja = "Formati: NUMERPRIMAR [Numri deri te i cili do te gjenerohen N.P.]"
    elif kushti[0:8] == "CONSTANT":
        if kushti[8:9] == " ":
            if kushti[9:len(kushti)] == "PI":
                pergjigja = str(math.pi)
            elif kushti[9:len(kushti)] == "E":
                pergjigja = str(math.e)
            elif kushti[9:len(kushti)] == "TAU":
                pergjigja = str(math.tau)
            elif kushti[9:len(kushti)] == "SQRT2":
                pergjigja = str(math.sqrt(2))
            elif kushti[9:len(kushti)] == "SQRT3":
                pergjigja = str(math.sqrt(3))
        else:
            pergjigja = "Formati: CONSTANT [KONSTANTA]\n TE NJOHURA: \nPI \n E \n TAU \n SQRT2 \n SQRT3"
    elif kushti[0:8] == "FIZZBUZZ":
        if kushti[8:9] == " ":
            numri = int(kushti[9:len(kushti)])
        if numri % 5 == 0 and numri % 3 == 0:
            pergjigja = "FizzBuzz"
        elif numri % 3 == 0:
            pergjigja = "Fizz"
        elif numri % 5 == 0:
            pergjigja = "Buzz"
        else:
            pergjigja = "Nuk keni japur numer te vlefshem!"
    elif kushti[0:6] == "VALUTA":
        if kushti[6:7] == " ":
            string = kushti.split(" ")
            if string[1] == '1':
                pergjigja = str(round(float(string[2]) * 1.06, 2))
            elif string[1] == '2':
                pergjigja = str(round(float(string[2]) * 0.94, 2))
            elif string[1] == '3':
                pergjigja = str(round(float(string[2]) * 1.07, 2))
            elif string[1] == '4':
                pergjigja = str(round(float(string[2]) * 0.94, 2))
            elif string[1] == '5':
                pergjigja = str(round(float(string[2]) * 0.85, 2))
            elif string[1] == '6':
                pergjigja = str(round(float(string[2]) * 1.18, 2))
        else:
            pergjigja = "Formati: VALUTA [NUMRI I OPERACIONI] [VLERA PER KONVERTIM]"
            pergjigja += "\nZgjedh njerin nga OPERACIONET:"
            pergjigja += "\n1 - EurToUSD"
            pergjigja += "\n2 - USDToEur" 
            pergjigja += "\n3 - EurToCHF" 
            pergjigja += "\n4 - CHFToEur"
            pergjigja += "\n5 - EurToGBP"
            pergjigja += "\n6 - GBPToEur"
        else:
        pergjigja = "Shenoni njeren nga sherbimet tona: IP, PORT, ZANORE, PRINTO, HOST, TIME, KENO, FAKTORIEL, KONVERTO, ARMSTRONG, FIBONNACI."
        
    elif kushti[0:8] == "KONVERTO":
        if kushti[8:9] == " ":
            string = kushti.split(" ")
            if string[1] == '1':
                pergjigja = str(float(string[2]) + 273.15)
            elif string[1] == '2':
                pergjigja = str(float(string[2]) * 1.8 + 32)
            elif string[1] == '3':
                pergjigja = str(float(string[2]) * 9 / 5 - 459.67)
            elif string[1] == '4':
                pergjigja = str(float(string[2]) - 273.15)
            elif string[1] == '5':
                pergjigja = str((float(string[2]) - 32) / 1.8)
            elif string[1] == '6':
                pergjigja = str(float(string[2]) + 459.67)
            elif string[1] == '7':
                pergjigja = str(float(string[2]) / 2.2046)
            elif string[1] == '8':
                pergjigja = str(float(string[2]) * 2.2046)
            else:
                pergjigja = "Shkruaj njerin nga opsionet [ 1 - 8 ]"
        else:
            pergjigja = "Formati: KONVERTO [NUMRI I OPERACIONI] [VLERA PER KONVERTIM]"
            pergjigja += "\nZgjedh njerin nga OPERACIONET:"
            pergjigja += "\n1 - CelsiusToKelvin"
            pergjigja += "\n2 - CelsiusToFahrenheit" 
            pergjigja += "\n3 - KelvinToFahrenheit" 
            pergjigja += "\n4 - KelvinToCelsius"
            pergjigja += "\n5 - FahrenheitToCelsius"
            pergjigja += "\n6 - FahrenheitToKelvin"
            pergjigja += "\n7 - PoundToKilogram"
            pergjigja += "\n8 - KilogramToPound"

    elif kushti[0:9] == "FAKTORIEL":
        if kushti[9:10] == " ":
            pergjigja = str(math.factorial(int(kushti[10:len(kushti)])))
        else:
            pergjigja = "Formati: FAKTORIEL [numri]";

    elif kushti[0:9] == "ARMSTRONG":
        if kushti[9:10] == " ":
            shuma = 0
            i = int(kushti[10:len(kushti)])
            while i>0:
                mod10 = i % 10
                shuma += math.pow(mod10, 3)
                i //= 10
            if shuma == int(kushti[10:len(kushti)]):
                pergjigja = "Numri i dhene eshte numer ARMSTRONG"
            else:
                pergjigja = "Numri i dhene nuk eshte numer ARMSTRONG"
        else:
            pergjigja = "Formati: ARMSTRONG [numri]";

    elif kushti[0:9] =="FIBONNACI":
        ardhshme = 1 
        paraprake = -1
        if kushti[9:10] == " ":
            for i in range(0, int(kushti[10:len(kushti)])):
                shuma = ardhshme + paraprake
                paraprake = ardhshme
                ardhshme = shuma
            pergjigja = str(shuma)
        else:
            pergjigja = "Formati: FIBONNACI [numri]";
    
    elif kushti[0:6] == "SUBNET":
        if kushti[6:7] == " ":

            addr = kushti[7:len(kushti)].split("/")
            ip = addr[0].split(".")
            maska = int(addr[1])
            ipaddr = ipaddress.ip_address(addr[0])
            pergjigja = ""

            classA = ipaddress.IPv4Network(("10.0.0.0", "255.0.0.0"))
            classB = ipaddress.IPv4Network(("172.16.0.0", "255.240.0.0"))
            classC = ipaddress.IPv4Network(("192.168.0.0", "255.255.0.0"))

            if ipaddr in classA:
                addr = ipaddress.IPv4Network(ip[0]+".0.0.0/"+addr[1])
                if maska > 31 or maska < 8:
                    pergjigja = "Netmaska per ip te klases A duhet te jete nga 8 deri ne 31"
            elif ipaddr in classB:
                addr = ipaddress.IPv4Network(ip[0]+"."+ip[1]+".0.0/"+addr[1])
                if maska > 31 or maska < 16:
                    pergjigja = "Netmaska per ip te klases B duhet te jete nga 16 deri ne 31"
            elif ipaddr in classC:
                addr = ipaddress.IPv4Network(ip[0]+"."+ip[1]+".0.0/"+addr[1])
                if maska > 31 or maska < 16:
                    pergjigja = "Netmaska per ip te klases C duhet te jete nga 16 deri ne 31"
            else:
                pergigja = "Shkruani nje ip adres private valide!"


            if pergjigja == "":
                pergjigja = "\nNetwork: " + str(addr.network_address) + "\nNetmask: " + str(addr.netmask) + "\nBroadcast: " + str(addr.broadcast_address)
                pergjigja += "\nHosti Pare: " +  str(addr.network_address+1) + "\nHosti Fundit: " +  str(addr.broadcast_address - 1)
        else:
            pergjigja = "Formati: SUBNET [Adresa Private/Netmaska]"

    elif kushti[0:7] == "IPCLASS":
        if kushti[7:8] == " ":

            classA = ipaddress.IPv4Network(("10.0.0.0", "255.0.0.0"))
            classB = ipaddress.IPv4Network(("172.16.0.0", "255.240.0.0"))
            classC = ipaddress.IPv4Network(("192.168.0.0", "255.255.0.0"))

            ip = ipaddress.IPv4Address(kushti[8:len(kushti)])

            if ip in classA:
                pergjigja = "Klasa A"
            elif ip in classB:
                pergjigja = "Klasa B"
            elif ip in classC:
                pergjigja = "Klasa C"
            else:
                pergjigja = "Nuk keni shenuar ip adres private valide!"
        else:
            pergjigja = "Formati: IPCLASS [IP Adresa Private]"
    
    try:
        connectionSocket.send(pergjigja.encode("ASCII"))
        print( socketName[0] + ":" + str(socketName[1]) + " Pergjigja " + kushti.split(" ")[0] + " eshte derguar...")
    except:
        print(socketName[0] + ":" + str(socketName[1]) + " Pergjigja nuk mund te dergohet!")
        pass        
