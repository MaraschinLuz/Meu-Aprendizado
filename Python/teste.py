n = int(input())

for i in range(0,n):
    num = int(input())
    y = 0
    x = 1
    while x <= num:
        if num % x == 0:
            y = y + 1
        x = x + 1
    if y > 2:
        print(f'{num} nao eh primo')
    else:
        print(f'{num} eh primo')