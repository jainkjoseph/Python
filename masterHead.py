import tkinter as tk
from  tkinter import *

from tkinter import ttk
import mysql.connector

conn=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd="Milan@2000",
    database='accounts')
c=conn.cursor()
c.execute("SELECT acc_name FROM  master")
results = c.fetchall()
#selected = StringVar()

class Master:
    def __init__(self,acc_name,group_name,op_bal,dr_cr):
        self.acc_name = acc_name
        self.group_name = group_name
        self.op_bal = op_bal
        self.dr_cr = dr_cr



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
   if mgroup_name == "":
       mlevel = 1
   else:
       mlevel = 2
   mdr_cr = dr_cr.get()
   master_data = (macc_name, mgroup_name, mop_bal,mdr_cr,mlevel)
   mysql_insert_query = ("INSERT INTO master(acc_name,group_name,op_bal,dr_cr,level) VALUES(%s,%s,%s,%s,%s)")
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


master = tk.Tk()
master.geometry("650x150")
tk.Label(master, text="Account Name",font=('Ariel',14)).grid(row=0 )
tk.Label(master, text="Group Name",font=('Ariel',14)).grid(row=1)
tk.Label(master, text="Opening Bal",font=('Ariel',14)).grid(row=2)
frame1 = Frame(master)
frame1.grid()
box_value = tk.StringVar()
acc_name = tk.Entry(master, width=30, font=('Ariel', 14))
#group_name = tk.Entry(master, width=30, font=('Ariel', 14) )
group_name = ttk.Combobox(master,values = results)
opn_bal =  tk.Entry(master, width=12, font=('Ariel', 14),justify=RIGHT)
dr_cr = ttk.Combobox(master,textvariable=box_value,values=["","Dr","Cr"] ,width=10,font=('Ariel',14))

acc_name.grid(row=0, column=1)
group_name.grid(row=1, column=1)
opn_bal.grid(row=2, column=1)
dr_cr.grid(row=2,column=2)

obj = Master(acc_name,group_name,opn_bal,dr_cr)

b1=tk.Button(frame1,text='OK'   ,font=('Ariel',14),command=do_Save)
b2=tk.Button(frame1,text='RESET',font=('Ariel',14),command=lambda : do_Reset())
b3=tk.Button(frame1,text='QUIT' ,font=('Ariel',14),command=lambda : do_Exit())

b1.grid(row=6,column=0)
b2.grid(row=6,column=1)
b3.grid(row=6,column=2)

master.mainloop()