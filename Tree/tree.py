class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        
def create_tree():
    root = TreeNode("A")
    
    B = TreeNode("B")
    C = TreeNode("C")
    D = TreeNode("D")
    
    root.children = [B, C, D]
    
    E = TreeNode("E")
    F = TreeNode("F")
    
    B.children = [E, F]
    
    G = TreeNode("G")
    H = TreeNode("H")
    
    D.children = [G, H]
    
    return root