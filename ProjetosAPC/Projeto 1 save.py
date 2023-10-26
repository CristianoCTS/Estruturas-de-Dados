import copy
InicioCONFIGURAÇÂO = input()
espacos = []
while True:
    AreaMesasCadeiras = input()
    if (AreaMesasCadeiras == '--ATENDIMENTO'):
        break
    area, mesas, cadeiras = AreaMesasCadeiras.split(' ')
    amco = [area, int(mesas), int(cadeiras), 0]
    espacos.append(amco)
areas, analisando, analisando2, analisando3, tempo_de_permanencia = [], [], [], [], []
tempo, pessoas = 0, 0
#print('espacos =', espacos)
for i in range(len(espacos)):
        analisando.append(espacos[i][0])
        [areas.append(c) for c in analisando if c not in areas]
        areas.sort()
#print('areas =', areas)


while True:
    comandos = input()
    tempo=tempo+1
    
    
    for i in range(len(tempo_de_permanencia)):
        if tempo_de_permanencia[i][0]==tempo:
            espacos[tempo_de_permanencia[i][1]][3] -= 1


    if (comandos == '1'):
        analisando, analisando2, analisando3 = [], [], []
        comando1 = input().split()
        for i in range(len(espacos)):
            if (comando1[8]==espacos[i][0]) and (espacos[i][2]>=int(comando1[4])) and (espacos[i][3]<espacos[i][1]):
                analisando.append(espacos[i])
        analisando.sort(key=lambda x: x[2])
        if analisando == []:
            print('Nao foi possivel levar o grupo de clientes para uma mesa.')
        else:
            index_mesa = espacos.index(analisando[0])
            espacos[index_mesa][3] += 1
            tempo_de_permanencia.append([((2 * int(comando1[4])) + 2 + tempo), index_mesa, int(comando1[4]), comando1[8]])
            pessoas += int(comando1[4])
            print('Um grupo de ',comando1[4],' pessoas ocupou uma mesa de ',analisando[0][2],' lugares na area ',comando1[8],'.', sep='')
                
                
    elif (comandos == '2'):
        analisando, analisando2, analisando3 = [], [], []
        for i in range(len(areas)):
            rem=[]
            for j in range(len(espacos)):
                if (espacos[j][0]==areas[i]):
                    rem.append(espacos[j][1])
            analisando2.append(sum(rem))
        for i in range(len(areas)):
            M=0
            for j in range(len(tempo_de_permanencia)):
                if (tempo_de_permanencia[j][0]>tempo) and (tempo_de_permanencia[j][3]==areas[i]):
                    M += 1
            print(areas[i],': (',M,' de ',analisando2[i],' mesas)', sep='')
        
            
    elif (comandos == '3'):
        analisando, analisando2, analisando3 = [], [], []
        for i in range(len(areas)):
            rem=[]
            for j in range(len(tempo_de_permanencia)):
                if (tempo_de_permanencia[j][0]>tempo) and (tempo_de_permanencia[j][3]==areas[i]):
                    rem.append(tempo_de_permanencia[j][2])
            analisando2.append(sum(rem))
        for i in range(len(areas)):
            rem=[]
            for j in range(len(espacos)):
                if espacos[j][0]==areas[i]:
                    rem.append(espacos[j][1] * espacos[j][2])
            analisando3.append(sum(rem))
        for i in range(len(areas)):
            print(areas[i],': ','(',analisando2[i],' de ',analisando3[i],' pessoas)', sep='')
            
            
    elif (comandos == '4'):
        analisando, analisando2, analisando3 = [], [], []
        comando5 = input().split()
        if comando5[1]=='adicionar':
            OP='adicionadas'
            for i in range(len(espacos)):
                if (comando5[11]==espacos[i][0]) and (int(comando5[6])==espacos[i][2]):
                    analisando.append(espacos[i])
            if analisando==[]:
                espacos.append([comando5[11], int(comando5[3]), int(comando5[6]), 0])
                print(comando5[3], ' mesas de ',comando5[6], ' cadeiras ', OP, ' com sucesso na area ',comando5[11], '.', sep='')
            else:
                analisando.sort(key=lambda x: x[2])
                index_mesa = espacos.index(analisando[0])
                espacos[index_mesa][1] = analisando[0][1]+int(comando5[3])
                print(comando5[3], ' mesas de ',comando5[6], ' cadeiras ', OP, ' com sucesso na area ',comando5[11], '.', sep='')
        elif comando5[1]=='remover':
            OP='removidas'
            for i in range(len(espacos)):
                if (comando5[11]==espacos[i][0]) and (int(comando5[6])==espacos[i][2]):
                    analisando.append(espacos[i])
            if analisando==[]:
                print('ERROR: TENTANDO REMOVER MESAS QUE NÂO EXISTEM')
            else:
                index_mesa = espacos.index(analisando[0])
                espacos[index_mesa][1] -= int(comando5[3])
                print(comando5[3], ' mesas de ',comando5[6], ' cadeiras ', OP, ' com sucesso na area ',comando5[11], '.', sep='')
                
                
    elif comandos == '-1':
        for i in range(len(tempo_de_permanencia)):
            if tempo_de_permanencia[i][0]>tempo:
                espacos[tempo_de_permanencia[i][1]][3] -= 1
        break

print('Restaurante fechado.')
print('Balanco final de mesas:')

analisando, analisando2, analisando3 = [], [], []
for i in range(len(areas)):
    analisando2 = []
    for j in range(len(espacos)):
        if espacos[j][0] == areas[i]:
            analisando2.append(espacos[j])
        analisando2.sort(key=lambda x: x[2])
    print(areas[i], ':', sep='')
    for j in range(len(analisando2)):
        print(' ', analisando2[j][1], ' mesas de ', analisando2[j][2], ' cadeiras.', sep='')
print('Um total de', pessoas, 'pessoas visitaram o restaurante hoje.')
print('Bom descanso!')