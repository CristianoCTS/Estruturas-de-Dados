class tree():
    def __init__(self, value=None, left=None, right=None, root=None):
        self.root = root
        self.value = value
        self.left = left
        self.right = right
    def __str__(self):
        return "v:(" + str(self.value) + ") l:(" + str(self.left) + ") r:(" + str(self.right) + ")"
    def insert(self, insertion):
        if type(insertion) != type(2):
            print("error: binary tree - insertion class not supported")
        elif self.value == None:
            self.value = insertion
        elif insertion <= self.value:
            if self.left == None:
                self.left = tree(insertion, None, None, self)
            else:
                self.left.insert(insertion)
        elif insertion > self.value:
            if self.right == None:
                self.right = tree(insertion, None, None, self)
            else:
                self.right.insert(insertion)
    def isItin(self, item):
        if type(item) != type(2):
            print("error: binary tree - item class not supported")
        elif self.value == item:
            return True
        elif insertion <= self.value:
            if self.left == item:
                return True
            else:
                self.left.isItin(item)
        elif insertion > self.value:
            if self.right == item:
                return True
            else:
                self.right.isItin(item)
    def preorder(self):
        if self.value == None:
            print("", end="")
        else:
            print(str(self.value) + " ", end="")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    def inorder(self):
        if self.left:
            self.left.inorder()
        if self.value == None:
            print("", end="")
        else:
            print(str(self.value) + " ", end="")
        if self.right:
            self.right.inorder()
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        if self.value == None:
            print("", end="")
        else:
            print(str(self.value) + " ", end="")
        
arvore = tree()   
comandos = []
while True:
    comando = input()
    try:
        comando = int(comando)
        arvore.insert(comando)
    except:
        pass
    if comando == "quack":
        break
    elif type(comando) == type("str"):
        if comando == "in":
            arvore.inorder()
            print("")
        if comando == "pre":
            arvore.preorder()
            print("")
        if comando == "pos":
            arvore.postorder()
            print("")