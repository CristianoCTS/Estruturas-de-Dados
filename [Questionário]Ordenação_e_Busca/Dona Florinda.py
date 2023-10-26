Monitorando = False
numeroDEpretendentes = int(input())
alt, pes, sob, nom = [], [], [], []
pretendentes = []
def w(l):
    if l == 75:
        aux = 0
    elif l < 75:
        aux = (75 - l)
    else:
        aux = (l - 75)*100
    return aux
for i in range(numeroDEpretendentes):
    pretendente = input().split(" ")
    sobrenome, nome = pretendente[1], pretendente[0]
    peso = int(pretendente[3])
    altura = 180 - int(pretendente[2]) if 180 > int(pretendente[2]) else int(pretendente[2]) - 180
    if altura not in alt:
        alt.append(altura)
    if peso not in pes:
        pes.append(peso)
    if sobrenome not in sob:
        sob.append(sobrenome)
    if nome not in nom:
        nom.append(nome)
    pretendentes.append([altura, peso, sobrenome, nome])
alt.sort()
pes.sort(key=w)
sob.sort()
nom.sort()
if Monitorando:
    print(f"------------------------------------------------------------------")
    print(f"alt: {alt}")
    print(f"pes: {pes}")
    print(f"sob: {sob}")
    print(f"nom: {nom}")
    print(f"pretendentes: {pretendentes}")
    print(f"------------------------------------------------------------------")
    print(" ")
aux, aux2, aux3, aux4 = [], [], [], []
for i in alt:
    aux=[]
    for i2 in pretendentes:
        if i2[0] == i:
            aux.append(i2)
    print(f"{i}{aux}") if aux != [] and Monitorando else None
    for j in pes:
        aux2 =[]
        for j2 in aux:
            if j2[1] == j:
                aux2.append(j2)
            print(f"  {j}{aux2}") if aux2 != [] and Monitorando else None
        for k in sob:
            aux3 = []
            for k2 in aux2:
                if k2[2] == k:
                    aux3.append(k2)
                print(f"    {k}{aux3}") if aux3 != [] and Monitorando else None
            for l in nom:
                aux4 = []
                for l2 in aux3:
                    if l2[3] == l:
                        aux4.append(l2)
                    print(f"      {l}{aux4}") if aux4 != [] and Monitorando else None
                    print(f"      -------------------------------------------") if aux4 != [] and Monitorando else None
                    print(f"{aux4[0][2]}, {l}") if aux4 != [] else None
                    print(f"      -------------------------------------------") if aux4 != [] and Monitorando else None