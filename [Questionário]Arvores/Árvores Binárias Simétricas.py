def inorder(tree):
    global string
    if tree.esq:
        inorder(tree.esq)
    if tree.dado == None:
        pass
    else:
        string += str(tree.dado)
    if tree.dir:
        inorder(tree.dir)

def verificaSimetria(raiz):
    global string
    string = ""
    inorder(raiz)
    #print(string)
    if len(string) == 1:
        return True
    else:
        for i in range(int(len(string)/2)):
            if string[i] != string[-(i+1)]:
                return False
            else:
                return True