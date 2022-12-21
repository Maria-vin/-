from tkinter.messagebox import showerror
from math import ceil
import tkinter as tk
from tkinter import IntVar, StringVar, ttk


root = tk.Tk()
root.geometry("600x350")

lang = IntVar()
header = ttk.Label(textvariable=lang)
CHARA_btn = ttk.Radiobutton(text="ЧАРА 321", value=0, variable=lang)
CHARA_btn.grid(column=8, row=2)
ALTAI_btn = ttk.Radiobutton(text="АЛТАЙ 1", value=1, variable=lang)
ALTAI_btn.grid(column=8, row=3)
TULA_btn = ttk.Radiobutton(text="ТУЛА 1", value=2, variable=lang)
TULA_btn.grid(column=8, row=4)
triumf_btn = ttk.Radiobutton(text="ТРИУМФ 111", value=3, variable=lang)
triumf_btn.grid(column=8, row=5)


def calc(room, lino):
    # англ
    room = room.replace(' ', '')
    room = room.replace('x', ' ')
    room = room.replace('X', ' ')
    # рус
    room = room.replace('х', ' ')
    room = room.replace('Х', ' ')

    room = room.replace(',', '.')
    room = room.split(' ')

    try:
        a, b = float(room[0]), float(room[1])
    except Exception:
        showerror(message='Некорректный ввод!')
        return 'None'

    if a < 0 or b < 0:
        showerror(message='Некооректный ввод')
        return 'None'

    square = None
    unit_price = None
    lino = lino.get()

    match lino:
        case 0:
            square = 1.5
            unit_price = 357
        case 1:
            square = 3
            unit_price = 750
        case 2:
            square = 2.5
            unit_price = 632
        case 3:
            square = 4.5
            unit_price = 950

    count = ceil(a * b / square)
    all_price = count * unit_price
    my_str.set(f'{count} рулон. == {all_price}₽')


txt = tk.Entry(root, width=30)
txt.grid(column=4, row=3)

btn = ttk.Button(text="Посчитать",
                 command=lambda: calc(room=txt.get(), lino=lang))
btn.grid(column=4, row=5)

my_str = StringVar()
my_str.set('Здесь будет значение')
lable = ttk.Label(textvariable=my_str)
lable.grid(column=4, row=4)


class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):

        super().__init__(parent)
        table = ttk.Treeview(parent, show="headings", selectmode="browse")
        table["columns"] = headings
        table["displaycolumns"] = headings
        for head in headings:
            table.heading(head, text=head, anchor=tk.CENTER)
            table.column(head, anchor=tk.CENTER)
        for row in rows:
            table.insert('', tk.END, values=tuple(row))
        table.grid(column=4, row=0, columnspan=9)


table = Table(root, headings=('Марка линолеума',
                              'Ширина линолеума',
                              'Цена погонного метра линолеума'),
              rows=(("Линолеум бытовой Комитекс «Чара 321»",
                     "1,5м",
                     "357 руб."),
                    ('Линолеум бытовой Tarkett «Алтай 1»',
                     '3м',
                     '750руб'),
                    ("Линолеум бытовой Tarkett «Тула 1»",
                     "2,5м",
                     "623 руб"),
                    ("Линолеум бытовой комитекс «Триумф 111»",
                     "4,5м",
                     "950 руб")))

root.mainloop()


def calc(room, lino=0):
    # англ
    room = room.replace(' ', '')
    room = room.replace('x', ' ')
    room = room.replace('X', ' ')
    # рус
    room = room.replace('х', ' ')
    room = room.replace('Х', ' ')

    room = room.replace(',', '.')
    room = room.split(' ')

    try:
        a, b = float(room[0]), float(room[1])
    except Exception:
        showerror(message='Ты лох')
        return False

    square = None
    unit_price = None

    match lino:
        case 0:
            square = 1.5
            unit_price = 357
        case 1:
            square = 3
            unit_price = 750
        case 2:
            square = 2.5
            unit_price = 632
        case 3:
            square = 4.5
            unit_price = 950

    count = ceil(a * b / square)
    all_price = count * unit_price
    print(f'{count} рулонов обойдутся в {all_price} рублей')


my_calc = calc(lino=3, room='6 x 4,5')