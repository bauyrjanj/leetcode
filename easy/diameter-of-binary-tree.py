def dobt(root):
    global ans
    ans = 0

    def depth(p):
        global ans
        if p==None:
            return 0
        left, right = depth(p.left), depth(p.right)
        ans = max(ans, left+right)
        return 1+max(left, right)

    depth(root)

    return ans

class node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

if __name__ == "__main__":
    root = node(1)
    c1 = node(2)
    c2 = node(3)
    c3 = node(4)
    c4 = node(5)
    root.left = c1
    root.right = c2
    c1.left = c3
    c1.right = c4
    print(dobt(root))

