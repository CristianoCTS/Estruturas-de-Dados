atividades = input().split(" ")
tempo = int(input())
afazeres = {}
prioridades = []
for i in range(len(atividades)):
    try:
        if int(atividades[i]) in afazeres:
            afazeres[int(atividades[i])].append(atividades[i-1])
        else:
            afazeres[int(atividades[i])] = [atividades[i-1]]
            prioridades.append(int(atividades[i]))
    except:
        pass
prioridades.sort()
# print(f'atividades: {atividades}')
# print(f'tempo: {tempo}')
# print(f'afazeres: {afazeres}')
# print(f'prioridades: {prioridades}')
if int(len(atividades)/2) > tempo:
    print(f"Tamanho da fila: {int((len(atividades)/2) - tempo)}")
else:
    print(f"Tamanho da fila: {0}")
for i in prioridades:
    for j in afazeres[i]:
        if tempo <= 0:
            print(f"Atividade: {j}, Prioridade: #{i}")
        else:
            tempo -= 1