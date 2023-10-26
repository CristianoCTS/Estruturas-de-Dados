Efalso = None
def listas(node):
    no = []
    if node.esq:
        no.append(node.esq.dado)
    if node.dado:
        no.append(node.dado)
    if node.dir:
        no.append(node.dir.dado)
    return no

def emordem(lista):
    if len(lista) == 0:
        return True
    if len(lista) == 1:
        return True
    if len(lista) == 2:
        if lista[0] < lista[1]:
            return True
        else:
            return False
    if len(lista) == 3:
        if (lista[0] < lista[1]) and ((lista[1] < lista[2])):
            return True
        else:
            return False

def auxiliar(tree):
    global Efalso
    if tree.esq:
        auxiliar(tree.esq)
    if tree.dado == None:
        pass
    else:
        #print(f" arvore: {listas(tree)} valida: {emordem(listas(tree))}")
        if emordem(listas(tree)) == False:
            Efalso = "TRUE"
            return False
    if tree.dir:
        auxiliar(tree.dir)

def constituiArvoreBinariaDeBusca(raiz):
    global Efalso
    Efalso = None
    aux = auxiliar(raiz)
    if Efalso:
        return False
    else:
        return True
