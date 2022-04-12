#palindromo
lista_pal = []

for i in range(5):
    a = input("Ponga una palabra para saber si es un palindromo: ")
    a = a.lower()
    lista_pal.append(a)

print(" ")

for i in lista_pal:
    palind = i[::-1]
    
    if (palind == i):
        print(f"{i.capitalize()} es una palabra palindroma.")
    else:
        print(f"{i.capitalize()} no es una palabra palíndroma")

#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#contraseña.
print(" ")

usuario = "Gato"
contraseña = "gato12345"


user_ = input("Ponga el usuario: ")
passw_ = input("Ponga su contraseña: ")

print(" ")

if ((usuario != user_)or(contraseña != passw_)):
    print("Contraseña o usuario incorrectos.")
else:
    print("Hola. Buen dia.")

