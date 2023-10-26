V, A, T = input().split(" ")
V, A = int(V), int(A)
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
    #print(f"-----------------------------------")
    #print(f"tabela[{X}][{Y}] = {tabela[X-1][Y-1]}")
    #print(f"tabela[{Y}][{X}] = {tabela[Y-1][X-1]}")
    #print(f"-----------------------------------")
#impressão da tabela funcionando
for i in range(V):
    for j in range(V):
        if tabela[i][j] < 10:
            espaco = "   "
        elif tabela[i][j] < 100:
            espaco = "  "
        elif tabela[i][j] < 1000:
            espaco = " "
        print(espaco + str(tabela[i][j]), end="")
    print("")
    