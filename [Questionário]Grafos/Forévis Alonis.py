tabela = []
for i in range(V):
    tabela.append([])
    for j in range(V):
        tabela[i].append(0)
for i in range(A):
    if T == "N":
        X, Y, P = input().split(" ")
        X, Y, P = int(X), int(Y), int(P)
        tabela[X-1][Y-1] = tabela[Y-1][X-1] = P
    elif T == "D":
        X, Y, P = input().split(" ")
        X, Y, P = int(X), int(Y), int(P)
        tabela[X-1][Y-1] = P