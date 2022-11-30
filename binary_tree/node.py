class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree():
    def __init__(self, root=None):
        self.root = root

    def insert(self, val):
        newNode = TreeNode(val)
        if self.root is None:
            self.root = newNode
            return

        ptr = self.root
        while True:
            if val > ptr.val:
                if ptr.right:
                    ptr = ptr.right
                else:
                    ptr.right = newNode
                    return
            elif val < ptr.val:
                if ptr.left:
                    ptr = ptr.left
                else:
                    ptr.left = newNode
                    return
            break

    def find(self, val):
        ptr = self.root
        while ptr:
            if val == ptr.val:
                return ptr
            elif val > ptr.val:
                ptr = ptr.right
            else:
                ptr = ptr.left
        return None

    def pop_min(self, node):



    def delete(self, val):
        if self.root.val == val:
            if self.root.left is None and self.root.right is None:
                self.root = None
            elif self.root.left != None and self.root.right == None:
                self.root = self.root.left
            elif self.root.left == None and self.root.right != None:
                self.root = self.root.left
            else:
                # РЕКУРСИЯ НАЙТИ В ИНЕТЕ



tree = BinarySearchTree()
tree.insert(5)
tree.insert(3)
tree.insert(6)

print(tree.find(3))






