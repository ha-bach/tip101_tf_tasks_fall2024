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


class TreeNode():
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def print_bst(root):
    if root:
        print_bst(root.left)
        print(root.key if root.key else "None", end=" ")
        print_bst(root.right)


def inorder_successor(root, current):
    if not root:
        return None
    if root.key <= current.key:
        return inorder_successor(root.right, current)
    if root is current:
        return None
    successor = inorder_successor(root.left, current)
    if not successor:
        return root
    return successor


def main():
    current_2 = TreeNode(6)
    current = TreeNode(5, TreeNode(1), TreeNode(8, current_2, TreeNode(9)))
    root = TreeNode(10, current, TreeNode(15))
    # print_bst(root)
    print("Inorder successor: ", inorder_successor(root, current).key)
    print("Inorder successor: ", inorder_successor(root, current_2).key)

if __name__ == "__main__":
    main()
