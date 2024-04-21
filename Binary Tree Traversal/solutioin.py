from collections import deque

def pre_order(node):
    if not node:
        return []
    queue = deque([node])
    traversal = []
    while queue:
        node = queue.popleft()
        traversal.append(node.data)
        
        if node.right:
            queue.appendleft(node.right)
        
        if node.left:
            queue.appendleft(node.left)
    
    return traversal


def in_order(node):
    if not node:
        return []
    queue = deque([node])
    node  = node.left
    traversal = []
    while queue or node:
        if node is not None:
            queue.append(node)
            node = node.left
        else:
            node = queue.pop()
            traversal.append(node.data)
            node = node.right
         
    return traversal


def post_order(node):
    if not node:
        return []
    queue = deque([node])
    traversal = []
    while queue:
        node = queue.popleft()
        traversal.append(node.data)
        
        if node.left:
            queue.appendleft(node.left)
            
        if node.right:
            queue.appendleft(node.right)
    
    return list(reversed(traversal))