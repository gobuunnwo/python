# format関数（https://qiita.com/Morio/items/b79ead5f881e6551d9e1）

# ①
maximum = int(input("please enter any maximum value"))
for number in range(1,maximum+1):
    if(number%2!=0):
        print("{0}".format(number))

# ②
apple = 100
orange =50
total =apple + orange
print("合計{}円".format(total))

# ③
apple = 100
orange = 50
total =apple + orange
print("りんご{}円　みかん{}円 合計{}円".format(apple,orange,total))

# ④数値表現
# b   | 2進数で出力
# d   |10進数で出力
# o   |8進数で出力
# x(X)|16進数で出力
decimal = 106
print('{0}は2進数だと{0:b}、8進数だと{0:o}、16進数だと{0:X}'.format(decimal))

# ⑤幅
# 型名	  |説明
# <任意の幅|任意の幅を取り、左詰め
# >任意の幅|任意の幅を取り、右詰め
# ^任意の幅|任意の幅を取り、中央寄せ




