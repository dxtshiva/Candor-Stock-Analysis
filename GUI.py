import warnings

from tkinter import ttk
import matplotlib.pyplot as plt
from ttkwidgets.autocomplete import AutocompleteCombobox
import math
from nsepy import get_history
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from datetime import date
from tkinter import *
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri
from nsetools import Nse
import tkinter as tk
from statsmodels.tsa.arima.model import ARIMA
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from threading import Timer

root = Tk()
root.geometry("1440x1124")
root.configure(bg='black')
style = ttk.Style()
style.configure("Treeview",font=('Times',20),rowheight=50,columnheight=100)
style.configure("Treeview.Heading", font=('Times', 20),rowheight=20,columnheight=100)

nse = Nse()
pandas2ri.activate()
r_nse = importr("nse2r")

lis = nse.get_stock_codes()
lis.pop('SYMBOL')
stocks = []
for i, j in lis.items():
    stocks.append(i + '  (' + j + ')')
global data
now = date.today()


v=1
#entry for showing current price and all
st_entry = ttk.Treeview(root)
st_entry.place(x=10, y=280, width=500, height=530)



#function to refresh the nifty data
def refresh():

    entry1.configure(state='normal')
    entry2.configure(state='normal')
    entry3.configure(state='normal')
    entry4.configure(state='normal')

    data = r_nse.nse_index_quote()

    # df1
    df1 = data[data['index_name'] == 'NIFTY 50'].values[0]
    df1[3] = str(df1[3]) + '%'
    entry1.delete(0.0, END)
    for i in df1:
        entry1.insert(END, str(i) + '\n')
    entry1.configure(state='disabled')
    entry1.tag_config('center', justify='center')
    entry1.tag_add('center', 1.0, 'end')

    # df2
    df2 = data[data['index_name'] == 'NIFTY BANK'].values[0]
    df2[3] = str(df2[3]) + '%'
    entry2.delete(0.0, END)

    for j in df2:
        entry2.insert(END, str(j) + '\n')
    entry2.configure(state='disabled')
    entry2.tag_config('center', justify='center')
    entry2.tag_add('center', 1.0, 'end')

    # df3
    df3 = data[data['index_name'] == 'NIFTY MIDCAP 50'].values[0]
    df3[3] = str(df3[3]) + '%'
    entry3.delete(0.0, END)
    for k in df3:
        entry3.insert(END, str(k) + '\n')
    entry3.configure(state='disabled')
    entry3.tag_config('center', justify='center')
    entry3.tag_add('center', 1.0, 'end')

    # df4
    df4 = data[data['index_name'] == 'NIFTY IT'].values[0]
    df4[3] = str(df4[3]) + '%'
    entry4.delete(0.0, END)

    for l in df4:
        entry4.insert(END, str(l) + '\n')
    entry4.configure(state='disabled')
    entry4.tag_config('center', justify='center')
    entry4.tag_add('center', 1.0, 'end')
    warnings.filterwarnings("ignore")

    Timer(10, refresh).start()


# def on_click(event):
#     d_entry.configure(state="normal")
#     d_entry.delete(0, END)
#
# def end_click(event):
#     d_entry1.configure(state="normal")
#     d_entry1.delete(0,END)

#creating labels and entries for start and end of date
start_d = Label(root, text="Start (dd-mm-yyyy)", font=10).place(x=330, y=130, width=180, height=30)
d_entry = Entry(root, font=("times", 15), width=70)
d_entry.place(x=517, y=130, width=150, height=30)
# d_entry.insert(0,"(dd-mm-yyyy)")
# d_entry.configure(state="disabled")
# d_entry.bind("<Button-1>",on_click)
end_d = Label(root, text="End (dd-mm-yyyy)", font=10).place(x=695, y=130, width=180, height=30)
d_entry1 = Entry(root, font=("times", 15), width=70)
d_entry1.place(x=882, y=130, width=150, height=30)


# d_entry1.insert(0,"(dd-mm-yyyy)")
# d_entry1.configure(state="disabled")
# d_entry1.bind("<Button-1>",end_click)

#function to create graph and update the stocks in treeview frame
def click():
    stock_update()
    sbframe = Frame(root)

    sbframe.place(x=530, y=280, width=900, height=530)
    search = my_entry.get()
    search = search[search.find("(") + 1:search.find(")")]
    #graph
    fig = Figure(figsize=(15, 5))
    plot1 = fig.add_subplot(111)

    canvas = FigureCanvasTkAgg(fig, master=sbframe)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, sbframe)
    toolbar.update()
    canvas._tkcanvas.pack(side=BOTTOM)

    if d_entry.get() != '' and d_entry1.get() != '':
        z, y, x = d_entry.get().split('-')
        c, b, a = d_entry1.get().split('-')
        s_data = get_history(symbol=search, start=date(int(x), int(y), int(z)), end=date(int(a), int(b), int(c)))['Close']

        plot1.plot(s_data)

    else:
        s_data = get_history(symbol=search, start=date(now.year - 6, now.month, now.day),
                             end=date(now.year, now.month, now.day))['Close']
        plot1.plot(s_data)



def stock_update(): #updating stock and predicting the price using 6 year back data

    warnings.filterwarnings("ignore")
    # global v
    # v=v+1
    # print(v)



    search = my_entry.get()
    search = search.split()[:1]
    search=search[0]
    #print(search)

    st_entry['columns'] = (search, "price")

    st_entry.column('#0', width=0, stretch=NO)

    st_entry.column(search, width=250, minwidth=250)
    st_entry.column('price', width=300, minwidth=10)

    st_entry.heading('#0', anchor=CENTER, text='')
    st_entry.heading(search, text=search, anchor=W)
    st_entry.heading("price", text="Price", anchor=W)
    # Fetching live stock data

    data_ = pd.DataFrame(get_history(symbol=search, start=date(now.year - 6, now.month, now.day),
                                     end=date(now.year, now.month, now.day))['Close'])

    prsnt_data = nse.get_quote(search)
    price = r_nse.nse_stock_quote(search)[0]
    pchange = round((price - prsnt_data['basePrice']) / (prsnt_data['basePrice']) * 100, 2)
    curprice = '₹ ' + str(price) + ' (' + str(pchange) + '%)'
    cp = ("Current Price", str(curprice))

    openprice = '₹ ' + str(prsnt_data['open'])
    op = ("Open Price", str(openprice))

    dhigh = '₹ ' + str(prsnt_data['dayHigh'])
    dh = ("Day High", str(dhigh))

    dlow = '₹ ' + str(prsnt_data['dayLow'])
    dl = ("Day Low", str(dlow))

    l52 = '₹ ' + str(prsnt_data['low52'])
    l5 = ("Low 52 week", str(l52))

    h52 = '₹ ' + str(prsnt_data['high52'])
    h5 = ("High 52 week", str(h52))

    # Adding live data to the past data to retrain the model
    data_ = pd.concat([data_, pd.DataFrame([int(price)], index=[date.today()], columns=['Close'])])
    # Creating a prediction model

    model = ARIMA(data_, order=(0, 1, 15))
    model_fit = model.fit()

    # Generating prediction based on the data

    prediction = [round(num, 2) for num in model_fit.predict(start=len(data_), end=len(data_), typ='levels')]
    prediction = '₹ ' + ''.join((map(str, prediction)))

    pred = ("Prediction", str(prediction))
    # print(pred)

    # sdf = pd.concat([cp, op, dh, dl, l5, h5, pred]).pop(0).to_string()
    # print(sdf)

    #deletion
    for item in st_entry.get_children():
        st_entry.delete(item)




    # insertion
    st_entry.insert('', index='end', values=cp)

    st_entry.insert('', index='end', values=op)
    st_entry.insert('', index='end', values=dh)
    st_entry.insert('', index='end', values=dl)
    st_entry.insert('', index='end', values=l5)
    st_entry.insert('', index='end', values=h5)
    st_entry.insert('', index='end', values=pred)
    Timer(10,stock_update).start()


img0 = PhotoImage(file=f"img0.png")
#searchbox
my_entry = AutocompleteCombobox(root, font=("times", 15), width=70, completevalues=stocks)
my_entry.place(x=374, y=55, width=585, height=53)
#search button
b0 = Button(image=img0, borderwidth=0, highlightthickness=0, command=click, relief="flat")
b0.place(x=988, y=55, width=110, height=51)
#entries of nifty's
entry1 = Text(root, bg="#98FB98", font=('Helvetica', 12), highlightthickness=0)

entry1.place(x=320, y=171, width=140, height=100)

entry2 = Text(root, bg="#98FB98", font=('Helvetica', 12), highlightthickness=0)
entry2.place(x=500, y=171, width=140, height=100)

entry3 = Text(root, bg="#98FB98", font=('Helvetica', 12), highlightthickness=0)
entry3.place(x=680, y=171, width=140, height=100)

entry4 = Text(root, bg="#98FB98", font=('Helvetica', 12), highlightthickness=0)
entry4.place(x=860, y=171, width=140, height=100)



refresh()


root.resizable(width=root.winfo_screenwidth(), height=root.winfo_screenheight())

root.mainloop()
