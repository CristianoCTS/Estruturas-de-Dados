tamanho_lista = int(input())
lista = input().split()
for i in range(len(lista)):
    lista[i] = int(lista[i])
janela = int(input())
slice_da_lista = lista[:janela]
maiores_numeros = str(max(slice_da_lista[-janela:]))

for i in range(janela , tamanho_lista):
    slice_da_lista.append(lista[i])
    maiores_numeros += '  ' + str((max(slice_da_lista[-janela:])))
print(maiores_numeros)
    
