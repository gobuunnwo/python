# rangeの使い方(https://note.nkmk.me/python-range-usage/)

# ①
# 0<= n <20
for n in range(0,20):
    print(n)

# ②
# 0<= n <20 ＆　+2ずつ
for n in range(0,20,2):
    print(n)

# ③
# A=0,B=1...
lists=["A","B","C","D","E"]
for n in range(1,3):
    print(n,lists[n])
for n in range(len(lists)):
    print(n,lists[n])













