#programa  que te  diga en que estacion del año estas.

hem = input("En que hemisferio vivis?: (N/S): ")
mes = input("En que mes estás?: ")

a1 = hem.upper()
a2 = mes.lower()

trimestres = {}

if (a1 == "S"):
    trimestres = {
    "verano" : ["diciembre", "enero", "febrero"],
    "otoño" : ["marzo", "abril", "mayo",],
    "invierno" : ["junio", "julio", "agosto"],
    "primavera" : ["septiembre","octubre","noviembre"]
    }

    

if (a1 == "N"):
    trimestres = {
    "invierno" : [ "diciembre", "enero", "febrero",],
    "primavera" : ["marzo", "abril", "mayo",],
    "verano" : ["junio", "julio", "agosto"],
    "otoño" : ["septiembre","octubre","noviembre"]
    }


estaciones = []
for i, j in trimestres.items():
  
  estaciones.append(i)
  meses = list(j)

  if mes in meses:
    for a in estaciones:
        sumat = len(estaciones) - 1
        print("La estacion en el mes de", mes, "es:", estaciones[sumat])
        print(" ")
        break
        
