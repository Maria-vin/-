from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Расчет рулонов")
window.geometry('600x350')

def clicked():
    res1 = " {}".format(txt1.get())
    res2 = " {}".format(txt2.get())
    res3 = " {}".format(txt3.get())
    res4 = " {}".format(txt4.get())
    res5 = " {}".format(txt5.get())

    square_g = float(res1)
    square_d = float(res2)
    square_w = float(res3)
    length_roll = float(res4)
    width_roll = float(res5)

    amount_roll = (((square_g - (square_d + square_w))/(length_roll * width_roll)))
    round_ar = round(amount_roll)
    str_round_ar = str(round_ar)

    messagebox.showinfo('Расчет рулонов', str_round_ar + " рулонов обоев необходимо для поклейки стен команты.")

errmsg = StringVar()

lbl = Label(window, text="")
lbl.grid(column=0, row=0)
lbl = Label(window, text="    Для получении информации о количестве рулонов обоев Вам необходимо ввести следующие данные.")
lbl.grid(column=0, row=1)
lbl = Label(window, text="Ввод чисел с дробной частью производиться исключительно через точку.")
lbl.grid(column=0, row=2)
lbl = Label(window, text="")
lbl.grid(column=0, row=3)

lbl1 = Label(window, text="Общая площадь стен комнаты (в м2)")
lbl1.grid(column=0, row=4)
txt1 = Entry(window,width=20)
txt1.grid(column=0, row=5)

lbl2 = Label(window, text="Площадь двери (в м2)")
lbl2.grid(column=0, row=6)
txt2 = Entry(window,width=20)
txt2.grid(column=0, row=7)

lbl3 = Label(window, text="Площадь окна (в м2)")
lbl3.grid(column=0, row=8)
txt3 = Entry(window,width=20)
txt3.grid(column=0, row=9)

lbl4 = Label(window, text="Длина одного рулона обоев (в м)")
lbl4.grid(column=0, row=10)
txt4 = Entry(window,width=20)
txt4.grid(column=0, row=11)

lbl5 = Label(window, text="Ширина одного рулона обоев (в м)")
lbl5.grid(column=0, row=12)
txt5 = Entry(window,width=20)
txt5.grid(column=0, row=13)

lbl = Label(window, text="")
lbl.grid(column=0, row=14)

btn = Button(window, text='Далее', command=clicked)
btn.grid(column=0, row=15)

window.mainloop()