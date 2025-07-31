import requests
import json
import pprint
from tkinter import*
from tkinter import messagebox as mb
from tkinter import ttk





def exchange():
    code = combobox.get()#получает информацию из поля entry

    if code:# если код есть то работаем дальше, если код не введен то программа должна попросить ввести код
        try:
            response = requests.get("https://open.er-api.com/v6/latest/USD")# получаем информацию в переменную
            response.raise_for_status()# проверяем статус ,если получаем ответ 200 то все хорошо
            data = response.json()#переводим json в обычный питон словарь
            if code in data["rates"]:# если в "rates" существует введенный код . то мы берем это значение
                exchange_rate = data["rates"][code]#в пременную положим словарь, и из него выбираем значение по ключу
                mb.showinfo("курс обмена", f"Курс:{exchange_rate:.2f}{code} за 1 доллар")
            else:
                mb.showerror("Ошибка!", f"Валюта {code} не найдена!")
        except Exception as e:
            mb.showerror ("Ошибка!", f"произошла ошибка:{e}.")
    else:
        mb.showwarning("Внимание!", "Введите код валюты")


window = Tk()
window.title('Курс обмена валют')
window.geometry("360x180")

Label(text="Выберите код валюты").pack(padx=10, pady=10)#метку нигде использовать не будем
cur = ["RUB","EUR","GBP","JPY","CNY","UZS","CHF","AED","CAD"]#создаем список валют
combobox= ttk.Combobox(values=cur)
combobox.pack(padx=10, pady=10)

#entry = Entry()#будем к этой метке обращаться окно не указываем , т.к. будет отображаться в виндов
#entry.pack(padx=10, pady=10)

Button(text="получить курс обмена к доллару", command=exchange).pack(padx=10, pady=10)#к кнопке обращаться не будем, поэтому имя не присваивается, будем просто нажимать кнопку

window.mainloop()