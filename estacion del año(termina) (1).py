#programa  que te  diga en que estacion del año estas.

hem = input("En que hemisferio vivis?: (N/S): ")
mes = input("En que mes estás?: ")

a1 = hem.upper()
a2 = mes.lower()

trimestres = {
  1 : ["enero", "febrero", "diciembre"],
  2 : ["marzo", "abril", "mayo",],
  3 : ["junio", "julio", "agosto"],
  4 : ["septiembre","octubre","noviembre"]
  }


#hemisferio sur.
if (a1 == "S"):
  trimestres["verano"] = trimestres.pop[1]

  print (trimestres)
  #  for i in trimestreS.values():
  #    print(trimestreS.values())
  #    if trimestreS.values() == mes:
  #      print("La estacion en el mes de", mes, "es: ", trimestreS.values())
  #  