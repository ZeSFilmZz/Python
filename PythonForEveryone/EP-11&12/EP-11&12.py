import csv
import os 

path = os.getcwd()
picicon = os.path.join(path,'Pixelkit-Swanky-Outlines-06-Wallet.ico')

#ฟังก์ชั่นสร้างไฟล์csv
def write_csv(data):
    csvfile = os.path.join(path,'Revenue Accounts.csv')
    with open(csvfile,'a',newline='',encoding='utf-8') as file:
        fw =csv.writer(file)
        fw.writerow(data)

from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import timedelta

#สร้างหน้าต่างGUI
GUI = Tk()
GUI.title('โปรแกรมบันทึกรายรับรายจ่าย')
GUI.geometry('500x500')
GUI.iconbitmap(picicon)

#สร้าเฟรม
F1 = Frame(GUI)
F1.place(x=45,y=20)

#วันที่
L0 = ttk.Label(F1,text='วันที่',font=('Angsana New',20))
L0.pack()

cal = DateEntry(F1, width=12, background='darkblue', foreground='white', borderwidth=2)
cal.pack()

#รายรับหรือรายจ่าย
ttk.Label(F1,text='\n',font=('Angsana New',3)).pack()
L1 = ttk.Label(F1,text='รายรับหรือรายจ่าย',font=('Angsana New',20))
L1.pack()

options = ['รายรับ','รายจ่าย']
combo = ttk.Combobox(F1,values=options)
combo.pack()
combo.set("รายรับหรือรายจ่าย")

#ยอดเงิน
ttk.Label(F1,text='\n',font=('Angsana New',3)).pack()
L2 = ttk.Label(F1,text='ใส่ยอดเงิน',font=('Angsana New',20))
L2.pack()

v_value = StringVar()

E2 = ttk.Entry(F1,textvariable=v_value,font=('Angsana New',18),width=15)
E2.pack()

#รายละเอียดเพิ่มเติม
ttk.Label(F1,text='\n',font=('Angsana New',3)).pack()
L3 = ttk.Label(F1,text='รายละเอียดเพิ่มเติม',font=('Angsana New',20))
L3.pack()

T1 = Text(F1,font=('Angsana New',18),height=4,width=50)
T1.pack()

#ฟังก์ชั่นบันทึกผล
def save():
    date = cal.get_date()
    title = combo.get()
    value = v_value.get()
    textbox = T1.get(1.0,"end-1c")
    print(date)
    print(title)
    print(value)
    print(textbox)
    data = [date,title,value,textbox]
    write_csv(data)
    combo.set("รายรับหรือรายจ่าย")
    v_value.set('')
    T1.delete(1.0,END)

#ปุ่มsave
B1 = ttk.Button(F1,text='บันทึก',command=save)
B1.pack(pady=10)

#--------------------------------
#--------Button Flashcard--------

#ฟัก์ชั่นอ่านไฟล์csv
def readcsv():
    csvfile = os.path.join(path,'Revenue Accounts.csv')
    with open(csvfile,newline='',encoding='utf-8') as file:
        fr = csv.reader(file)
        data = list(fr)
        return data

revenuelist = readcsv()
#print(revenuelist)
#สร้างฟังก์ชั่นรวมรายการบันทึกรายรับรายจ่ายในแต่ละวัน
def sumrevenuelist(rlist,date):
    sumlist =''
    for i in rlist:
        if i[0]==date :
            sumlist += i[1]+"\t"+i[2]+"บาท"+"\t\t"+i[3]+"\n"
    return sumlist
#print(sumrevenuelist(revenuelist,'2023-11-11'))

global countindex
countindex = cal.get_date()
#สร้างฟังก์ชั่นแสดงหน้าต่างใหม่
def Flashcard():
    revenuelist = readcsv()
    global countindex
    countindex = cal.get_date()
    GUI2 = Toplevel()
    GUI2.title('ประวัติรายรับรายจ่าย')
    GUI2.geometry('400x400')
    GUI2.iconbitmap(picicon)
    
    vtext_title = StringVar()
    vtext_detail = StringVar()
    title = ttk.Label(GUI2,textvariable=vtext_title,font=('Angsana New',20,'bold'))
    title.pack()
    vtext_title.set('รายรับรายจ่ายของวันที่'+" "+countindex.strftime("%Y-%m-%d"))
    detail = ttk.Label(GUI2,textvariable=vtext_detail)
    detail.pack()
    vtext_detail.set(sumrevenuelist(revenuelist,countindex.strftime("%Y-%m-%d")))

    #ฟังก์ชั่นปุ่มกดไปดูรายรับรายจ่ายวันก่อนหน้า
    def Prev():
        global countindex
        countindex = countindex - timedelta(days=1)
        vtext_title.set('รายรับรายจ่ายของวันที่'+" "+countindex.strftime("%Y-%m-%d"))
        vtext_detail.set(sumrevenuelist(revenuelist,countindex.strftime("%Y-%m-%d")))
    def Next():
        global countindex
        countindex = countindex + timedelta(days=1)
        vtext_title.set('รายรับรายจ่ายของวันที่'+" "+countindex.strftime("%Y-%m-%d"))
        vtext_detail.set(sumrevenuelist(revenuelist,countindex.strftime("%Y-%m-%d")))
    BPrev = ttk.Button(GUI2,text='<',command=Prev)
    BPrev.place(x=10,y=350)
    BNext = ttk.Button(GUI2,text='>',command=Next)
    BNext.place(x=314,y=350)
  
    GUI2.mainloop()


#ปุ่มกด
picbutton = os.path.join(path,'Pixelkit-Swanky-Outlines-06-Wallet.png')
pic = PhotoImage(file=picbutton)
BFlashcard = ttk.Button(GUI,image=pic,command=Flashcard)
BFlashcard.place(x=460,y=10)

GUI.mainloop()