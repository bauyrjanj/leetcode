class Node:
    def __init__(self, data):
        self.val = data
        self.children = []


def count_of_nodes(root, queries, s):
    final = []

    for query in queries:
        q = []
        sub = []
        result = 0
        v, c = query
        q.append(root)
        while q:
            node = q.pop(0)
            if node.val==v and s[node.val-1]==c:
                result+=1
                sub+=node.children
                while sub:
                    n = sub.pop(0)
                    if s[n.val-1]==c:
                        result+=1
                    sub+=n.children
                continue
            else:
                q+=node.children
        final.append(result)

    return final

if __name__ == "__main__":
  n_1 ,q_1 = 3, 1
  s_1 = "aba"
  root_1 = Node(1)
  root_1.children.append(Node(2))
  root_1.children.append(Node(3))
  queries_1 = [(1, 'a')]

  output_1 = count_of_nodes(root_1, queries_1, s_1)
  print(output_1)

  n_2, q_2 = 7, 3
  s_2 = "abaacab"
  root_2 = Node(1)
  root_2.children.append(Node(2))
  root_2.children.append(Node(3))
  root_2.children.append(Node(7))
  root_2.children[0].children.append(Node(4))
  root_2.children[0].children.append(Node(5))
  root_2.children[1].children.append(Node(6))
  queries_2 = [(1, 'a'), (2, 'b'), (3, 'a')]
  output_2 = count_of_nodes(root_2, queries_2, s_2)
  expected_2 = [4, 1, 2]

  print(output_2)