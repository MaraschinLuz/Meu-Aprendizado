n = int(input())
vet = list(map(int, input().split()))
menor = vet[0]
im = 0
for i in range (1, n):
    if vet[i] < menor:
        menor = vet[i]
        im = i
print(f'Menor valor: {menor}')
print(f'Posicao: {im}')