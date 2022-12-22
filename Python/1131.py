vi = 0
vg = 0
e = 0
while True:
    gi, gg = input().split()
    gi = int(gi)
    gg = int(gg)
    if gi==gg:
        e += 1
    else:
        if gi > gg:
            vi += 1
        else:
            vg += 1
    print('Novo grenal (1-sim 2-nao)')
    a = int(input())
    if (a==2):
        break
print(f'{vi+vg+e} grenais')
print(f'Inter:{vi}')
print(f'Gremio:{vg}')
print(f'Empates:{e}')

if vi > vg:
    print('Inter venceu mais')
elif vi < vg:
    print('Gremio venceu mais')
elif vi == vg:
    print('Nao houve vencedor')
        
    