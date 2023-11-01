print('------โปรแกรมคำนวณผ่อนบ้านหรือรถ------')
def cal_instalment_house(t,d,i=3):
    Interest_per_month = i/(12*100)
    x = (1+Interest_per_month)**(-1)
    payment = d*(1-x)/(x*(1-x**(t*12)))
    return payment

def cal_instalment_car(t,d,i=3):
    payment = ((i*d*t/100)+d)/(12*t)
    return payment

product = input('ต้องการคำนวณซื้อบ้านหรือรถ (บ้าน พิมพ์ "h" , รถ พิมพ์ "c" ) :')
if product.lower()=='h':
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
    print('ถ้าคุณกู้เงินซื้อบ้าน {:,d} บาท โดยผ่อนบ้านเป็นระยะเวลา {} ปี ดอกเบี้ย {}%ต่อปี คุณจะต้องผ่อนเดือนละ {:,.2f} บาท'.format(Debt,Time,Interest,cal_instalment_house(Time,Debt,Interest)))
elif product.lower()=='c' :
    try:
        Time = int(input('ต้องการผ่อนรถกี่ปี :'))
        Debt = int(input('ต้องการกู้เงินกี่บาท :'))
        Interest = float(input('ดอกเบี้ยกี่% :'))
    except:
        print('กรุณากรอกข้อมูลเป็นตัวเลขเท่านั้น')
        Time = int(input('ต้องการผ่อนรถกี่ปี :'))
        Debt = int(input('ต้องการกู้เงินกี่บาท :'))
        Interest = float(input('ดอกเบี้ยกี่% :'))
    print('------Calculate------')
    print('ถ้าคุณกู้เงินซื้อรถ {:,d} บาท โดยผ่อนรถเป็นระยะเวลา {} ปี ดอกเบี้ย {}%ต่อปี คุณจะต้องผ่อนเดือนละ {:,.2f} บาท'.format(Debt,Time,Interest,cal_instalment_car(Time,Debt,Interest)))
else :
    print('------กรอกข้อมูลไม่ถูกต้อง------')



