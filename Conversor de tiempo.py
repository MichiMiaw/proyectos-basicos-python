#Conversor de minutos a horas
from encodings import utf_8
import tkinter
import time
from tkinter import messagebox

utf_8
vent = tkinter.Tk()
vent.geometry("400x400")
vent.title("Conversor de tiempo")
vent.resizable(False, False)

frem = tkinter.Frame(vent, bg = "#06283D")
frem.pack(expand = True, fill = "both")

labl = tkinter.Label(vent, fg = "light gray", bg = "#06283D", text = "Conversor de tiempo", font = "MSSansSerif 25") 
labl.place(x = 200, y = 30, anchor = tkinter.CENTER)

a = tkinter.Label(vent, fg = "light gray", bg = "#06283D", text = "A", font = "MSSansSerif 25")
a.place(x = 200, y = 200, anchor = tkinter.CENTER)
##-----------------------------------------------------------------------------------------
#lista de opciones
opciones = ["Años", "Meses", "Semanas", "Dias", "Horas", "Minutos", "Segundos"]

def option_selected(value):
    callbackchoice = value.get()
    return (str(callbackchoice))
# Variable to keep track of the option
# selected in OptionMenu
value_inside = tkinter.StringVar(vent)
value_inside.set(opciones[0])

value_inside2= tkinter.StringVar(vent)
value_inside2.set(opciones[0])



menu = tkinter.OptionMenu(vent, value_inside, *opciones)
menu.place(x = 100, y = 200, anchor= tkinter.CENTER)
menu.configure(height = 2,  bg = "light gray", font = "arial 12 italic")

menu2 = tkinter.OptionMenu(vent, value_inside2, *opciones)
menu2.place(x = 300, y = 200, anchor= tkinter.CENTER)
menu2.configure(height = 2, bg = "light gray", font = "arial 12 italic")


##---------------------------------------------------------------------------------------
##---------------------------------------------------------------------------------------
##---------------------------------------------------------------------------------------
##---------------------------------------------------------------------------------------

entrada1 = tkinter.Entry(vent, bg =  "#06283D", fg = "light gray", font = "MSSansSerif 25", width = 10)
entrada1.place(x = 200, y = 120, anchor= tkinter.CENTER)

##---------------------------------------------------------------------------------------
##---------------------------------------------------------------------------------------
#años--------------------------------------------------------------------
def año_a_mes(año):
    return(año * 12)
def año_a_sem(año):
    return(año * 52.143)
def año_a_dia(año):
    return(año * 365)
def año_a_hs(año):
    return(año * 8760)
def año_a_min(año):
    return(año * 525600)
def año_a_seg(año):
    return(año * 3.154e+7)

#meses-------------------------------------------------------------------
def mes_a_año(mes):
    return(mes / 12)
def mes_a_sem(mes):
    return(mes * 4.345)
def mes_a_dias(mes):
    return(mes * 30.417)
def mes_a_hs(mes):
    return(mes * 730)
def mes_a_min(mes):
    return(mes * 43800)
def mes_a_seg(mes):
    return(mes * 2.628e+6)

#semanas------------------------------------------------------
def sem_a_año(sem):
    return(sem / 52.143)
def sem_a_mes(sem):
    return(sem / 4.345)
def sem_a_dia(sem):
    return(sem * 7)
def sem_a_hs(sem):
    return(sem * 168)
def sem_a_min(sem):
    return(sem * 10080)
def sem_a_seg(sem):
    return(sem * 604800)

#dias---------------------------------------------------------
def dias_a_años(dia):
    return (dia / 365)
def dias_a_mes(dia):
    return(dia / 30.417)
def dias_a_sem(dia):
    return(dia / 7)
def dias_a_hs(dia):
    return (dia * 24)
def dias_a_min(dia):
    return (dia * 1440)
def dias_a_segs(dia):
    return (dia * 86400)

#horas---------------------------------------------------------
def hs_a_años(hs):
    return(hs / 8760)
def hs_a_meses(hs):
    return(hs / 730)
def hs_a_semanas(hs):
    return (hs / 168)
def hs_a_dias(hs):
    return(hs / 24)
def hs_a_min(hs):
    return(hs * 60)
def hs_a_seg(hs):
    return (hs * 3600)

#minutos-------------------------------------------------------
def min_a_años(min):
    return (min / 525600)
def min_a_meses(min):
    return (min / 43800)
def min_a_sem(min):
    return (min / 10080)
def min_a_dia(min):
    return (min / 1440)
def min_a_horas(min):
    return (min / 60)
def min_a_seg(min):
    return (min * 60)

#segundos-------------------------------------------------------------------------
def seg_a_años(seg):
    return (seg / 3.154e+7)
def seg_a_meses(seg):
    return (seg / 2.628e+6)
def seg_a_sem(seg):
    return (seg / 604800)
def seg_a_dia(seg):
    return (seg / 86400)
def seg_a_horas(seg):
    return (seg / 3600)
def seg_a_min(seg):
    return (seg / 60)
##---------------------------------------------------------------------------------------
def convertir_tiempo(tiempo, conv_from, conv_to):
    #año
    if (conv_from == "Años"):
        if (conv_to == "Meses"):
            tiempo = año_a_mes(tiempo)
        elif (conv_to == "Semanas"):
            tiempo = año_a_sem(tiempo)
        elif (conv_to == "Dias"):
            tiempo = año_a_dia(tiempo)
        elif(conv_to == "Horas"):
            tiempo = año_a_hs(tiempo)
        elif(conv_to == "Minutos"):
            tiempo = año_a_min(tiempo)
        elif(conv_to == "Segundos"):
            tiempo = año_a_seg(tiempo)
        else:
            tiempo = tiempo

    elif (conv_from == "Meses"):
        if (conv_to == "Años"):
            tiempo = mes_a_año(tiempo)
        elif (conv_to == "Semanas"):
            tiempo = mes_a_sem(tiempo)
        elif (conv_to == "Dias"):
            tiempo = mes_a_dias(tiempo)
        elif(conv_to == "Horas"):
            tiempo = mes_a_hs(tiempo)
        elif(conv_to == "Minutos"):
            tiempo = mes_a_min(tiempo)
        elif(conv_to == "Segundos"):
            tiempo = mes_a_seg(tiempo)
        else:
            tiempo = tiempo
    
    elif (conv_from == "Semanas"):
        if (conv_to == "Años"):
            tiempo = sem_a_año(tiempo)
        elif (conv_to == "Meses"):
            tiempo = sem_a_mes(tiempo)
        elif (conv_to == "Dias"):
            tiempo = sem_a_dia(tiempo)
        elif(conv_to == "Horas"):
            tiempo = sem_a_hs(tiempo)
        elif(conv_to == "Minutos"):
            tiempo = sem_a_min(tiempo)
        elif(conv_to == "Segundos"):
            tiempo = sem_a_seg(tiempo)
        else:
            tiempo = tiempo

    elif (conv_from == "Dias"):
        if (conv_to == "Años"):
            tiempo = dias_a_años(tiempo)
        elif (conv_to == "Meses"):
            tiempo = dias_a_mes(tiempo)
        elif (conv_to == "Semanas"):
            tiempo = dias_a_sem(tiempo)
        elif(conv_to == "Horas"):
            tiempo = dias_a_hs(tiempo)
        elif(conv_to == "Minutos"):
            tiempo = dias_a_min(tiempo)
        elif(conv_to == "Segundos"):
            tiempo = dias_a_segs(tiempo)
        else:
            tiempo = tiempo

    elif (conv_from == "Horas"):
        if (conv_to == "Años"):
            tiempo = hs_a_años(tiempo)
        elif (conv_to == "Meses"):
            tiempo = hs_a_meses(tiempo)
        elif (conv_to == "Semanas"):
            tiempo = hs_a_semanas(tiempo)
        elif(conv_to == "Dias"):
            tiempo = hs_a_dias(tiempo)
        elif(conv_to == "Minutos"):
            tiempo = hs_a_min(tiempo)
        elif(conv_to == "Segundos"):
            tiempo = hs_a_seg(tiempo)
        else:
            tiempo = tiempo

    elif (conv_from == "Minutos"):
        if (conv_to == "Años"):
            tiempo = min_a_años(tiempo)
        elif (conv_to == "Meses"):
            tiempo = min_a_meses(tiempo)
        elif (conv_to == "Semanas"):
            tiempo = min_a_sem(tiempo)
        elif(conv_to == "Dias"):
            tiempo = min_a_dia(tiempo)
        elif(conv_to == "Horas"):
            tiempo = min_a_horas(tiempo)
        elif(conv_to == "Segundos"):
            tiempo = min_a_seg(tiempo)
        else:
            tiempo = tiempo

    elif (conv_from == "Segundos"):
        if (conv_to == "Años"):
            tiempo = seg_a_años(tiempo)
        elif (conv_to == "Meses"):
            tiempo = seg_a_meses(tiempo)
        elif (conv_to == "Semanas"):
            tiempo = seg_a_sem(tiempo)
        elif(conv_to == "Dias"):
            tiempo = seg_a_dia(tiempo)
        elif(conv_to == "Horas"):
            tiempo = seg_a_horas(tiempo)
        elif(conv_to == "Minutos"):
            tiempo = seg_a_min(tiempo)
        else:
            tiempo = tiempo
    #---------------------------------------------------------------------------------------
    #retornar cuadro de texto
    msj = messagebox.showinfo(title = "Resultado", message = f"La respuesta es: {tiempo}")
    return msj

def convertir():
    conv_from = option_selected(value_inside)
    conv_to = option_selected(value_inside2)
    
    tiempo = float(entrada1.get())
 
    convertir_tiempo(tiempo, conv_from, conv_to)

##---------------------------------------------------------------------------------------
##---------------------------------------------------------------------------------------
##---------------------------------------------------------------------------------------


bot = tkinter.Button(vent, font = "MSSansSerif 20", text = "Convertir.", command = convertir)
bot.place(relx = 0.5, rely = 0.80, anchor= tkinter.CENTER)

vent.mainloop()