from random import  randint

#ダイスを振る関数dice()を定義
def dice() :
    num = randint(1,6)
    return num

#dice()を5回呼び出す
for i in range(5) :
    result = dice()
    print(result)
