"""
Dict = {"CRV": "CASH RECEIPT", "CPV": "CASH PAYMENT","BRV":"BANK RECEIPT","BPV":"BANK PAYMENT","CON":"CONTRA","JOU":"JOURNAL" }
print(Dict)
print(Dict['CRV'])
print(Dict['CPV'])
print(Dict['BRV'])
print(Dict['BPV'])
print(Dict['CON'])
print(Dict['JOU'])
if Dict['CRV'] == "CASH RECEIPT":
    mdcr = "CRV"
    print(mdcr)
 """



import tkinter as tk
from tkinter import ttk

import tkinter as tk

from tkinter import *

from tkinter import ttk

from tkinter.ttk import Label, LabelFrame

import mysql.connector


my_w = tk.Tk()
my_w.geometry("300x150")  # Size of the window
my_w.title("www.plus2net.com")  # Adding a title

def my_upd(*args):

    if cb1.current() == 0:
        mdr_cr = "CRV"
        tr_function(mdr_cr)
    elif cb1.current() == 1:
         mdr_cr= "CPV"
    elif cb1.current() == 2:
        mdr_cr = "BRV"
    elif cb1.current() == 3:
         mdr_cr= "BPV"
    elif cb1.current() == 4:
         mdr_cr= "CON"
    elif cb1.current() == 5:
        mdr_cr = "JOU"
    l1.config(text=sel.get() + " : " + str(cb1.current()))




sel=tk.StringVar() # string variable

months=['CASH RECEIPT','CASH PAYMENT','BANK RECEIPT','BANK PAYMENT','CONTRA','JOURNAL']
cb1 = ttk.Combobox(my_w, values=months,width=12, textvariable=sel)
cb1.grid(row=1,column=1,padx=10,pady=20)

l1=tk.Label(my_w,text='Select Voucher Type')
l1.grid(row=1,column=2)

sel.trace_add('write',my_upd)





my_w.mainloop()  # Keep the window open