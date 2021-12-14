class tree:
    def __init__(self, data, left = None, right = None):
        self.val = data
        self.left = left
        self.right = right

def visible_nodes(root):
    q = []
    q.append(root)
    visible = 0

    while q:
        for i in range(len(q)):
            node = q.pop(0)
            if i==0:
                visible+=1
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return visible

if __name__=="__main__":

    r = tree(8)
    n1 = tree(3)
    n2 = tree(10)
    n3 = tree(1)
    n4 = tree(6)
    n5 = tree(14)
    n6 = tree(4)
    n7 = tree(7)
    n8 = tree(13)

    r.left = n1
    r.right = n2
    n1.left = n3
    n1.right = n4
    n4.left = n6
    n4.right = n7
    n2.right = n5
    n5.left = n8

    print(visible_nodes(r))




