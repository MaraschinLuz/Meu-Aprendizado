s = 0
while True:
    a = input().split()
    t = []
    if a == ['0']:
        break
    for i in a:
        t.append(str(len(i)))
        if len(i) >= s:
            s = len(i)
            b = i
    p = '-'.join(t)
    print(p)
print()
print('The biggest word: %s' % b)
    

    
    
    
