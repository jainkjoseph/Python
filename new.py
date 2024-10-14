# cmd - pip install fpdf

from fpdf import FPDF
import os

page = FPDF()
page.add_page()
page.set_font('Arial','B',20)
page.cell(50,40,"This is first pdf report")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
#print(fruit)
    page.cell(1,1,fruit)


page.output("Report.pdf","F")
