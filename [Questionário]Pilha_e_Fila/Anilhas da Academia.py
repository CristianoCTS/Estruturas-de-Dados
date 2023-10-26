rack = []
anilha_desejada = None
while True:
    try:
        anilhas = int(input())
    except:
        break
    if anilhas != 0:
        rack.append(anilhas)
    else:
        anilha_desejada = int(input())
        break
if rack != []:
    peso_movimentado = 0
    anilhas_retiradas = 0
    for i in rack[::-1]:
        print(f'Peso retirado: {i}')
        anilhas_retiradas += 1
        peso_movimentado += i
        if i == anilha_desejada:
            break
    print(f'Anilhas retiradas: {anilhas_retiradas}')
    print(f'Peso total movimentado: {peso_movimentado}')
else:
    print(f'Peso retirado: {0}')
    print(f'Anilhas retiradas: {0}')
    print(f'Peso total movimentado: {0}')