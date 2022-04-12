import random


a = int(input("Ponga un numero para ver si es par o impar: "))

if ((a % 2) == 0):
    print("Es un numero Par.")
else:
    print("Es un numero Impar")

#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
#contador de palabras
print(" ")

b = input("Ponga un texto para saber la cantidad de palabras: ")

palabras = len(b.split())
if (palabras == 1):
    print(f"El texto tiene {palabras} palabra")
else:
    print(f"El texto tiene {palabras} palabras")

#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
#acronimos(siglas)
print(" ")

def quitar_minus(texto):
    awa = []
    for i in texto:
        if (i.isupper()):
            awa.append(i)

    return "".join(awa)

#siglas
c = input("Ponga el nombre de una organizacion o concepto: ")
print(quitar_minus(c))


#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
#piedra papel o tijeras

def pied_pap_tij():
    advers = random.randint(0, 2)
    user = input("Piedra, papel o tijeras?: ")
    user = user.lower()

    eleccion = ["piedra", "papel", "tijeras"]
    e = eleccion[advers]

    print(e)

    if ((user == "piedra" and e == "papel") or (user == "papel" and e == "tijeras") or (user == "tijeras" and e == "piedra")):
        print("El sistema gana.")
    elif((e == "piedra" and user == "papel") or (e == "papel" and user == "tijeras")or (e == "tijeras" and user == "piedra")):
        print("Usted gana.")
    else:
        print("Las 2 son iguales.")
        pied_pap_tij()

        
pied_pap_tij()

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
#adivinar numero oculto
print(" ")

def nro_ocul():
    num = int(input("Adivine el numero oculto: "))
    ocult = random.randint(0, 10)

    if (num == ocult):
        print(" ")
        print("¡Adivinaste el numero!")
        #-------------------------------
    else:
        print(" ")
        print("No adivinaste el numero")
        nro_ocul()


nro_ocul()

#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------

