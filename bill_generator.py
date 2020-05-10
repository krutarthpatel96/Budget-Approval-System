from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import cx_Oracle as db
import datetime as dt
from PyPDF2 import PdfFileReader, PdfFileWriter
import os

def generate():

    
    f1=open(".\\Bills\\Data_Entry.txt","r")
    m_no=str(f1.read())
    f1.close()

    conn = db.connect("system/2824@localhost/xe")
    cur=conn.cursor()
    data2=cur.execute("select * from manager where mno='"+m_no+"'")
    for row2 in data2:
        m_name=row2[1]

    data=cur.execute("select count(bill_no) from requests where mno='"+m_no+"' and bill_status='Approved'")
    for row in data:
        cnt=row[0]
    print('items : '+str(cnt))

    c = canvas.Canvas(".\\Bills\\"+m_no+" raw.pdf", pagesize=letter)
    c.setLineWidth(.3)
    c.setFont('Helvetica', 12)

    c.line(0,780,650,780)

    c.drawString(260,750,'BILLS SUMMARY')
    c.drawString(250,710,'NIRMA UNIVERSITY')

    curr=dt.datetime.now()
    curr.strftime("%d-%m-%y")
    print(str(curr)[0:10])
    c.drawString(275,680,str(curr)[0:10])
    c.line(0,665,650,665)
     
    c.drawString(40,640,'TOTAL ITEMS :')
    c.drawString(128,640,str(cnt))

    c.drawString(400,640,'Manager No :')
    c.drawString(475,640,m_no)
    
    c.drawString(40,600,'TOTAL AMOUNT :')

    c.drawString(400,600,'Manager Name :')
    c.drawString(495,600,m_name.upper())

    c.line(40,560,520,560)
    c.line(40,560,40,530)
    c.line(520,560,520,530)
    c.line(40,530,520,530)
    c.line(400,560,400,530)
    c.line(80,560,80,530)
    c.drawCentredString(60,540,'SR.')
    c.drawCentredString(220,540,'Remarks')
    c.drawCentredString(460,540,'Amount')

    y1=530
    y2=510
    amt=0

    conn = db.connect("system/2824@localhost/xe")
    cur=conn.cursor()
    data=cur.execute("select * from requests where mno='"+m_no+"' and bill_status='Approved'")

    no=1
    for row in data:
        c.line(40,y1,40,y1-30)
        c.line(400,y1,400,y1-30)
        c.line(520,y1,520,y1-30)
        c.line(40,y1-30,520,y1-30)
        c.line(80,y1,80,y1-30)

        c.drawCentredString(60,y2,str(no))
        c.drawCentredString(220,y2,row[6])
        c.drawCentredString(460,y2,str(row[4]))
        amt=amt+row[4]
        y1=y1-30
        y2=y2-30
        no=no+1

    c.line(400,y1-30,520,y1-30)
    c.line(400,y1,400,y1-30)
    c.line(520,y1,520,y1-30)
    c.line(300,y1-30,400,y1-30)
    c.line(300,y1-30,300,y1)
    c.drawCentredString(350,y2,"TOTAL")
    c.drawCentredString(460,y2,str(amt))
    c.drawString(147,600,"INR. "+str(amt))
    c.drawString(40,150,"Manager's Signature")
    c.drawString(400,150,"Supervisor's Signature")
    c.save()
    

    water=PdfFileReader(open(".\\Bills\\"+m_no+" raw.pdf",'rb'))

    opfile=PdfFileWriter()
    ipfile=PdfFileReader(open(".\\Watermark\\watermark.pdf",'rb'))

    print("water")
    ippage=ipfile.getPage(0)
    ippage.mergePage(water.getPage(0))
    opfile.addPage(ippage)

    water.stream.close()
    os.remove(".\\Bills\\"+m_no+" raw.pdf")
    with open(".\\Bills\\"+m_no+" bills.pdf",'wb') as outputStream:
        opfile.write(outputStream)
