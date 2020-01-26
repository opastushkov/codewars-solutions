class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def insert_nth(head, index, data):
    if not head: 
        head = Node(data)
        return head
        
    if not index:
        tmp = head
        head = Node(data)
        head.next = tmp
        return head
        
    current = head
    prev = head
    for _ in range(index):
        prev = current
        current = current.next
    
    tmp = current
    current = Node(data)
    current.next = tmp
    prev.next = current
    
    return head
        