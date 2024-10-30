# this program to create Transaction file (Cash Payment) File in connection with accounting software
#program started  on 30.08.24
# tables required transaction & Master
# password & user   root , Milan@2000
import tkinter as tk

from tkinter import *

from tkinter import ttk

from tkinter.ttk import Label, LabelFrame

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
c2.execute("CREATE TABLE IF NOT EXISTS Transanction(doc_date VARCHAR(10),doc_no INT(5),acc_code INT(5)  ,"
          "acc_name VARCHAR(35),ledger_name VARCHAR(35),narration VARCHAR(50), ledger_dr_amount FLOAT(12,2), ledger_cr_amount FLOAT (12,2), voucher_type VARCHAR(5)) ")
conn.commit()

# This section for  Cash or  Bank head Selection
options = []

c.execute("SELECT acc_code,acc_name FROM  master WHERE  acc_name ='CASH BOOK'")
display_Cash_Bank = c.fetchall() # display cash & Banks head only
for i in display_Cash_Bank:
    options.append(str(i[1]))



master = tk.Tk()
master.geometry("700x300")
master.title("Home Expenses", )
# This varibles for Cash/Bank master file storing
macc_code =  StringVar()
macc_name = StringVar()
mdoc_No   =  StringVar()
mdoc_Date = StringVar()
mdr_cr = StringVar()

# This varibles for Ledger Head  from master file storing
macc_code1 =  StringVar()
macc_name1 = StringVar()
mdr_cr1    = StringVar()
mledger_dr_amount = float()
mledger_cr_amount = float()

def lookup_Cash_Bank(event):
    global macc_code,mdr_cr,macc_name
    cash_Bank_Name = acc_name.get()
    print(cash_Bank_Name)
    query = "SELECT * FROM master WHERE acc_name = %s"
    c3.execute(query,(cash_Bank_Name,))
    rows = c3.fetchall()

    for i in rows:
        macc_code=i[0]
        macc_name=i[1]
        mdr_cr = "CPV"  # based master database sequence

#This section for select all ledger heads
options1 = []
c1 = conn.cursor()
c1.execute("SELECT acc_name FROM  master WHERE group_code = 3")
display_Ledger = c1.fetchall()
for i in display_Ledger:
    options1.append(str(i[0]))

def lookup_ledger(event):
    global macc_code1, mdr_cr1,macc_name1,mledger_cr_amount
    ledger_Name = acc_name1.get()
    c4 = conn.cursor()
    query = "SELECT * FROM master WHERE acc_name = %s"
    c4.execute(query, (ledger_Name,))
    rows = c4.fetchall()
    print(rows)
    for i in rows:
        macc_code1 = i[0]
        macc_name1 = i[1]
        mdr_cr1    = "CPV"

def do_Exit():
    quit()

def do_Save():

    mdoc_No = doc_No.get()
    mdoc_Date = doc_Date.get()
    mledger_dr_amount = ledger_dr_Amount.get()
    print(mledger_dr_amount)
    mnarration = narration.get()
    # database insert with Cash book details  (first attempt)
    master_data = (mdoc_No,mdoc_Date,macc_code,macc_name,macc_name1,mledger_cr_amount,mnarration,mdr_cr)
    print(master_data)
    mysql_insert_query = ("INSERT INTO transanction(doc_no,doc_date,acc_code,acc_name,ledger_name,ledger_cr_amount,narration,voucher_type) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)")
    c.execute(mysql_insert_query,master_data)
    conn.commit()
    """
    #dabase insert with Leadger head details (2nd attempt)
    master_data = (mdoc_No,mdoc_Date,macc_code1,macc_name1,mledger_amount,mdr_cr)
    print(master_data)
    mysql_insert_query = ("INSERT INTO transanction(doc_no,doc_date,acc_code,acc_name,ledger_amount,dr_cr) VALUES(%s,%s,%s,%s,%s,%s)")
    c.execute(mysql_insert_query,master_data)
    conn.commit()
    """
    print("Record successfully insert into Transaction  table")
    do_Reset()

def do_Reset():
    doc_No.delete(0,END)
    doc_Date.delete(0,END)
    macc_code = ""
    acc_name.delete(0,END)
    mdr_cr = ""
    macc_code1=""
    acc_name1.delete(0, END)
    mdr_cr1= ""
    mledger_cr_amount = float()
    doc_No.focus()


label_Color = "Blue"
label_frame0 = tk.LabelFrame(master, text="CASH PAYMENT", font=('Cooper Black',18,'italic') ,height=125,width=700,labelanchor='n' )
label_frame0.pack(padx=5,pady=5)
Label(label_frame0, text="Doc.No.", font=('Ariel', 14),foreground='Blue').place(x=5, y=15)
Label(label_frame0, text="Date :" , font=('Ariel', 14),foreground='Blue').place(x=506, y=15)
Label(label_frame0, text="Cash/Bank", font=('Ariel', 14),foreground='Blue').place(x=5, y=50)


doc_No = Entry(label_frame0, font=('Ariel', 14),width=10)
doc_No.place(x=110,y=15)
doc_Date = Entry(label_frame0, font=('Ariel', 14),width=10)
doc_Date.place(x=568,y=15)
sel1 = tk.StringVar()
acc_name = ttk.Combobox(label_frame0,values=options,textvariable=sel1,font=('Ariel', 14),width=25)
(acc_name.place(y=50,x=110))

""" place without next line; bind showing nontype error
"""
acc_name.bind('<<ComboboxSelected>>', lookup_Cash_Bank)

label_frame1 = tk.LabelFrame(master, text="ACCOUNT HEAD.........................................................................................      AMOUNT", font=('Cooper Black',10,'italic') ,height=100,width=700,labelanchor='n' )
label_frame1.pack(padx=5,pady=5)



sel = tk.StringVar()

acc_name1 = ttk.Combobox(label_frame1,values = options1,textvariable=sel,font=('Ariel', 14),width=39)
acc_name1.place(y=5,x=20)
acc_name1.bind('<<ComboboxSelected>>', lookup_ledger)
ledger_dr_Amount = Entry(label_frame1, font=('Ariel', 14),width=15,justify='right')
ledger_dr_Amount.place(x=475,y=5)
narration = Entry(label_frame1, font=('Ariel', 14),width=59,)
narration.place(x=20,y=45)





label_frame2 = tk.LabelFrame(master, height=80,width=700,labelanchor='n' )
label_frame2.pack(padx=5,pady=5)
b1 = tk.Button(master, text='OK', font=('Ariel', 14), fg=label_Color, padx=20, command=do_Save )
b2 = tk.Button(master, text='RESET', font=('Ariel', 14), fg=label_Color, padx=20, command=lambda: do_Reset())
b3 = tk.Button(master, text='QUIT', font=('Ariel', 14), fg=label_Color, padx=20, command=lambda: do_Exit())

b1.place(y=250, x=100)
b2.place(y=250, x=250)
b3.place(y=250, x=400)

master.mainloop()