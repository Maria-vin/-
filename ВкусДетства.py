from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Расчет цены для коктейля')
root.geometry('720x720')
root.resizable(width=False, height=False)

arr = []


def add_ingr():
    e1 = ingr_name.get()
    e2 = cost.get()
    e3 = amount.get()
    e4 = portion.get()
    s = e1.split(",") + e2.split(",") + e3.split(",") + e4.split(",")
    c = 0
    for i in s:
        if i != "": c += 1
    if c == len(s): arr.append(s)

    ingr_name.delete(0, END)
    cost.delete(0, END)
    amount.delete(0, END)
    portion.delete(0, END)


def count():
    output.delete(0, END)
    price = 0

    for i in arr:
        price += ((int(i[1])) / (int(i[2]) / int(i[3]))) * 2

    output.insert(0, str("%.2f" % round(price, 2)))


ingr = Label(text='Введите ингредиент и данные о нем:')
ingr.place(x=200, y=100)

ingr_name = Entry()
ingr_name.place(x=225, y=150, width=200, height=40)

ingr_name_text = Label(text='Название')
ingr_name_text.place(x=150, y=160)

cost = Entry()
cost.place(x=225, y=200, width=200, height=40)

cost_text = Label(text='Цена')
cost_text.place(x=150, y=210)

amount = Entry()
amount.place(x=225, y=250, width=200, height=40)

amount_text = Label(text='Объем(количество)')
amount_text.place(x=75, y=260)

portion = Entry()
portion.place(x=225, y=310, width=200, height=40)

portion_text = Label(text='Объем(кол-во) на порцию')
portion_text.place(x=55, y=320)

button = Button(text="Расчитать стоимость коктейля", command=count)
button.place(x=100, y=360)

button = Button(text="Добавить ингредиент", command=add_ingr)
button.place(x=400, y=360)

output = Entry()
output.place(x=200, y=450, width=100, height=50)

output_text = Label(text='Стоимость коктейля =')
output_text.place(x=60, y=465)

root.mainloop()

print(arr)
