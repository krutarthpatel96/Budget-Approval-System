#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.14
# In conjunction with Tcl version 8.6
#    Jul 01, 2018 09:32:54 PM

import sys
import cx_Oracle as c
import smtplib as s

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

import datetime as dt

import tkinter
from tkinter import messagebox

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import manager_panel_support

import bill_generator as bg

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel (root)
    manager_panel_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel (w)
    manager_panel_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("600x510+415+232")
        top.title("Manager Panel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.02, rely=0.02, relheight=0.14, relwidth=0.96)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=575)

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.03, rely=0.31, height=31, width=92)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Filter :''')
        
        self.show_all = Button(self.Frame1)
        self.show_all.place(relx=0.20, rely=0.31, relheight=0.54, relwidth=0.14)
        self.show_all.configure(activebackground="#d9d9d9")
        self.show_all.configure(activeforeground="#000000")
        self.show_all.configure(background="#d9d9d9")
        self.show_all.configure(disabledforeground="#a3a3a3")
        self.show_all.configure(foreground="#000000")
        self.show_all.configure(highlightbackground="#d9d9d9")
        self.show_all.configure(highlightcolor="black")
        self.show_all.configure(justify=LEFT)
        self.show_all.configure(text='''All''')
        self.show_all.configure(command=self.all)

        self.show_app = Button(self.Frame1)
        self.show_app.place(relx=0.35, rely=0.31, relheight=0.54, relwidth=0.14)
        self.show_app.configure(activebackground="#d9d9d9")
        self.show_app.configure(activeforeground="#000000")
        self.show_app.configure(background="green")
        self.show_app.configure(disabledforeground="#a3a3a3")
        self.show_app.configure(foreground="#000000")
        self.show_app.configure(highlightbackground="#d9d9d9")
        self.show_app.configure(highlightcolor="black")
        self.show_app.configure(justify=LEFT)
        self.show_app.configure(text='''Approved''')
        self.show_app.configure(command=self.app)


        self.show_rej = Button(self.Frame1)
        self.show_rej.place(relx=0.5, rely=0.31, relheight=0.54, relwidth=0.14)
        self.show_rej.configure(activebackground="#d9d9d9")
        self.show_rej.configure(activeforeground="#000000")
        self.show_rej.configure(background="red")
        self.show_rej.configure(disabledforeground="#a3a3a3")
        self.show_rej.configure(foreground="#000000")
        self.show_rej.configure(highlightbackground="#d9d9d9")
        self.show_rej.configure(highlightcolor="black")
        self.show_rej.configure(justify=LEFT)
        self.show_rej.configure(text='''Rejected''')
        self.show_rej.configure(command=self.rej)

        self.Button1 = Button(top)
        self.Button1.place(relx=0.02, rely=0.895, relheight=0.1, relwidth=0.959)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(command=self.print_bills)
        self.Button1.configure(text='''Generate Bill''')

        self.show_pending = Button(self.Frame1)
        self.show_pending.place(relx=0.65, rely=0.31, relheight=0.54
                , relwidth=0.14)
        self.show_pending.configure(activebackground="#d9d9d9")
        self.show_pending.configure(activeforeground="#000000")
        self.show_pending.configure(background="blue")
        self.show_pending.configure(disabledforeground="#a3a3a3")
        self.show_pending.configure(foreground="#000000")
        self.show_pending.configure(highlightbackground="#d9d9d9")
        self.show_pending.configure(highlightcolor="black")
        self.show_pending.configure(justify=LEFT)
        self.show_pending.configure(text='''Pending''')
        self.show_pending.configure(command=self.pend)

        self.Label2_12 = Label(self.Frame1)
        self.Label2_12.place(relx=0.80, rely=0.22, height=40, width=114)
        self.Label2_12.configure(activebackground="#f9f9f9")
        self.Label2_12.configure(activeforeground="black")
        self.Label2_12.configure(background="#d9d9d9")
        self.Label2_12.configure(disabledforeground="#a3a3a3")
        self.Label2_12.configure(foreground="black")
        self.Label2_12.configure(highlightbackground="#d9d9d9")
        self.Label2_12.configure(highlightcolor="black")
        self.Label2_12.configure(text='''NA''')
        self.Label2_12.configure(width=114)

        f1=open("Data_Entry2.txt","r")
        self.m_no=str(f1.read())
        f1.close()

        conn = c.connect("system/2824@localhost/xe")
        cur=conn.cursor()
        data3=cur.execute("select * from manager where mno='"+self.m_no+"'")

        for row3 in data3:
            self.last=row3[5]
        self.Label2_12.configure(text='''Last Login : \n\n'''+self.last)

        curr=dt.datetime.now()
        cur.execute("update manager set last='"+str(curr.strftime("%d-%m-%y %H:%M"))+"'")
        conn.commit()
        conn.close()

        self.Frame2 = Frame(top)
        self.Frame2.place(relx=0.02, rely=0.18, relheight=0.71, relwidth=0.96)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(width=575)

        self.Label1_31 = Label(self.Frame2)
        self.Label1_31.place(relx=0.38, rely=0.03, height=21, width=64)
        self.Label1_31.configure(activebackground="#f9f9f9")
        self.Label1_31.configure(activeforeground="black")
        self.Label1_31.configure(background="#d9d9d9")
        self.Label1_31.configure(disabledforeground="#a3a3a3")
        self.Label1_31.configure(foreground="#000000")
        self.Label1_31.configure(highlightbackground="#d9d9d9")
        self.Label1_31.configure(highlightcolor="black")
        self.Label1_31.configure(text='''Amount''')

        self.Label1_32 = Label(self.Frame2)
        self.Label1_32.place(relx=0.51, rely=0.03, height=21, width=64)
        self.Label1_32.configure(activebackground="#f9f9f9")
        self.Label1_32.configure(activeforeground="black")
        self.Label1_32.configure(background="#d9d9d9")
        self.Label1_32.configure(disabledforeground="#a3a3a3")
        self.Label1_32.configure(foreground="#000000")
        self.Label1_32.configure(highlightbackground="#d9d9d9")
        self.Label1_32.configure(highlightcolor="black")
        self.Label1_32.configure(text='''Remarks''')

        self.Label1_3 = Label(self.Frame2)
        self.Label1_3.place(relx=0.79, rely=0.03, height=21, width=64)
        self.Label1_3.configure(activebackground="#f9f9f9")
        self.Label1_3.configure(activeforeground="black")
        self.Label1_3.configure(background="#d9d9d9")
        self.Label1_3.configure(disabledforeground="#a3a3a3")
        self.Label1_3.configure(foreground="#000000")
        self.Label1_3.configure(highlightbackground="#d9d9d9")
        self.Label1_3.configure(highlightcolor="black")
        self.Label1_3.configure(text='''Action''')

        self.Label1_2 = Label(self.Frame2)
        self.Label1_2.place(relx=0.23, rely=0.03, height=21, width=74)
        self.Label1_2.configure(activebackground="#f9f9f9")
        self.Label1_2.configure(activeforeground="black")
        self.Label1_2.configure(background="#d9d9d9")
        self.Label1_2.configure(disabledforeground="#a3a3a3")
        self.Label1_2.configure(foreground="#000000")
        self.Label1_2.configure(highlightbackground="#d9d9d9")
        self.Label1_2.configure(highlightcolor="black")
        self.Label1_2.configure(text='''Bill Status''')

        self.Label1 = Label(self.Frame2)
        self.Label1.place(relx=0.02, rely=0.03, height=21, width=64)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Emp. No''')

        self.Label1_5 = Label(self.Frame2)
        self.Label1_5.place(relx=0.131, rely=0.03, height=21, width=51)
        self.Label1_5.configure(activebackground="#f9f9f9")
        self.Label1_5.configure(activeforeground="black")
        self.Label1_5.configure(background="#d9d9d9")
        self.Label1_5.configure(disabledforeground="#a3a3a3")
        self.Label1_5.configure(foreground="#000000")
        self.Label1_5.configure(highlightbackground="#d9d9d9")
        self.Label1_5.configure(highlightcolor="black")
        self.Label1_5.configure(text='''Bill No''')
        self.Label1_5.configure(width=74)

        self.save_eno=[]
        self.save_bno=[]
        self.save_bstat=[]
        self.save_amt=[]
        self.save_remarks=[]

        self.lbl1=[]
        self.lbl2=[]
        self.lbl3=[]
        self.lbl4=[]
        self.lbl5=[]
        self.btn1=[]
        self.btn2=[]


        conn = c.connect("system/2824@localhost/xe")
        cur=conn.cursor()
        data=cur.execute("select * from requests where mno='"+self.m_no+"'")
        self.add_views(data)

    def add_views(self,data):

        y=0.09

        i=0
        
        for row in data:
            i=i+1

            self.lbl_bstat = Label(self.Frame2)
            self.lbl_bstat.place(relx=0.23, rely=i*y, height=41, width=74)
            self.lbl_bstat.configure(activebackground="#f9f9f9")
            self.lbl_bstat.configure(activeforeground="black")
            self.lbl_bstat.configure(background="#d9d9d9")
            self.lbl_bstat.configure(disabledforeground="#a3a3a3")
            self.lbl_bstat.configure(foreground="#000000")
            self.lbl_bstat.configure(highlightbackground="#d9d9d9")
            self.lbl_bstat.configure(highlightcolor="black")
            self.lbl_bstat.configure(text='''None''')

            self.lbl_eno = Label(self.Frame2)
            self.lbl_eno.place(relx=0.02, rely=i*y, height=41, width=54)
            self.lbl_eno.configure(activebackground="#f9f9f9")
            self.lbl_eno.configure(activeforeground="black")
            self.lbl_eno.configure(background="#d9d9d9")
            self.lbl_eno.configure(disabledforeground="#a3a3a3")
            self.lbl_eno.configure(foreground="#000000")
            self.lbl_eno.configure(highlightbackground="#d9d9d9")
            self.lbl_eno.configure(highlightcolor="black")
            self.lbl_eno.configure(text='''None''')
            self.lbl_eno.configure(width=54)

            self.lbl_bno = Label(self.Frame2)
            self.lbl_bno.place(relx=0.12, rely=i*y, height=41, width=64)
            self.lbl_bno.configure(activebackground="#f9f9f9")
            self.lbl_bno.configure(activeforeground="black")
            self.lbl_bno.configure(background="#d9d9d9")
            self.lbl_bno.configure(disabledforeground="#a3a3a3")
            self.lbl_bno.configure(foreground="#000000")
            self.lbl_bno.configure(highlightbackground="#d9d9d9")
            self.lbl_bno.configure(highlightcolor="black")
            self.lbl_bno.configure(text='''None''')
            self.lbl_bno.configure(width=64)


            self.lblamt = Label(self.Frame2)
            self.lblamt.place(relx=0.37, rely=i*y, height=41, width=74)
            self.lblamt.configure(activebackground="#f9f9f9")
            self.lblamt.configure(activeforeground="black")
            self.lblamt.configure(background="#d9d9d9")
            self.lblamt.configure(disabledforeground="#a3a3a3")
            self.lblamt.configure(foreground="#000000")
            self.lblamt.configure(highlightbackground="#d9d9d9")
            self.lblamt.configure(highlightcolor="black")
            self.lblamt.configure(text='''None''')

            self.lblremarks= Label(self.Frame2)
            self.lblremarks.place(relx=0.5, rely=i*y, height=41, width=74)
            self.lblremarks.configure(activebackground="#f9f9f9")
            self.lblremarks.configure(activeforeground="black")
            self.lblremarks.configure(background="#d9d9d9")
            self.lblremarks.configure(disabledforeground="#a3a3a3")
            self.lblremarks.configure(foreground="#000000")
            self.lblremarks.configure(highlightbackground="#d9d9d9")
            self.lblremarks.configure(highlightcolor="black")
            self.lblremarks.configure(text='''None''')
            
            self.lbl_bstat.configure(text=row[5])
            self.lbl_eno.configure(text=row[2])
            self.lbl_bno.configure(text=row[0])
            self.lblamt.configure(text=row[4])
            self.lblremarks.configure(text=row[6])

            if(row[5]=='Pending'):
                self.lbl_bstat.configure(fg='blue')
            elif(row[5]=='Approved'):
                self.lbl_bstat.configure(fg='green')
            else:
                self.lbl_bstat.configure(fg='red')
    
            self.save_eno.append(row[2])
            self.save_bno.append(row[0])
            self.save_bstat.append(row[5])
            self.save_amt.append(row[4])
            self.save_remarks.append(row[6])

            self.lbl1.append(self.lbl_bno)
            self.lbl2.append(self.lbl_eno)
            self.lbl3.append(self.lbl_bstat)
            self.lbl4.append(self.lblamt)
            self.lbl5.append(self.lblremarks)


            self.bill_approve = Button(self.Frame2)
            self.bill_approve.place(relx=0.68, rely=i*y, height=34, width=86)
            self.bill_approve.configure(activebackground="#d9d9d9")
            self.bill_approve.configure(activeforeground="#000000")
            self.bill_approve.configure(background="#d9d9d9")
            self.bill_approve.configure(disabledforeground="#a3a3a3")
            self.bill_approve.configure(foreground="#000000")
            self.bill_approve.configure(highlightbackground="#d9d9d9")
            self.bill_approve.configure(highlightcolor="black")
            self.bill_approve.configure(pady="0")
            self.bill_approve.configure(command=lambda i=i:self.update_app(i-1))
            self.bill_approve.configure(text='''Approve''')

            self.bill_reject = Button(self.Frame2)
            self.bill_reject.place(relx=0.83, rely=i*y, height=34, width=86)
            self.bill_reject.configure(activebackground="#d9d9d9")
            self.bill_reject.configure(activeforeground="#000000")
            self.bill_reject.configure(background="#d9d9d9")
            self.bill_reject.configure(disabledforeground="#a3a3a3")
            self.bill_reject.configure(foreground="#000000")
            self.bill_reject.configure(highlightbackground="#d9d9d9")
            self.bill_reject.configure(highlightcolor="black")
            self.bill_reject.configure(pady="0")
            self.bill_reject.configure(command=lambda i=i:self.update_rej(i-1))
            self.bill_reject.configure(text='''Reject''')

            self.btn1.append(self.bill_approve)
            self.btn2.append(self.bill_reject)
        

    def all(self):

        self.save_eno.clear()
        self.save_bno.clear()
        self.save_bstat.clear()
        self.save_amt.clear()
        self.save_remarks.clear()

        j=0
        for j in range(len(self.lbl1)):
            self.lbl1[j].destroy()
            self.lbl2[j].destroy()
            self.lbl3[j].destroy()
            self.lbl4[j].destroy()
            self.lbl5[j].destroy()
            self.btn1[j].destroy()
            self.btn2[j].destroy()

        self.lbl1.clear()
        self.lbl2.clear()
        self.lbl3.clear()
        self.lbl4.clear()
        self.lbl5.clear()
        self.btn1.clear()
        self.btn2.clear()

                 
        conn = c.connect("system/2824@localhost/xe")
        cur=conn.cursor()
        data=cur.execute("select * from requests where mno='"+self.m_no+"'")
        self.add_views(data)
        
    def app(self):
            
        self.save_eno.clear()
        self.save_bno.clear()
        self.save_bstat.clear()
        self.save_amt.clear()
        self.save_remarks.clear()

        j=0
        for j in range(len(self.lbl1)):
            self.lbl1[j].destroy()
            self.lbl2[j].destroy()
            self.lbl3[j].destroy()
            self.lbl4[j].destroy()
            self.lbl5[j].destroy()
            self.btn1[j].destroy()
            self.btn2[j].destroy()

        self.lbl1.clear()
        self.lbl2.clear()
        self.lbl3.clear()
        self.lbl4.clear()
        self.lbl5.clear()
        self.btn1.clear()
        self.btn2.clear()

        conn = c.connect("system/2824@localhost/xe")
        cur=conn.cursor()
        data=cur.execute("select * from requests where mno='"+self.m_no+"' and bill_status='Approved'")
        self.add_views(data)
            
    def rej(self):
        
        self.save_eno.clear()
        self.save_bno.clear()
        self.save_bstat.clear()
        self.save_amt.clear()
        self.save_remarks.clear()

        j=0
        for j in range(len(self.lbl1)):
            self.lbl1[j].destroy()
            self.lbl2[j].destroy()
            self.lbl3[j].destroy()
            self.lbl4[j].destroy()
            self.lbl5[j].destroy()
            self.btn1[j].destroy()
            self.btn2[j].destroy()

        self.lbl1.clear()
        self.lbl2.clear()
        self.lbl3.clear()
        self.lbl4.clear()
        self.lbl5.clear()
        self.btn1.clear()
        self.btn2.clear()
        
        conn = c.connect("system/2824@localhost/xe")
        cur=conn.cursor()
        data=cur.execute("select * from requests where mno='"+self.m_no+"' and bill_status='Rejected'")
        self.add_views(data)

    def pend(self):
        
        self.save_eno.clear()
        self.save_bno.clear()
        self.save_bstat.clear()
        self.save_amt.clear()
        self.save_remarks.clear()

        j=0
        for j in range(len(self.lbl1)):
            self.lbl1[j].destroy()
            self.lbl2[j].destroy()
            self.lbl3[j].destroy()
            self.lbl4[j].destroy()
            self.lbl5[j].destroy()
            self.btn1[j].destroy()
            self.btn2[j].destroy()

        self.lbl1.clear()
        self.lbl2.clear()
        self.lbl3.clear()
        self.lbl4.clear()
        self.lbl5.clear()
        self.btn1.clear()
        self.btn2.clear()
               
        conn = c.connect("system/2824@localhost/xe")
        cur=conn.cursor()
        data=cur.execute("select * from requests where mno='"+self.m_no+"' and bill_status='Pending'")
        self.add_views(data)
        conn.close()
    def update_app(self,pos):
        print(self.save_bno[pos])
        conn = c.connect("system/2824@localhost/xe")
        cur=conn.cursor()
        cur.execute("update requests set bill_status = 'Approved' where bill_no='"+self.save_bno[pos]+"'")
        conn.commit()
        conn.close()
        self.lbl3[pos].configure(fg="green")
        self.lbl3[pos].configure(text="Approved")

        server=s.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()

        server.login("budget.approval.system.project@gmail.com",'Budget@python07')

        text='\nBill No. : '+self.save_bno[pos]+' has been approved by your manager.\n\nEmployee No. : '+self.save_eno[pos]+'\nBill No. : '+self.save_bno[pos]+'\nBill Amount : '+str(self.save_amt[pos])+'\nBill Remarks : '+self.save_remarks[pos]+'\nBill Status : Approved';
        
        msg = """From: %s\nTo: %s\nSubject: %s\n\n%s""" %('budget.approval.system.project@gmail.com', ",", 'Bill Status Updated', text)

        server.sendmail("budget.approval.system.project@gmail.com",'16bit159@nirmauni.ac.in',msg)
        server.quit()
        
    def update_rej(self,pos):
        print(self.save_bno[pos])
        conn = c.connect("system/2824@localhost/xe")
        cur=conn.cursor()
        cur.execute("update requests set bill_status = 'Rejected' where bill_no='"+self.save_bno[pos]+"'")
        conn.commit()
        conn.close()
        self.lbl3[pos].configure(fg="red")
        self.lbl3[pos].configure(text="Rejected")

        server=s.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()

        server.login("budget.approval.system.project@gmail.com",'Budget@python07')

        text='\nBill No. : '+self.save_bno[pos]+' has been Rejected by your manager.\n\nEmployee No. : '+self.save_eno[pos]+'\nBill No. : '+self.save_bno[pos]+'\nBill Amount : '+str(self.save_amt[pos])+'\nBill Remarks : '+self.save_remarks[pos]+'\nBill Status : Rejected';
        
        msg = """From: %s\nTo: %s\nSubject: %s\n\n%s""" %('budget.approval.system.project@gmail.com', ",", 'Bill Status Updated', text)

        server.sendmail("budget.approval.system.project@gmail.com",'16bit159@nirmauni.ac.in',msg)
        server.quit()

    def print_bills(self):
        
        conn = c.connect("system/2824@localhost/xe")
        cur=conn.cursor()
        data=cur.execute("select * from requests where mno='"+self.m_no+"' and bill_status='Approved'")
        if(data.fetchone()):
            print("Generating!")
            bg.generate()
        else:
            messagebox.showinfo('Error','Please approve bills first!')
        conn.close()

        messagebox.showinfo('Successful','Bill Successfully Generated!')

        
if __name__ == '__main__':
    vp_start_gui()


