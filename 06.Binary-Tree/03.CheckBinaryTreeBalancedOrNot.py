def height(root):
    
    if root == None:
        return 0
    return 1 + max(height(root.left),height(root.right))
    
def isBalanced(root):

    if root == None:
        return True
    lh = height(root.left)
    rh = height(root.right)
    
    if lh - rh > 1 or rh - lh > 1:
        return False
        
    isLeftBalanced = isBalanced(root.left)
    isRightBalanced = isBalanced(root.right)
    
    if isLeftBalanced and isRightBalanced:
        return True
    else:
        return False
        
print(isBalanced(root))
