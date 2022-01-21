
class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

def merge_sorted_lists(l1, l2):
    if l1==None and l2==None:
        return l1
    if l1==None:
        return l2
    if l2==None:
        return l1

    traverse1 = l1
    traverse2 = l2
    sorted_list = []
    while traverse1 and traverse2:
        if traverse1.val>=traverse2.val:
            sorted_list.append(traverse2.val)
            traverse2 = traverse2.next
        else:
            sorted_list.append(traverse1.val)
            traverse1 = traverse1.next

    while traverse1:
        sorted_list.append(traverse1.val)
        traverse1 = traverse1.next

    while traverse2:
        sorted_list.append(traverse2.val)
        traverse2 = traverse2.next

    prev = None
    head = None

    for num in sorted_list:
        node = ListNode(num)
        if prev!=None:
            prev.next = node
            prev = node
        else:
            head = prev = node

    return head

if __name__ == "__main__":
    l1 = ListNode(1)
    l12 = ListNode(2)
    l13 = ListNode(3)
    l1.next = l12
    l12.next = l13

    l2 = ListNode(2)
    l22 = ListNode(3)
    l23 = ListNode(4)
    l2.next = l22
    l22.next = l23

    h = merge_sorted_lists(l1, l2)
    t = h

    while t:
        print(t.val)
        t = t.next


