a = 15
for i in range(0,3):
    print('請猜一個數字:')
    b=int(input())
    if a == b:
        print('bingo!!')
        break
if a != b:
    print('哈哈 沒猜到!')
