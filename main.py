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


def find_min(root):
    cur = root
    while cur.left:
        cur = cur.left
    return cur


def remove_bst(root, key):
    # Locate the node to be removed
    if key < root.key:
        root.left = remove_bst(root.left, key)
    elif key > root.key:
        root.right = remove_bst(root.right, key)
    else:  # we are at node to remove
        if not root.left:   # there is right child or no child
            return root.right
        if not root.right:    # there is left child
            return root.left

        # node has two children
        # Find the node's inorder successor (smallest node in right subtree)
        successor = find_min(root.right)
        # Swap the value of the node and its inorder successor
        successor.key, root.key = root.key, successor.key
        # Recursively remove the successor (which now has the current node's value)
        root.right = remove_bst(root.right, key)

    return root


def main():
    root = TreeNode(10, TreeNode(5, TreeNode(1), TreeNode(8)), TreeNode(15, TreeNode(13), TreeNode(16)))
    print_bst(root)
    print()

    root = remove_bst(root, 10)
    print_bst(root)
    print()

    root = TreeNode(10, TreeNode(5, TreeNode(1), TreeNode(8, None, TreeNode(9))),
                    TreeNode(15, TreeNode(13), TreeNode(16)))
    print_bst(root)
    print()

    root = remove_bst(root, 8)
    print_bst(root)
    print()

    root = TreeNode(10, TreeNode(5, TreeNode(1), TreeNode(8, TreeNode(9), None)),
                    TreeNode(15, TreeNode(13), TreeNode(16)))
    print_bst(root)
    print()

    root = remove_bst(root, 8)
    print_bst(root)
    print()

    root = TreeNode(10, TreeNode(5, TreeNode(1), TreeNode(8, None, TreeNode(9))),
                    TreeNode(15, TreeNode(13), TreeNode(16)))
    print_bst(root)
    print()

    root = remove_bst(root, 9)
    print_bst(root)
    print()

if __name__ == "__main__":
    main()
