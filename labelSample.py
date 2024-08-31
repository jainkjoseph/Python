#Import the required library
from tkinter import*
#Create an instance of tkinter frame
win= Tk()
#Set the geometry
win.geometry("750x250")
#Create a Label Widget
Label(win, text= "New Line Text", font= ('Helvetica 15 underline'),
background="gray74").pack(pady=20, side= TOP, anchor="w")
win.mainloop()