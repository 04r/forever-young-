import time

x = int(input("Nummer"))

for i in range(1,11):
    print(x * i)

time.sleep(1)

for i in range(0,30):
    time.sleep(1)
    print(i)

time.sleep(1)

for i in range(1,24):
    am = 'AM'
    pm = 'PM'
    if i < 12:
        print('{} {}'.format(i, am))
    else:
        print('{} {}'.format(i, pm))


for i in range(20,50):
    if i % 10 == 0: 
        print('{}'.format(i))