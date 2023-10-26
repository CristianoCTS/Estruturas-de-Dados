def fibonacci(x):
    if x == 0:
        return [0]
    if x == 1:
        return [0,1]
    else:
        lista = [0, 1]
        i = (len(lista)-1)
        while i < x:
            num = lista[i] + lista[i-1]
            lista.append(num)
            i = (len(lista)-1)
        return lista
x = int(input())
aux = fibonacci(x)
aux2 = aux[::-1]
num_chamadas = 1
print(f'fibonacci({x}) = {aux[-1]}.')
if x == 0:
    print(f'1 chamada(s) a fibonacci(0).')
else:
    print(f'{aux2[1]} chamada(s) a fibonacci(0).')
j = 0
for i in range(1, x + 1):
    print(f'{aux2[j]} chamada(s) a fibonacci({i}).')
    j += 1