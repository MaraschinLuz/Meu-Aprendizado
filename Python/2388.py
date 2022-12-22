n = int(input())
dt = 0
for i in range(n):
    t, v = input().split()
    t = int(t)
    v = int(v)
    d = t*v
    dt += d
print(f'{dt}')