# this program to create Master File in connection with accounting software
#program finished on 30.08.24
# column 3rd level * child fields not finished

import tkinter as tk

from  tkinter import *

from tkinter import ttk

from tkinter import Tk, mainloop
from tkinter.ttk import Label, LabelFrame
import mysql.connector
global mgroup_code
conn=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd="Milan@2000",
    database='accounts')
c=conn.cursor()
#c.conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS Master(acc_code INT(5) NOT NULL AUTO_INCREMENT PRIMARY KEY ,"
          "acc_name VARCHAR(35),group_name VARCHAR(35),group_code INT(5), op_bal FLOAT(12,2),dr_cr VARCHAR(2), "
          "level INT(2), child INT(1) ) ")
conn.commit()
""" number_of_rows= c.execute("SELECT * FROM master")
if not number_of_rows:
    print(number_of_rows)
    INSERT INTO masters(acc_code,Acc_name,level) VALUES(1,"ASSETS",1)
    INSERT INTO masters(acc_code,Acc_name,level) VALUES(2,"LIABILITIES",1)
    INSERT INTO masters(acc_code,Acc_name,level) VALUES(3,"EXPENSES",1)
    INSERT INTO masters(acc_code,Acc_name,level) VALUES(4,"INCOME",1)
    
    INSERT INTO masters(acc_code,Acc_name,level,group_code,group_name) VALUES(5,"Cash Book",2,1,"ASSETS")
    INSERT INTO masters(acc_code,Acc_name,level,group_code,group_name) VALUES(6,"BANK ACCOUNTS",2,1,"ASSETS")
    INSERT INTO masters(acc_code,Acc_name,level,group_code,group_name) VALUES(7,"SUNDRY CREDITORS",2,1,"ASSETS")
    INSERT INTO masters(acc_code,Acc_name,level,group_code,group_name) VALUES(8,"SUNDRY DEBTORS",2,2,"LISBILITIES")
    
"""
c.execute("SELECT acc_name FROM  master")
results = c.fetchall()
#print(results)
my_list = results
my_dict ={}
for row in results:
    my_dict [[row][0][0]]= row
#print(my_dict)

def do_Save(*arg):
   # pass

    c.execute("CREATE TABLE IF NOT EXISTS Master(acc_code INT(5) NOT NULL AUTO_INCREMENT PRIMARY KEY ,"
             "acc_name VARCHAR(35),group_name VARCHAR(35),group_code INT(5), op_bal FLOAT(12,2),dr_cr VARCHAR(2), "
             "level INT(2), child INT(1) ) ")
    conn.commit()
    print("Master table successfully created")
    macc_name = acc_name.get()
    mgroup_name = group_name.get()
    mop_bal =opn_bal.get()
    if mop_bal  == "":
       mop_bal = float()
       mdr_cr = 0
    if mgroup_name == "":
       mlevel = 1
    else:

       mlevel = 2
       mdr_cr = dr_cr.get()

    master_data = (mgroup_code,mgroup_name,macc_name,mop_bal,mdr_cr,mlevel)
    mysql_insert_query = ("INSERT INTO master(group_code,group_name,acc_name,op_bal,dr_cr,level) VALUES(%s,%s,%s,%s,%s,%s)")
    print(master_data)
    c.execute(mysql_insert_query,master_data)
    conn.commit()
    print("Record successfully insert into Master table")
    do_Reset()

def do_Exit():
    quit()

def do_Reset():
    acc_name.delete(0,END)
    group_name.delete(0,END)
    opn_bal.delete(0, END)
    dr_cr.delete(0,END)
    acc_name.focus()
def my_upd(*args):
    global mgroup_code
    query="SELECT acc_code,acc_name FROM  master"
    my_data = c.execute(query)
    results = c.fetchall()
    my_list = results

   # print(sel.get())
    for row in results:
        if row[1]== sel.get():
            mgroup_code = row[0]
 #   print(mgroup_code)

master = tk.Tk()
master.geometry("650x150")
tk.Label(master, text="Account Name",font=('Ariel',14)).grid(row=0 )
tk.Label(master, text="Group Name",font=('Ariel',14)).grid(row=1)
tk.Label(master, text="Opening Bal",font=('Ariel',14)).grid(row=2)
frame1 = Frame(master)
frame1.grid()
mgroup_code =0
box_value = tk.StringVar()
sel = tk.StringVar()
acc_name = tk.Entry(master, width=30, font=('Ariel', 14))

group_name = ttk.Combobox(master,values = my_list,textvariable=sel)
opn_bal =  tk.Entry(master, width=12, font=('Ariel', 14),justify=RIGHT)
dr_cr = ttk.Combobox(master,textvariable=box_value,values=["","Dr","Cr"] ,width=10,font=('Ariel',14))

acc_name.grid(row=0, column=1)
group_name.grid(row=1, column=1)
opn_bal.grid(row=2, column=1)
dr_cr.grid(row=2,column=2)
sel.trace('w',my_upd)
#obj = Master(acc_name,group_name,mgroup_code,opn_bal,dr_cr)
b1=tk.Button(frame1,text='OK'   ,font=('Ariel',14),command=do_Save)
b2=tk.Button(frame1,text='RESET',font=('Ariel',14),command=lambda : do_Reset())
b3=tk.Button(frame1,text='QUIT' ,font=('Ariel',14),command=lambda : do_Exit())

b1.grid(row=6,column=0)
b2.grid(row=6,column=1)
b3.grid(row=6,column=2)

master.mainloop()
