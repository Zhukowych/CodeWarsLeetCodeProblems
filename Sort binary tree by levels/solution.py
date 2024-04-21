from collections import deque

def tree_by_levels(node):
    if not node:
        return []
    
    queue = deque([(node, 0)])
    
    nodes_by_levels = {}
   
    while queue:
        node, level = queue.popleft()
        
        if level not in nodes_by_levels:
            nodes_by_levels[level] = [node.value]
        else:
            nodes_by_levels[level].append(node.value)

        if node.right:
            queue.appendleft((node.right, level+1))
            
        if node.left:
            queue.appendleft((node.left, level+1))

    sorted_nodes = []
    
    for nodes in nodes_by_levels.values():
        sorted_nodes.extend(nodes)
    
    return sorted_nodes
        