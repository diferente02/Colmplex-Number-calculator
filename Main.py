from tkinter import *
import math
import numpy as np
from pyautogui import alert


# ----funções-----

def rp_cal():
    try:
        a = float(ena.get())
        b = float(enb.get())

    except:
        alert("algo deu errado, insira apenas numeros e use o ponto ao invés da vírgula")
        a = float(ena.get())
        b = float(enb.get())

    # parte real
    z = "%.2f" % (math.sqrt(((a**2)+(b**2))))

    #parte imaginaria
    #caluclo arco tangente
    arco = (math.atan(b/a))
    #passando de radianos para graus
    arcog = "%.2f" % (math.degrees(arco))

    lb3 = Label(root, text=f'{a} {b}j = {z}<{arcog}')
    lb3.place(x='15', y='270')


def pr_cal():
    try:
        a = float(ena.get())
        b = float(enb.get())

    except:
        alert("algo deu errado, insira apenas numeros e use o ponto ao invés da vírgula")
        a = float(ena.get())
        b = float(enb.get())

    # pega o valor do cosseno em radianos e passa pra graus
    t2 = np.cos(np.radians(b))
    re = "%.2f" % (t2 * a)     #arredondando pra duas casas depois da virgula

    #pega o valor do cosseno em radianos e passa para graus
    t3 = np.sin(np.radians(b))
    im = "%.2f" % (t3 * a)

    lb3 = Label(root, text=f'{a}<{b} = {re} {im}j'           )
    lb3.place(x='15', y='270')


def bt_click():
    v = variavel.get()
    print(v)

    if v == "x":
        rp_cal()
    else:
        pr_cal()

# -----main -------
root = Tk()
root.geometry('400x500+200+50')

variavel = StringVar()

lb = Label(root, text="Números complexos", font='Arial')
lb.place(x='100', y="15")

rdx = Radiobutton(root, text ='Rentagular[a+bj] para polar[z<0]', value="x", variable= variavel)
rdx.place(x='10', y='55')

rdy = Radiobutton(root, text ='Polar[z<0] para retangular[a+bj]', value="y",variable= variavel)
rdy.place(x='10', y='85')

# ------ parte real --------
lba = Label(root, text = "Parte real =")
lba.place(x='10', y='130')

ena = Entry(root)
ena.place(x='120', y='130')

#------- parte imaginaria -----------
lbb = Label(root, text = "Parte imaginaria =")
lbb.place(x='10', y='200')

enb = Entry(root)
enb.place(x='120', y='200')


bt = Button( root, width='10', text='calcular',command = bt_click)
bt.place(x='140', y='240')


root.mainloop()
