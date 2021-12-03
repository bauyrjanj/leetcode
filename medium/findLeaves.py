def findLeaves(root):

    # Function to get the height of the node at each node
    # The height at the very bottom leaf is -1. The height of a node is defined as height = max(left leaf, right leaf)+1
    def getHeight(root):
        if root==None:
            return -1

        height = max(getHeight(root.left), getHeight(root.right))+1
        if height > len(result)-1:
            result.append([])
        result[height].append(root.val)

        return height

    result = []
    getHeight(root)
    return result

class tree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

if __name__=="__main__":
    node1 = tree(1)
    node2 = tree(2)
    node3 = tree(3)
    node4 = tree(4)
    node5 = tree(5)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5

    node6 = tree(1)
    print(findLeaves(node6))

