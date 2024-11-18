#This generate pdf for all  ledger head,  calling from CshBank Report.py
from reportlab.lib import colors

from reportlab.lib.pagesizes import letter

from reportlab.platypus import SimpleDocTemplate, Table,TableStyle

import mysql.connector

def reportledger(macc_code,head,mop_bal):
    tcode = macc_code
    top_bal = mop_bal

    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd="Milan@2000",
        database='accounts')
    c = conn.cursor()
    conn.commit()
    pdf = SimpleDocTemplate("Reports.pdf", pagesize=letter)

    #c.execute("SELECT doc_date,doc_no,ledger_name, ledger_dr_amount, ledger_cr_amount FROM  Transanction WHERE acc_code =macc_code")
    query =("SELECT doc_date,doc_no,ledger_name, ledger_dr_amount, ledger_cr_amount FROM  Transanction WHERE acc_code "
            "= %s")


    c.execute(query,(tcode,))


    data=[]
    elements = []
  #  titles1 = ['Date','Voucher No.','Description','Amount','Amount','Balance']
  #  data.append(titles1)
  

    titles = ['Date','Voucher No.','Description','Amount','Amount','Balance']

    data.append(titles)

    data1 = c.fetchall()  # display selected ledgers Only
    for p in data1:
        data.append(p)

    total_dr_amount = mop_bal+ sum(row[3] for row in data[1:]) #  ledger_dr_amount in4th position
    total_cr_amount = sum(row[4] for row in data[1:]) #  ledger_cr_amount in5th position
    data.append([' ',' ',' ',"-----------","----------"])
    data.append([' ',' ','Total =',round(total_dr_amount,2) , round(total_cr_amount,2), round(total_dr_amount-total_cr_amount,2)])
    data.append([' ',' ',' ',"=======","======"])
    table = Table(data)

    elements.append(table)
    pdf.build(elements)


