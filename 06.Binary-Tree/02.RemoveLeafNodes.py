def removeLeafNodes(root):
    if root == None:
        return None
    if root.left == None and root.right == None:
        return None:
    root.left = removeLeafNodes(root.left)
    root.right = removeLeafNodes(root.right)
    return root
    
root = removeLeafNodes(root)
