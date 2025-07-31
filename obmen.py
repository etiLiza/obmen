import requests
import json
import pprint
from tkinter import*
from tkinter import messagebox as mb




window = Tk()
window.title('Курс обмена валют')
window.geometry("360x180")

Label(text="Введите курс валют").pack(padx=10, pady=10)#метку нигде использовать не будем

entry = Entry()#будем к этой метке обращаться окно не указываем , т.к. будет отображаться в виндов
entry.pack(padx=10, pady=10)

Button(text="получить курс обмена к доллару", command=exchange).pack(padx=10, pady=10)#к кнопке обращаться не будем, поэтому имя не присваивается, будем просто нажимать кнопку

window.mainloop()