# Automatically reformat code on save
# Press Ctrl Alt 0S to open settings and then select Tools | Actions on Save.
# Enable the Reformat code option.

# This main menu program


import tkinter as tk

from tkinter import Menu

import casbbankreport

from casbbankreport import ledger_report


def ledger_report1():
    casbbankreport.ledger_report()


root = tk.Tk()
root.geometry('1000x650')
root.title('Menu Demo')

# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create the file_menu
file_menu = Menu(
    menubar,
    tearoff=0
)

# add menu items to the File menu
file_menu.add_command(label='Voucher Entries')
file_menu.add_separator()

# add Exit menu item
file_menu.add_command(
    label='Exit',

)

# add the File menu to the menubar
menubar.add_cascade(
    label="TRANSACTIONS",
    menu=file_menu
)
# create the Help menu
help_menu = Menu(
    menubar,
    tearoff=0
)

help_menu.add_command(label='Ledgers', command=ledger_report1)
help_menu.add_command(label='About...')

# add the Help menu to the menubar
menubar.add_cascade(
    label="REPORTS",
    menu=help_menu
)

root.mainloop()
