#import required Libraries
import requests
from tkinter import *
from tkinter import ttk
#define currency convertor object
class Currency_Convertor:
    rates = {}
    def __init__(self, url):
        data = requests.get(url).json()
        self.rates = data["rates"]
    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'EUR':
            amount = amount / self.rates[from_currency]
        amount = round(amount * self.rates[to_currency], 2)
        to1.delete(0, last =END)
        to1.insert(0, amount)



#define url to pull data from
url = str.__add__('http://data.fixer.io/api/latest?access_key=', "94f9cbf5f43e2f858e53cb0e66219560")
#define object with url 
c= Currency_Convertor(url)

#define gui objects 
root = Tk()
cur1 = StringVar()
cur2= StringVar()
root.title("Currency")
label = Label(root, text = "Currency")
label.pack()
frame1 = Frame(root, height = 10, width = 60)
currency1 = ttk.Combobox(frame1, textvariable = cur1, width = 30)
currency2 = ttk.Combobox(frame1, textvariable= cur2, width = 30)
frame1.pack(side = TOP)
currency1.pack(side = LEFT)
currency2.pack(side = RIGHT)
#define list of currencies to convert to and from(will expand later)
currency1.config(values = ("USD", "EUR", "JPY", "GBP"))
currency2.config(values = ("USD", "EUR", "JPY", "GBP"))
frame2 = Frame(root, height = 10, width = 60)
frame2.pack(side = BOTTOM)
#define textvariable as a double so that it can be used for math functions
ammount1 = DoubleVar()
from1 = ttk.Entry(frame2, width = 33, textvariable = ammount1)
to1 = ttk.Entry(frame2, width = 33)
from1.pack(side= LEFT)
to1.pack(side = RIGHT)

frame3 = Frame(frame2, height = 10 , width = 60)
frame3.pack(side = BOTTOM)
#define button so that it will use frame3 as it's home and will say convert
button1 = ttk.Button(frame3, text = "Convert")
#call convert using a lambda function so that arguements can be passed
button1.config(command = lambda: (c.convert(str(currency1.get()), str(currency2.get()), float(from1.get()))))
button1.pack(side = LEFT)




