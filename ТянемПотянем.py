from tkinter import *
from tkinter import messagebox
def calculate():
    buhta = float(weight.get()) / 3
    povt = float(weight.get()) / 3
    kross = float(weight.get()) / 1.5
    mufta = float(weight.get()) / 1.5
    sum = buhta * 36000 + povt*300000 + kross *1200 + mufta * 1200
    if sum > 0:
        messagebox.showinfo('затраты', f'Примерные затраты материала = {sum} рублей')
    else:
        messagebox.showinfo('затраты',  f'Вы не корректно ввели данные')
def clear():
    weight.delete("0", "end")
window = Tk()
window.title('Примерные затраты на материал')
window.geometry('600x100')


name = Label(window, text="Рассчитать затрат")
name.grid(row=0, column=1)

weight = Label(window, text="Введите протяженность трассы(в км)")
weight.grid(row=1, column=1)

weight = Entry(window)
weight.grid(row=1, column=2)

cal_btn = Button(window, text='Рассчитать', command=calculate)
cal_btn.grid(row=3, column=1)
clear_btn = Button(window, text="Сброс", command=clear)
clear_btn.grid(row=3, column=2)

window.mainloop()
