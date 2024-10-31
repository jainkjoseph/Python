from reportlab.lib import colors

from reportlab.lib.pagesizes import letter

from reportlab.platypus import SimpleDocTemplate, Table,TableStyle

import mysql.connector




conn = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd="Milan@2000",
    database='accounts')
c = conn.cursor()
conn.commit()


pdf = SimpleDocTemplate("table_example.pdf", pagesize=letter)
c.execute("SELECT doc_date,doc_no,ledger_name,  ledger_cr_amount FROM  Transanction WHERE acc_code =5")
data=[]


 
titles = ['Date','Voucher No.','Description','Amount','Amount','Balance']
elements = []

data.append(titles)
data1 = c.fetchall()  # display cashBOOK Only

for p in data1:
    data.append(p)

total_amount = sum(row[3] for row in data[1:]) #  ledger_cr_amount in4th position

data.append([' ',' ','Total =',round(total_amount,2)])

table = Table(data)

elements.append(table)
pdf.build(elements)



