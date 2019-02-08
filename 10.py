# while文
name=20
age=2
while age<name:
    if name%2==0:
        print(age)
    age+=2

i=1
while i < 6:
    print(i)
    i+=1

i=1
while i<6:
    print(i)
    if i ==3:
        break
    i+=1

i=0
while i <6:
    i+=1
    if i==3:
        continue
    print(i)

i=0
while i<11:
    i+=1
    if i%2==0:
        continue
    print(i)