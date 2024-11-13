# this program to create Master File in connection with accounting software
# program finished on 30.08.24   , password = "Milan@2000"
# column 3rd level * child fields not finished
# before running this program install mysql and database name is accounts  and table is master

import tkinter as tk

from tkinter import *

from tkinter import ttk

from tkinter import Tk, mainloop
from tkinter.ttk import Label, LabelFrame
import mysql.connector

global results
global mgroup_code
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd="Milan@2000",
    database='accounts')
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS Master(acc_code INT(5) NOT NULL AUTO_INCREMENT PRIMARY KEY ,"
          "acc_name VARCHAR(35),group_name VARCHAR(35),group_code INT(5), op_bal FLOAT(12,2),dr_cr VARCHAR(2), "
          "level INT(2), child INT(1) ) ")

conn.commit()
c.execute("SELECT acc_name FROM  master WHERE acc_name IS NOT NULL")
found_record = c.fetchone()

if found_record is None:

    mtext = [("-select Group", 0, 0, 0, ""), ("ASSETS", 0, 0, 0, ""), ("LIABILITIES", 0, 0, 0, ""),
             ("EXPENSES", 0,0 , 0, ""), ("INCOME", 0, 0, 0, "")]

    master_data = (mtext)
    mysql_insert_query = "INSERT INTO master(acc_name,level,child,group_code,group_name) VALUES (%s,%s,%s,%s,%s)"

    c.executemany(mysql_insert_query, master_data)
    conn.commit()
    c.execute("SELECT acc_name FROM  master WHERE acc_name IS NOT NULL")
    results = c.fetchall()
    my_list = results
    my_dict = {}
    for row in results:
        my_dict[[row][0][0]] = row



else:

    results = c.fetchall()

    my_list = results
    my_dict = {}
    for row in results:
        my_dict[[row][0][0]] = row


def do_Save(*arg):
    tlevel = 0.00

    c.execute("CREATE TABLE IF NOT EXISTS Master(acc_code INT(5) NOT NULL AUTO_INCREMENT PRIMARY KEY ,"
              "acc_name VARCHAR(35),group_name VARCHAR(35),group_code INT(5), op_bal FLOAT(12,2),dr_cr VARCHAR(2), "
              "level INT(2), child INT(1) ) ")
    conn.commit()
    print("Master table successfully created")
    macc_name = acc_name.get()
    # mgroup_name = group_name.get()
    tgroup_name = group_name.get()
    x = len(tgroup_name)

    if tgroup_name[0:1] == "{":
        mgroup_name = (tgroup_name[1:(x - 1)])

    else:
        mgroup_name = tgroup_name

    mop_bal = opn_bal.get()
    if mop_bal == "":
        mop_bal = float()
        mdr_cr = 0
    if mgroup_name == "":
        mlevel = 1
    else:

        mlevel = 2
        mdr_cr = dr_cr.get()
    # head creation write to file

    master_data = (mgroup_code, mgroup_name, macc_name, mop_bal, mdr_cr, mlevel, 0)
    mysql_insert_query = (
        "INSERT INTO master(group_code,group_name,acc_name,op_bal,dr_cr,level,child) VALUES(%s,%s,%s,%s,%s,%s,%s)")
    c.execute(mysql_insert_query, master_data)
    conn.commit()
    """ master head child field updation display acc_code based on group_code count row the
        update child field + rowcount
    """
    c5 = conn.cursor()
    query = "SELECT * FROM master WHERE acc_code = %s"

    c5.execute(query, (mgroup_code,))
    rows = c5.fetchall()

    for i in rows:
        tlevel = i[7]
    xlevel = tlevel + 1
    # updating child field if exists
    query = "update master set child = %s WHERE acc_code = %s"
    c5.execute(query, (xlevel, mgroup_code,))
    conn.commit()
    print("Record successfully insert into Master table")
    do_Reset()


def do_Exit():
    quit()


def do_Reset():
    acc_name.delete(0, END)
    group_name.delete(0, END)
    opn_bal.delete(0, END)
    dr_cr.delete(0, END)
    acc_name.focus()


def my_upd(*args):
    global mgroup_code, mgroup_name

    tgroup_name = group_name.get()

    x = len(tgroup_name)

    if tgroup_name[0:1] == "{":
        mgroup_name = (tgroup_name[1:(x - 1)])

    else:
        mgroup_name = tgroup_name

    c = conn.cursor()
    query = "SELECT * FROM master WHERE acc_name = %s"
    c.execute(query, (mgroup_name,))
    results = c.fetchall()
    my_list = results
    for row in results:
        mgroup_code = row[0]
        mgroup_name = row[1]


master = tk.Tk()
master.geometry("650x150")
tk.Label(master, text="Account Name", font=('Ariel', 14)).grid(row=0)
tk.Label(master, text="Group Name", font=('Ariel', 14)).grid(row=1)
tk.Label(master, text="Opening Bal", font=('Ariel', 14)).grid(row=2)

frame1 = Frame(master)
frame1.grid()
mgroup_code = 0

box_value = tk.StringVar()
sel = tk.StringVar()
acc_name = tk.Entry(master, width=30, font=('Ariel', 14))
acc_name.grid(row=0, column=1)
group_name = ttk.Combobox(master, values=my_list, textvariable=sel)
group_name.grid(row=1, column=1)
group_name.bind('<<ComboboxSelected>>', my_upd)
opn_bal = tk.Entry(master, width=12, font=('Ariel', 14), justify=RIGHT)
opn_bal.grid(row=2, column=1)
dr_cr = ttk.Combobox(master, textvariable=box_value, values=["Dr", "Cr"], width=10, font=('Ariel', 14))
dr_cr.grid(row=2, column=2)

# obj = Master(acc_name,group_name,mgroup_code,opn_bal,dr_cr)
b1 = tk.Button(frame1, text='OK', font=('Ariel', 14), command=do_Save)
b2 = tk.Button(frame1, text='RESET', font=('Ariel', 14), command=lambda: do_Reset())
b3 = tk.Button(frame1, text='QUIT', font=('Ariel', 14), command=lambda: do_Exit())

b1.grid(row=6, column=0)
b2.grid(row=6, column=1)
b3.grid(row=6, column=2)

master.mainloop()
