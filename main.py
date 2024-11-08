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


def binary_tree_paths(root):
    if not root:
        return []

    val = ""
    if root.val:
        val += str(root.val)
    if root.left or root.right:
        val += "->"

    if not root.left and not root.right:
        return [val]

    left_paths = []
    right_paths = []
    if root.left:
        left_paths = binary_tree_paths(root.left)  # we get back a list of strings
        for i in range(len(left_paths)):
            left_paths[i] = val + left_paths[i]
    if root.right:
        right_paths = binary_tree_paths(root.right)
        for i in range(len(right_paths)):
            right_paths[i] = val + right_paths[i]
    return left_paths + right_paths


def main():
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
    print(binary_tree_paths(root))

    root = TreeNode(1)
    print(binary_tree_paths(root))


if __name__ == "__main__":
    main()
