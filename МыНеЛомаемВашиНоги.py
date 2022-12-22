from tkinter import *

window = Tk()
window.title("Мы не ломаем ваши ноги")
window.geometry('380x400+760+250')

lbl_description = Label(window,
                        text="Приложение по расчету длины и ширины идеальной ступени, а также количества ступеней "
                             "в зависимости от высоты и длины лестничного пролета",
                        wraplength=390, padx=10, pady=10)
lbl_input = Label(window, text="Для этого Вам необходимо ввести высоту и длину лестничного пролета (см)",
                  wraplength=390, padx=10, pady=10)

lbl_height = Label(window, text="Высота, см: ")
entry_height = Entry(window, width=30)

lbl_length = Label(window, text="Длина, см: ")
entry_length = Entry(window, width=30)


def calculate():
    global output
    length = int(entry_length.get())
    height = int(entry_height.get())
    for a in range(200, 330):
        count = length // (a // 10)
        height_degree = height / (length / (a // 10))
        if 14 < height_degree < 18:
            length_degree = height_degree + 12
            if 46 <= (length_degree + height_degree) <= 47:
                if 60 < ((2 * height_degree) + length_degree) < 65:
                    output.set("Высота: " + str(height_degree) + " см, " + "длина: " + str(
                        length_degree) + " см, " + "количество: " + str(count))
                    break
    else:
        output.set("Данные параметры лестничного пролета не подходят для рассчета идеальной ступени")


btn_output = Button(window, text="Произвести рассчет", command=calculate)

output = StringVar()
output.set("Здесь будут рассчеты ступеней")
lbl_output = Label(window, textvariable=output, wraplength=340, padx=10, pady=10)

lbl_description.grid(row=0, column=0, columnspan=2)
lbl_input.grid(row=1, column=0, columnspan=2)
lbl_height.grid(row=2, column=0, sticky=W, pady=10, padx=10)
entry_height.grid(row=2, column=1, sticky=W)

lbl_length.grid(row=3, column=0, sticky=W, pady=0, padx=10)
entry_length.grid(row=3, column=1, sticky=W)

btn_output.grid(row=4, column=0, columnspan=2, sticky=N, pady=30)
lbl_output.grid(row=5, column=0, columnspan=2, sticky=N, pady=30)
window.mainloop()