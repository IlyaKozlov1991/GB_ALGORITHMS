# Red-black binary tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.red = False
        self.parent = None

class rb_tree:
    def __init__(self):
        self.null = Node(0)
        self.null.red = False
        self.null.red = None
        self.null.left = None
        self.root = self.null

    def insert(self, data):
        new_node = Node(data)
        new_node.parent = None
        new_node.left = self.null
        new_node.right = self.null
        new_node.red = True

        parent = None
        root = self.root
        while root != self.null:
            parent = root
            if new_node.data < root.data:
                root = root.left
            elif new_node.data > root.data:
                root = root.right
            else:
                return
            
        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node
        
        self.balance_tree(new_node)
    
    def rotate_left(self, node):
        temp = node.right
        node.right = temp.left
        if temp.left != self.null:
            temp.left.parent = node
        
        temp.parent = node.parent
        if node.parent is None:
            self.root = temp
        elif node == node.parent.left:
            node.parent.left = temp
        else:
            node.parent.right = temp
        temp.left = node
        node.parent = temp

    def rotate_right(self, node):
        temp = node.left
        node.left = temp.right
        if temp.right != self.null:
            temp.right.parent = node

        temp.parent = node.parent
        if node.parent is None:
            self.root = temp
        elif node == node.parent.right:
            node.parent.right == temp
        else:
            node.parent.left = temp
        temp.right = node
        node.parent = temp

    def balance_tree(self, new_node):
            while new_node != self.root and new_node.parent.red:
                if new_node.parent == new_node.parent.parent.right:
                    temp = new_node.parent.parent.left
                    if temp.red:

                        temp.red = False
                        new_node.parent.red = False
                        new_node.parent.parent.red = True
                        new_node = new_node.parent.parent
                    else:
                        if new_node == new_node.parent.left:
                            new_node = new_node.parent
                            self.rotate_right(new_node)
                        new_node.parent.red = False
                        new_node.parent.parent.red = True
                        self.rotate_left(new_node.parent.parent)
                else:
                    temp = new_node.parent.parent.right

                    if temp.red:
                        temp.red = False
                        new_node.parent.red = False
                        new_node.parent.parent.red = True
                        new_node = new_node.parent.parent
                    else:
                        if new_node == new_node.parent.right:
                            new_node = new_node.parent
                            self.rotate_left(new_node)
                        new_node.parent.red = False
                        new_node.parent.parent.red = True
                        self.rotate_right(new_node.parent.parent)
            self.root.red = False
