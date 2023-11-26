# -*- coding: utf-8 -*-
"""

Automatically generated by Colaboratory.


"""

class BinaryTree:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None

    def insertNode(self, value):
        if value < self.key and self.left == None:
            self.left = BinaryTree(value)
        elif value < self.key and self.left != None:
            self.left.insertNode(value)
        elif value >self.key and self.right == None:
            self.right = BinaryTree(value)
        elif value >self.key and self.right != None:
            self.right.insertNode(value)

    def preOrder(self):
        print(self.key)
        if self.left!=None:
            self.left.preOrder()
        if self.right!=None:
            self.right.preOrder()

    def inOrder(self):
        if self.left!=None:
            self.left.inOrder()
        print(self.key)
        if self.right!=None:
            self.right.inOrder()

    def posOrder(self):
        if self.left!=None:
            self.left.posOrder()
        if self.right!=None:
            self.right.posOrder()
        print(self.key)

    def searchValue(self, value):
        if self.key==value:
            print("Achei!!!")
        elif value>self.key and self.right!=None:
            self.right.searchValue(value)
        elif value<self.key and self.left!=None:
            self.left.searchValue(value)

    def caminho(self, value, path=[]):

        path.append(self.key)
        if self.key == value:
            print("Caminho:", path)
        elif value < self.key and self.left is not None:
            self.left.caminho(value, path)
        elif value > self.key and self.right is not None:
            self.right.caminho(value, path)
        else:
            print("Valor não encontrado no caminho.")

    def remover(self, value):

        if value < self.key:
            if self.left is not None:
                self.left = self.left.remover(value)
        elif value > self.key:
            if self.right is not None:
                self.right = self.right.remover(value)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            temp = self.right
            while temp.left is not None:
                temp = temp.left

            self.key = temp.key

            self.right = self.right.remover(temp.key)

        return self



#criando um nó
raiz = BinaryTree(20)
raiz.insertNode(10)
raiz.insertNode(8)
raiz.insertNode(15)
raiz.insertNode(40)
raiz.insertNode(30)
raiz.insertNode(50)

#
print("Pre-Ordem")
raiz.preOrder()
print("Em Ordem")
raiz.inOrder()
print("Pos-Ordem")
raiz.posOrder()
#Testando do Caminho
print("\n")
valor_procurado = 30
raiz.caminho(valor_procurado)
#Testando o Remover
valor_remover = 40
raiz.remover(valor_remover)

print(f"\nÁrvore após remover {valor_remover}:\n")
raiz.inOrder()