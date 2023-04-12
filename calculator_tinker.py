from tkinter import *


def clicked_plus():
    resT.delete(0, END)
    res = int(a.get()) + int(b.get())
    resT.insert(0, res)
def clicked_min():
    resT.delete(0, END)
    res = int(a.get()) - int(b.get())
    resT.insert(0, res)
def clicked_umn():
    resT.delete(0, END)
    res = int(a.get()) * int(b.get())
    resT.insert(0, res)
def clicked_del():
    resT.delete(0, END)
    res = int(a.get()) / int(b.get())
    resT.insert(0, res)


window = Tk()
window.title("Calculator")
window.geometry('400x300')
lblA = Label(window, text="Введите первое число")
lblA.grid(column=0, row=0)
a = Entry(window, width=10)
a.grid(column=1, row=0)
lblB = Label(window, text="Введите второе число")
lblB.grid(column=0, row=1)
b = Entry(window, width=10)
b.grid(column=1, row=1)
btnPlus = Button(window, text="+", command=clicked_plus)
btnPlus.grid(column=0, row=3)
btnMinus = Button(window, text="-", command=clicked_min)
btnMinus.grid(column=1, row=3)
btnUmn = Button(window, text="*", command=clicked_umn)
btnUmn.grid(column=0, row=4)
btnDel = Button(window, text="/", command=clicked_del)
btnDel.grid(column=1, row=4)
lblres = Label(window, text="Результат")
lblres.grid(column=0, row=5)
resT = Entry(window, width=10)
resT.grid(column=1, row=5)
window.mainloop()
