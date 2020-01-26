class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def append(listA, listB):
    if not listA: return listB
    if not listB: return listA
    head = listA
    while listA.next:
        listA = listA.next
    listA.next = listB
    return head