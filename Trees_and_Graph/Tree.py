__author__ = 'SunnyYan'

class TreeNode:

    def __init__(self,parent,key):
        self.parent = parent
        self.key = key
        self.leftChild = None
        self.rightChild = None
        self.state = None
        self.visited = False

    def getKey(self):
        return self.key

    def setParent(self,parent):
        self.parent = parent

    def setleftChild(self, leftChild):
        self.leftChild = leftChild

    def setrightChild(self, rightChild):
        self.rightChild = rightChild

    def printSubtree(self, space):
        if(self.rightChild != None):
            self.rightChild.printSubtree(space + 3)
        for i in range(0,space):
            print "-",
        print self.key
        if(self.leftChild != None):
            self.leftChild.printSubtree(space + 3)




class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def insertion(self, key):
        node = self.root
        if(self.root == None):
            self.root = TreeNode(None,key)
        while(node != None):
            if(key <= node.key):
                if(node.leftChild != None):
                    node = node.leftChild
                else:
                    node.leftChild = TreeNode(node,key)
                    self.size += 1
                    return
            else:
                if(node.rightChild != None):
                    node = node.rightChild
                else:
                    node.rightChild = TreeNode(node,key)
                    self.size += 1
                    return



# Testing Part...
# Generated a Binary Search Tree...
#TreeRoot = BinarySearchTree()
#l = [2,3,5,7,2,3,4,5,9,0,3,5,6,2,4,5]
#for i in l:
#    TreeRoot.insertion(i)
#
#TreeRoot.root.printSubtree(5)

