import requests
import json
import pprint
from tkinter import*
from tkinter import messagebox as mb
from tkinter import ttk


def update_b_label(event): #так как функцию вызываем когда происходит событие то надо добавить event в аргумент
    code = b_combobox.get()
    name = cur[code]
    b_label.config(text=name)


def update_t_label(event): #так как функцию вызываем когда происходит событие то надо добавить event в аргумент
    code = t_combobox.get()
    name = cur[code]
    t_label.config(text=name)

def exchange():
    t_code = t_combobox.get()
    b_code = b_combobox.get()

    if t_code and b_code:# если код есть то работаем дальше, если код не введен то программа должна попросить ввести код
        try:
            response = requests.get(f"https://open.er-api.com/v6/latest/{b_code}")# получаем информацию в переменную
            response.raise_for_status()# проверяем статус ,если получаем ответ 200 то все хорошо

            data = response.json()#переводим json в обычный питон словарь

            if t_code in data["rates"]:# если в "rates" существует введенный код . то мы берем это значение
                exchange_rate = data["rates"][t_code]#в пременную положим словарь, и из него выбираем значение по ключу
                t_name = cur[t_code]
                b_name = cur[b_code]
                mb.showinfo("курс обмена", f"Курс: {exchange_rate:.2f} {t_name} за 1 {b_name}")
            else:
                mb.showerror("Ошибка!", f"Валюта {t_code} не найдена!")
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
window.geometry("360x300")

Label(text="Базовая валюта").pack(padx=10, pady=10)
b_combobox= ttk.Combobox(values=list(cur.keys()))# нужно из словаря сделать список , используем функцию лист
b_combobox.pack(padx=10, pady=10)
b_combobox.bind("<<ComboboxSelected>>", update_b_label)

b_label = ttk.Label()
b_label.pack(padx=10, pady=10)

Label(text="Целевая валюта").pack(padx=10, pady=10)#метку нигде использовать не будем

t_combobox= ttk.Combobox(values=list(cur.keys()))# нужно из словаря сделать список , используем функцию лист
t_combobox.pack(padx=10, pady=10)
t_combobox.bind("<<ComboboxSelected>>", update_t_label)#когда произойдет событие выбора значения из выпадающего списка то запустится функция update, метка будет обновляться

t_label = ttk.Label()
t_label.pack(padx=10, pady=10)

Button(text="получить курс обмена к доллару", command=exchange).pack(padx=10, pady=10)#к кнопке обращаться не будем, поэтому имя не присваивается, будем просто нажимать кнопку

window.mainloop()