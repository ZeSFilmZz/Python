print('------โปรแกรมคำนวณผ่อนบ้าน------')
try:
    Time = int(input('ต้องการผ่อนบ้านกี่ปี :'))
    Debt = int(input('ต้องการกู้เงินกี่บาท :'))
    Interest = float(input('ดอกเบี้ยกี่% :'))
except:
    print('กรุณากรอกข้อมูลเป็นตัวเลขเท่านั้น')
    Time = int(input('ต้องการผ่อนบ้านกี่ปี :'))
    Debt = int(input('ต้องการกู้เงินกี่บาท :'))
    Interest = float(input('ดอกเบี้ยกี่% :'))
    
print('------Calculate------')

Interest_per_month = Interest/(12*100)
x = (1+Interest_per_month)**(-1)
payment = Debt*(1-x)/(x*(1-x**(Time*12)))

print('ถ้าคุณกู้เงินซื้อบ้าน {:,d} บาท โดยผ่อนบ้านเป็นระยะเวลา {} ปี คุณจะต้องผ่อนเดือนละ {:,.2f} บาท'.format(Debt,Time,payment))
