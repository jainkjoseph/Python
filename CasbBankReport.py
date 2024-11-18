# This for report generation through calling module ReportLedger.py
# report based on head selection
#program started  on 30.08.24
# tables required transaction & Master
# password & user   root , Milan@2000
from tkinter import Tk
import tkinter as tk

from tkinter import *

from tkinter import ttk

from tkinter.ttk import Label, LabelFrame

from tkcalendar import Calendar, DateEntry

from datetime import date

from ReportLedger import *

import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd="",
    database='accounts')
c = conn.cursor()
c1 = conn.cursor()
c2 = conn.cursor()
c3 = conn.cursor()

# This section for  Cash or  Bank head Selection
options = []
#c.execute("SELECT acc_code,acc_name FROM  master WHERE acc_name = 'CASH BOOK' OR  group_name = '{BANK ACCOUNTS}' ")
c.execute("SELECT acc_code,acc_name FROM  master")

display_Cash_Bank = c.fetchall()  # display cash & Banks head only
for i in display_Cash_Bank:
    options.append(str(i[1]))


def lookup_cash_bank(event):
    global macc_name, macc_code
    cash_Bank_Name = master.acc_name.get()

    c3 = conn.cursor()
    query = "SELECT * FROM master WHERE acc_name = %s"
    c3.execute(query, (cash_Bank_Name,))

    rows = c3.fetchall()

    for i in rows:
        macc_code = i[0]
        macc_name = i[1]


def do_print():
    ReportLedger1(macc_code, macc_name)


def do_Exit():
    quit()


def do_Reset():
    macc_code = ""
    acc_name.delete(0, END)
    acc_name.focus()


def main(master):
    # master = tk.Tk()

    master.geometry("550x250")
    master.title("Home Expenses", )
    # This varibles for Cash/Bank master file storing
    master.macc_code = StringVar()
    master.macc_name = StringVar()
    sel1 = tk.StringVar()
    label_Color = "Blue"
    label_frame0 = tk.LabelFrame(master, text="CASH/BANK REGISTERS", font=('Cooper Black', 18, 'italic'), height=125,
                                 width=700, labelanchor='n')
    label_frame0.pack(padx=5, pady=5)
    Label(label_frame0, text="Cash/Bank", font=('Ariel', 14), foreground='Blue').place(x=25, y=20)
    master.acc_name = ttk.Combobox(label_frame0, values=options, textvariable=sel1, font=('Ariel', 14), width=25)

    master.acc_name.current(0)
    master.acc_name.place(y=20, x=130)
    """ place without next line; bind showing nontype error
   """

    #master.acc_name.bind('<<ComboboxSelected>>',comboclick)
    master.acc_name.bind('<<ComboboxSelected>>', lookup_cash_bank)
    Label(label_frame0, text="period", font=('Ariel', 14), foreground='Blue').place(x=25, y=60)
    today = date.today()
    master.doc_Date1 = today.strftime("%dd/%mm/%YY")
    master.doc_Date2 = date.today()
    doc_Date1 = DateEntry(label_frame0, font=('Ariel', 14), width=10)
    doc_Date1.place(x=130, y=60)
    doc_Date2 = DateEntry(label_frame0, font=('Ariel', 14), width=10)
    doc_Date2.place(x=300, y=60)
    label_frame2 = tk.LabelFrame(master, height=80, width=700, labelanchor='n')
    label_frame2.pack(padx=5, pady=5)
    b1 = tk.Button(label_frame2, text='OK', font=('Ariel', 14), fg=label_Color, padx=20, command=do_print)
    b2 = tk.Button(label_frame2, text='RESET', font=('Ariel', 14), fg=label_Color, padx=20, command=lambda: do_Reset())
    b3 = tk.Button(label_frame2, text='QUIT', font=('Ariel', 14), fg=label_Color, padx=20, command=lambda: do_Exit())
    b1.place(y=25, x=100)
    b2.place(y=25, x=250)
    b3.place(y=25, x=400)
    master.mainloop()


if __name__ == "__main__":
    master = tk.Tk()
    main(master)
