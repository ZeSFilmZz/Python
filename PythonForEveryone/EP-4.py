num = input('ต้องการอนุการfibonanciกี่ตัว :')
fibo_list = [0,1]
golden_list = []
def fibo(n) :
    for c in range (n-2):
        fibo_list.append(fibo_list[c]+fibo_list[c+1])

def golden_ratio() :
    for c in range(1,len(fibo_list)-1):
        golden_list.append('%.2f'%(fibo_list[c+1]*100/fibo_list[c]))


fibo(int(num))
golden_ratio()
print('อนุกรมfibonanci',fibo_list)
print('ลำดับ golden ratio',golden_list)
