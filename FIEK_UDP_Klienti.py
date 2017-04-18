from socket import *

server = "localhost"
port = 9000

print("Per te zgjedhur sherbimin shkruani fjalet:")
print("IP, PORT, PRINTO, HOST, TIME, ZANORE, KENO, FAKTORIEL, KONVERTO ARMSTRONG, FIBONNACI, MAX, MIN, SUBNET, IPCLASS, FIZZBUZZ, VALUTA, CONSTANT dhe NUMERPRIMAR\n")

try:
    clientSocket = socket(AF_INET, SOCK_DGRAM)
except socket.error:
    print ('Problem ne krijimin e soketes')
pass

while True:
       
    kerkesa = input("Kerkesa: ").upper()
    clientSocket.sendto(kerkesa.encode("ASCII"), (server, port))

    while kerkesa == "":
        print("IP, PORT, PRINTO, HOST, TIME, ZANORE, KENO, FAKTORIEL, KONVERTO ARMSTRONG, FIBONNACI, MAX, MIN, SUBNET, IPCLASS, FIZZBUZZ, VALUTA, CONSTANT dhe NUMERPRIMAR")
        kerkesa = input("Kerkesa: ").upper()
        
    try:
        pergjigja, adresa = clientSocket.recvfrom(2048)
        print("Pergjigja: " + pergjigja.decode("ASCII"))
    except:
            print("Kerkesa nuk mund te dergohet!")
    pass

clientSocket.close()
