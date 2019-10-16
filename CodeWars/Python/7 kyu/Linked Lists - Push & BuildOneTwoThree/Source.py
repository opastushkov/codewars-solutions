class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def push(head, data):
    tmp = Node(data)
    tmp.next = head
    return tmp
  
def build_one_two_three():
    res = None
    for x in range(3, 0, -1):
        res = push(res, x)
        
    return res