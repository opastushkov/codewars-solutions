class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def get_nth(node, index):
    if index < 0 or not node : raise IndexError
    for _ in range(index):
        node = node.next
        if node is None: raise IndexError
    return node
  