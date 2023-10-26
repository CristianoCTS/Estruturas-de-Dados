print('=> restaurante aberto')
mesas, mesas_por_area, cardapio, estoque, pedidos_mesa = {}, {}, {}, {}, {}
mesas_alfabética, cardapio_alfabético, estoque_alfabético, pedidos_mesa_alfabético, pedidos_restaurante = [], [], [], [], []
numero_pedido = 0
aberto = True
while aberto:
    comando = input()
    
    if comando == "+ atualizar mesas":
        nome_do_arquivo = input()
        file1 = open(nome_do_arquivo, "r")
        mesas_lista = file1.readlines()
        file1.close()
#        print(f"mesas_lista: {mesas_lista}")
        for c in mesas_lista:
            c = c[:-1].split(", ") if '\n' in c else c.split(", ")
            if int(c[0]) not in mesas:
                mesas[int(c[0])] = c[1:]
                if c[1] in mesas_por_area:
                    mesas_por_area[c[1]].append(int(c[0]))
                    mesas_por_area[c[1]].sort()
                else:
                    mesas_alfabética.append(c[1])
                    mesas_por_area[c[1]] = [int(c[0])]
                    mesas_alfabética.sort()
            else:
                mesas_por_area[mesas[int(c[0])][0]].remove(int(c[0]))
                mesas[int(c[0])] = c[1:]
                if c[1] in mesas_por_area:
                    mesas_por_area[c[1]].append(int(c[0]))
                    mesas_por_area[c[1]].sort()
                else:
                    mesas_alfabética.append(c[1])
                    mesas_por_area[c[1]] = [int(c[0])]
                    mesas_alfabética.sort()
#        print(f"mesas: {mesas}")
#        print(f"mesas_por_area: {mesas_por_area}")
#        print(f"mesas_alfabética: {mesas_alfabética}")
        
    elif comando == "+ atualizar cardapio":
        nome_do_arquivo = input()
        file2 = open(nome_do_arquivo, "r")
        cardapio_lista = file2.readlines()
        file2.close()
#        print(f"cardapio_lista: {cardapio_lista}")
        for c in cardapio_lista:
            c = c[:-1].split(", ") if '\n' in c else c.split(", ")
            cardapio[c[0]] = {}
            for d in sorted(c[1:]):
                if d not in cardapio[c[0]]:
                    cardapio[c[0]][d] = 1
                else:
                    cardapio[c[0]][d] += 1
            if c[0] not in cardapio_alfabético:
                cardapio_alfabético.append(c[0])
        cardapio_alfabético.sort()
#        print(f"cardapio: {cardapio}")
#        print(f"cardapio_alfabético: {cardapio_alfabético}")
        
    elif comando == "+ atualizar estoque":
        nome_do_arquivo = input()
        file3 = open(nome_do_arquivo, "r")
        estoque_lista = file3.readlines()
        file3.close()
#        print(f"estoque_lista: {estoque_lista}")
        for c in estoque_lista:
            c = c[:-1].split(", ") if '\n' in c else c.split(", ")
            if c[0] in estoque:
                estoque[c[0]] += int(c[1])
            else:
                estoque[c[0]] = int(c[1])
                estoque_alfabético.append(c[0])
                estoque_alfabético.sort()
#        print(f"estoque: {estoque}")
#        print(f"estoque_alfabético: {estoque_alfabético}")
        
    elif comando == "+ relatorio mesas":
        if mesas_alfabética == []:
            print("- restaurante sem mesas")
        else:
            for c in mesas_alfabética:
                print(f"area: {c}")
                if mesas_por_area[c] == []:
                    print("- area sem mesas")
                else:
                    for d in mesas_por_area[c]:
                        print(f"- mesa: {d}, status: {mesas[d][1]}")

    elif comando == "+ relatorio cardapio":
        if cardapio_alfabético == []:
            print("- cardapio vazio")
        else:
            for c in cardapio_alfabético:
                print(f"item: {c}")
                for d in cardapio[c]:
                    print(f"- {d}: {cardapio[c][d]}")

    elif comando == "+ relatorio estoque":
        if estoque_alfabético == []:
            print("- estoque vazio")
        else:
            estoque_vazio = True
            for c in estoque_alfabético:
                if estoque[c] > 0:
                    print(f"{c}: {estoque[c]}")
                    estoque_vazio = False
            if estoque_vazio:
                print("- estoque vazio")

    elif comando == "+ fazer pedido":
        mesa, item = input().split(", ")
        if int(mesa) not in mesas:
            print(f"erro >> mesa {int(mesa)} inexistente")
        elif mesas[int(mesa)][1] == 'livre':
            print(f"erro >> mesa {int(mesa)} desocupada")
        elif item not in cardapio:
            print(f"erro >> item {item} nao existe no cardapio")
        else:
            pedido_possivel = True
            for c in cardapio[item]:
                try:
                    if estoque[c] < cardapio[item][c]:
                        print(f"erro >> ingredientes insuficientes para produzir o item {item}")
                        pedido_possivel = False
                        break
                except KeyError:
                    print(f"erro >> ingredientes insuficientes para produzir o item {item}")
                    pedido_possivel = False
                    break
            if pedido_possivel:
                print(f"sucesso >> pedido realizado: item {item} para mesa {mesa}")
                if int(mesa) in pedidos_mesa:
                    pedidos_mesa[int(mesa)].append(item)
                else:
                    pedidos_mesa[int(mesa)] = [item]
                if int(mesa) not in pedidos_mesa_alfabético:
                    pedidos_mesa_alfabético.append(int(mesa))
                numero_pedido += 1
                pedidos_restaurante.append([numero_pedido, int(mesa), item])
                for c in cardapio[item]:
                    estoque[c] -= 1

    elif comando == "+ relatorio pedidos":
        if pedidos_mesa_alfabético == []:
            print("- nenhum pedido foi realizado")
        else:
            for i in sorted(pedidos_mesa_alfabético):
                print(f"mesa: {i}")
                for c in sorted(pedidos_mesa[i]):
                    print(f"- {c}")

    elif comando == "+ fechar restaurante":
        if pedidos_restaurante == []:
            print("- historico vazio")
        else:
            for c in pedidos_restaurante:
                print(f"{c[0]}. mesa {c[1]} pediu {c[2]}")
        print("=> restaurante fechado")
        aberto = False

    else:
        print("erro >> comando inexistente")