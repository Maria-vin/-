from tkinter import *
from tkinter import messagebox
def calculate_bmi():
    buhta = float(weight.get()) / 3
    povt = float(weight.get()) / 3
    kross = float(weight.get()) / 1.5
    mufta = float(weight.get()) / 1.5
    sum = buhta * 36000 + povt*300000 + kross *1200 + mufta * 1200
    if sum > 0:
        messagebox.showinfo('затраты', f'Примерные затраты материала = {sum} рублей')
    else:
        messagebox.showinfo('затраты',  f'Вы не ввели данные')
def clear():
    weight.delete("0", "end")
window = Tk()
window.title('Примерные затраты на материал')
window.geometry('700x100')
window["bg"] = "lemon chiffon"


name = Label(window, text="Рассчитать затрат", bg="lemon chiffon", fg="black", width=28, font=('helvetica', 15, 'bold'), compound=RIGHT)
name.grid(row=0, column=0)

weight = Label(window, text="Введите протяженность трассы(в км)", bg="lemon chiffon", fg="black", font=6)
weight.grid(row=1, column=1)

weight = Entry(window, width=28, font=6, bg="navajo white", bd=5)
weight.grid(row=1, column=2)

cal_btn = Button(window, text='Рассчитать', bg="navajo white", command=calculate_bmi, bd=5, width=15, font=6)
cal_btn.grid(row=3, column=1)
clear_btn = Button(window, fg="black", text="Сброс", bg="navajo white", command=clear, bd=5,  width=15, font=6)
clear_btn.grid(row=3, column=2)

window.mainloop()
