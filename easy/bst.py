
class node:
    def __init__(self, data=0, left=None, right = None):
        self.data = data
        self.left = left
        self.right = right

# Breadth first traversal
def bst(root, low, high):
    q = []
    visited = set()
    q.append(root)
    total = 0

    while q:
        node = q.pop(0)
        if not node:
            continue
        if node not in visited:
            visited.add(node)
            if low<=node.data<=high:
                total+=node.data
                q.append(node.left)
                q.append(node.right)
            elif node.data<low:
                q.append(node.right)
            else:
                q.append(node.left)
        else:
            pass
    return total



# Recursive solution
def bst2(root, low, high):
    if not root:
        return 0
    if root.data<low:
        return bst2(root.right, low, high)
    elif root.data>high:
        return bst2(root.left, low, high)
    else:
        return root.data+ bst2(root.left, low, high)+bst2(root.right, low, high)

if __name__ == "__main__":
    root = node(10)
    l1 = node(5)
    r1 = node(15)
    l2 = node(3)
    r2 = node(7)
    l3 = node(13)
    r3 = node(18)
    l4 = node(1)
    l5 = node(6)
    root.left = l1
    root.right = r1
    l1.left = l2
    l1.right = r2
    r1.left = l3
    r1.right = r3
    l2.left = l4
    r2.left = l5

    print(bst2(root, 6, 10))