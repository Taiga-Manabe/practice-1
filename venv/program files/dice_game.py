from random import  randint

#ダイスを振る関数dice()を定義
def dice() :
    num = randint(1,6)
    return num

#2個のダイスを5回振った結果
for i in range(5) :
    dice1 = dice()
    dice2 = dice()
    sum = dice1 + dice2
    print(f"{dice1}と{dice2}で合計{sum}")
