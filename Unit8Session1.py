# PROBLEM 1: Build a Binary Tree I
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# I want to create a binary tree given the TreeNode class

# 3. Translate each sub-problem into pseudocode:
# top = TreeNode(10, TreeNode(4), TreeNode(6))

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
root = TreeNode(10, TreeNode(4), TreeNode(6))


# PROBLEM 2: 3-Node Sum I
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# Given a 3 node binary tree
# I want to return a boolean indicating whether the root value is
# equal to the sum of the child nodes' values
# To do that, I compare the root node's value with its two children's sum and
# return accordingly

# 3. Translate each sub-problem into pseudocode:
# def check_tree(root):
#   return root.val == root.left.val + root.right.val

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def check_tree(root):
    return root.val == root.left.val + root.right.val
# time complexity: O(1), since we are checking exactly 3 nodes

# PROBLEM 3: 3-Node Sum II
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
#   I want to write a function that takes in a root node of a
#   binary tree, who has at most 3 nodes, and return whether
#   the root's node value is equal to the sum of its
#   children's values
#   Given that the tree has at most 3 nodes, it could have
#   0 node
#   root only
#   root with left child
#   root with right child
#   root with left and right child
#   so if i see 0 nodes, i return False
#   if i see 1 node, also False, no children's sum
#   if there is at least one child, I calculate the sum
#   and return whether that matches root's value

# 3. Translate each sub-problem into pseudocode:
# def check_tree(root):
#     if not root:
#         return False
#     if not root.left and not root.right:
#         return False
#     left = root.left.val if root.left else 0
#     right = root.right.val if root.right else 0
#     return left + right == root.val

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def check_tree(root):
    if not root:
        return False
    if not root.left and not root.right:
        return False
    left = root.left.val if root.left else 0
    right = root.right.val if root.right else 0
    return left + right == root.val
# time complexity: O(1), since we check at most 3 nodes


# PROBLEM 4: Find Leftmost Node I
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# Given the root node, I want to write a function that returns
# the value of the leftmost node
# some edges cases:
# if tree is empty and root node is none, we return None
# so what i will do is as long as there is a left node,
# i will traverse to that left node
# if left is None i will return the current value

# 3. Translate each sub-problem into pseudocode:
# def left_most(root):
#   if not root:
#       return None
#   cur = root
#   while cur.left:
#       cur = cur.left
#   return cur.val

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def left_most(root):
    if not root:
        return None
    cur = root
    while cur.left:
        cur = cur.left
    return cur.val
# time complexity: O(n)
# why: in worst case scenario - all nodes are left nodes, we check all nodes
# space complexity: O(1)
# why: we don't have extra storage for input

# PROBLEM 5: Find Leftmost Node II
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# I want to implement find left most, but do it recursively
# so once again the input is the root node
# i have the find the left most node
# edge case is no nodes or only root nodes
# how i will do it is i will return left_most on every left node
# my base case is if there are no more left nodes, i return the current value

# 3. Translate each sub-problem into pseudocode:
# def left_most(root):
#   if not root:
#       return None
#   if not root.left:
#       return root.val
#   return left_most(root.left)

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def left_most(root):
    if not root:
        return None
    if not root.left:
        return root.val
    return left_most(root.left)
# time complexity: O(n)
# why: in worst case scenario, every node is a left node, we traverse the entire input
# space complexity: O(n)
# why: we create stack frame for every left node, which could be every node in input
