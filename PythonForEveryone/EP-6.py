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
    
def cal_instalment(t,d,i=3):
    Interest_per_month = i/(12*100)
    x = (1+Interest_per_month)**(-1)
    payment = d*(1-x)/(x*(1-x**(t*12)))
    return payment

print('------Calculate------')
print('ถ้าคุณกู้เงินซื้อบ้าน {:,d} บาท โดยผ่อนบ้านเป็นระยะเวลา {} ปี ดอกเบี้ย {}%ต่อปี คุณจะต้องผ่อนเดือนละ {:,.2f} บาท'.format(Debt,Time,Interest,cal_instalment(Time,Debt,Interest)))