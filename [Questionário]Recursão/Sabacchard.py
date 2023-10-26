num = int(input())
aux = input().split(' ')
cartas = []
for i in aux:
    cartas.append(int(i))
cartas.sort(reverse=True)
i = sum(cartas[:int(num/2)])
print(i)