#TC OF THIS APPROACH IS O(n*h), h being the height of the tree, it could be n or log n
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
###############################################################################################################
#NEW APPROACH
def getHeightandCheckBalanced(root):
    if root == None:
        return 0, True
    lh, isLeftBalanced = getHeightandCheckBalanced(root.left)
    rh, isRightBalanced = getHeightandCheckBalanced(root.right)
    
    h = 1 + max(lh, rh)
    if lh - rh or  rh - lh > 1:
        return h, False
        
    if isLeftBalanced and isLeftBalanced:
        return h, True
    
    else:
        return h, False

print(getHeightandCheckBalanced(root))

def isBalanced(root):
    h, isRootBalanced = getHeightandCheckBalanced(root)
    return isRootBalanced
