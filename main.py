# PROBLEM 1
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:

# 3. Translate each sub-problem into pseudocode: 

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:


# PROBLEM 2
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:

# 3. Translate each sub-problem into pseudocode: 

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:


# PROBLEM 3
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:

# 3. Translate each sub-problem into pseudocode: 

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:


# PROBLEM 4
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:

# 3. Translate each sub-problem into pseudocode: 

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:


# PROBLEM 5
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:

# 3. Translate each sub-problem into pseudocode:

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:


# UPI TEMPLATE

# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:

# 3. Translate each sub-problem into pseudocode: 

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_bst(root):
    if root:
        print_bst(root.left)
        print(root.key if root.key else "None", end=" ")
        print_bst(root.right)


def is_symmetric_tree(left, right):
    if not left and not right:
        return True
    if not left or not right:
        return False
    if left.val != right.val:
        return False
    left_tree = is_symmetric_tree(left.left, right.right)
    right_tree = is_symmetric_tree(left.right, right.left)
    return left_tree and right_tree


def is_symmetric(root):
    if not root:
        return True
    return is_symmetric_tree(root.left, root.right)


def main():
    root = None
    print(is_symmetric(root))

    root = TreeNode(1)
    print(is_symmetric(root))

    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
    print(is_symmetric(root))

    root = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
    print(is_symmetric(root))

if __name__ == "__main__":
    main()
