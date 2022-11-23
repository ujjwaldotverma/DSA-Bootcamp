def height(root):
    if root == None:
        return 0
    return 1 +  max(height(root.left), height(root.right))

def diameter(root):
    if root == None:
        return 0
    op1 = height(root.left) + height(root.right)
    op2 = diameter(root.left)
    op3 = diameter(root.right)
    return max(op1,op2,op3)
