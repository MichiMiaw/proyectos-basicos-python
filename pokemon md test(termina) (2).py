#pokemon md test
import random
import time

tot_score = 0

#naturaleza
serena = 0
docil = 0
rara = 0
audaz = 0
grosera = 0
placida = 0
alegre = 0
miedosa = 0
fuerte = 0
agitada = 0
huraña = 0
activa = 0
osada = 0

print("Test de personalidad Pokémon MD.")
print("")


def random():
    #random
    resp = 0
    num_rand = random.randint(0, 19) 


#preguntas
if (num_rand == 0):
     print("Vas a hacer un examen.¿Cómo te preparas?")
    print("     1- Estudio mucho. ")
    print("     2- El último día. ")
    print("     3- Paso, prefiero jugar ")

    while (resp != 1 and resp != 2 and resp != 3):
        resp = input()

    if (resp == 1):
         fuerte = fuerte + 2
    elif (resp == 2):
        placida = placida + 2    
    elif (resp == 3):
        agitada = agitada + 2


