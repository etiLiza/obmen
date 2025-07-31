import requests
import json
import pprint
from tkinter import*
from tkinter import messagebox as mb
from tkinter import ttk


def update_c_label(event): #так как функцию вызываем когда происходит событие то надо добавить event в аргумент
    code = combobox.get()
    name = cur[code]
    c_label.config(text=name)

def exchange():
    code = combobox.get()#получает информацию из поля entry

    if code:# если код есть то работаем дальше, если код не введен то программа должна попросить ввести код
        try:
            response = requests.get("https://open.er-api.com/v6/latest/USD")# получаем информацию в переменную
            response.raise_for_status()# проверяем статус ,если получаем ответ 200 то все хорошо
            data = response.json()#переводим json в обычный питон словарь
            if code in data["rates"]:# если в "rates" существует введенный код . то мы берем это значение
                exchange_rate = data["rates"][code]#в пременную положим словарь, и из него выбираем значение по ключу
                c_name = cur[code]
                mb.showinfo("курс обмена", f"Курс:{exchange_rate:.2f}{c_name} за 1 доллар")
            else:
                mb.showerror("Ошибка!", f"Валюта {code} не найдена!")
        except Exception as e:
            mb.showerror ("Ошибка!", f"произошла ошибка:{e}.")
    else:
        mb.showwarning("Внимание!", "Введите код валюты")

cur = {"RUB":"Российский рубль",
       "EUR":"Евро",
       "GBP":"Британский фунт стерлингов",
       "JPY":"Японская йена",
       "CNY":"Китайский юань",
       "UZS":"Узбекский сум",
       "CHF":"Швейцарский франк",
       "AED":"Арабский дирхам",
       "CAD":"Канадский доллар"
}#создаем список валют

window = Tk()
window.title('Курс обмена валют')
window.geometry("360x180")

Label(text="Выберите код валюты").pack(padx=10, pady=10)#метку нигде использовать не будем

combobox= ttk.Combobox(values=list(cur.keys()))# нужно из словаря сделать список , используем функцию лист
combobox.pack(padx=10, pady=10)
combobox.bind("<<ComboboxSelected>>", update_c_label)#когда произойдет событие выбора значения из выпадающего списка то запустится функция update, метка будет обновляться

c_label = ttk.Label()
c_label.pack(padx=10, pady=10)

Button(text="получить курс обмена к доллару", command=exchange).pack(padx=10, pady=10)#к кнопке обращаться не будем, поэтому имя не присваивается, будем просто нажимать кнопку

window.mainloop()