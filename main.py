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

    def __str__(self):
        return str(self.val)


def print_bst(root):
    if root:
        print_bst(root.left)
        print(root.val if root.val else "None", end=" ")
        print_bst(root.right)


def min_depth(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return 1 + min(min_depth(root.left), min_depth(root.right))


def main():
    root = TreeNode(5, TreeNode(1, TreeNode(2)), TreeNode(7))
    print(min_depth(root))


if __name__ == "__main__":
    main()
