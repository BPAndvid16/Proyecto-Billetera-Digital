import callBack as callBack
import os

opcion = 0

def Recibir():

    callBack.call()

def Transferir():
    print()

def BalanceMoneda():
    print()

def BalanceGeneral():
    print()

def Historico():
    print()

while True:
    
    print("---------- Menu ----------")
    print("1. Recibir cantidad")
    print("2. Transferir monto")
    print("3. Mostrar balance una moneda")
    print("4. Mostrar balance general")
    print("5. Mostrar histórico de transacciones")
    print("6. Salir del programa")
    

    opcion = input("Digite una opcion del menu: ")
    opcion = int(opcion)

    if opcion == 6:
        break
    elif opcion == 1:
        monedas=callBack.call()


        print(monedas)

        

print("salio")
    


  