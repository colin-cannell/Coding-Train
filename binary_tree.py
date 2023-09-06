# visit node
# go to left
# print value
# go to right

class node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class binary_tree(object):
    def __init__(self, root):
        self.root = node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")

        else:
            print("Traversal type" + str(traversal_type) + "is not supported")
            return False

    def preorder_print(self, start, traversal):
        """ROOT->LEFT->RIGHT"""

        if start:
            traversal += (str(start.value) + "-")

            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """"Left->Root->Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        """Left->Right->Root"""
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal


#        1
#      /   \
#     2      3
#    / \    / \
#   4   5  6   7


tree = binary_tree(1)

tree.root.left = node(2)
tree.root.right = node(3)

tree.root.left.left = node(4)
tree.root.left.right = node(5)

tree.root.right.left = node(6)
tree.root.right.right = node(7)

print(tree.print_tree("preorder"))

print(tree.print_tree("inorder"))

print(tree.print_tree("postorder"))
