from tkinter import *
from tkinter import ttk
GUI = Tk()
GUI.title('โปรแกรมบันทึกรายรับรายจ่าย')
GUI.geometry('500x500')

L1 = ttk.Label(GUI,text='รายรับหรือรายจ่าย \n - รายรับพิมพ์ "i"\n - รายจ่ายพิมพ์ "o"',font=('Angsana New',20))
L1.pack()

E1 = ttk.Entry(GUI,font=('Angsana New',18),width=5)
E1.pack()

ttk.Label(GUI,text='\n',font=('Angsana New',3)).pack()
L2 = ttk.Label(GUI,text='ใส่ยอดเงิน',font=('Angsana New',20))
L2.pack()

E2 = ttk.Entry(GUI,font=('Angsana New',18),width=15)
E2.pack()

ttk.Label(GUI,text='\n',font=('Angsana New',3)).pack()
L3 = ttk.Label(GUI,text='รายละเอียดเพิ่มเติม',font=('Angsana New',20))
L3.pack()

T1 = Text(GUI,font=('Angsana New',18),height=4,width=50)
T1.pack()

B1 = ttk.Button(GUI,text='บันทึก')
B1.pack(pady=10)

GUI.mainloop()