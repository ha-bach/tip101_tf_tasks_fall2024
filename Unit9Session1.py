# PROBLEM 1: Is Symmetric Tree
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# Understanding
# input: root node of a tree
# output: boolean indicating whether tree is symmetric
# constraints: the tree is a binary tree. any min or max height for input?
# edge case: empty tree, one node tree

# 1) If both left and right nodes are None, return True.
# 2) If only one of the nodes is None, return False.
# 3) If the values of the left and right nodes do not match, return False.
# 4) Recursively compare the left child of the left node with the right child of the right node, and the right child of the left node with the left child of the right node.
# 5) Return the result of the recursive comparisons.

# 3. Translate each sub-problem into pseudocode:
# def is_symmetric_tree(left, right):
#   if not left and not right:
#       return True
#   if not left or not right:
#       return False
#   if left.key != right.key:
#       return False
#   left = is_symmetric_tree(left.left, right.right)
#   right = is_symmetric_tree(left.right, right.left)
#   return left and right

# def is_symmetric(root):
#   if not root:
#       return True
#   return is_symmetric_tree(root.left, root.right)

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
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

# Time complexity: O(n)
# Why: we are traversing every node to make sure the tree is symmetrical
# Time complexity: O(n)
# Why: We create a stack frame for every node we visit


# PROBLEM 2: Root-to-Leaf Paths
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# Understanding
# Input: root node of a binary tree
# Output: a list containing all the possible paths to a leaf node represented by strings
# Constraint: ?
# Edge case: empty tree (list with empty string?), tree with only root (list with one string containing one value)

# Plan
# it's going to be a recursive function
# first we make a string of the current node value
# if its leaf node is "node_val"
# else its "node_val->"
# make a list call result
# then if left child
# we add string + recursive call to left child
# and add that to result
# if right child
# add string + recursive call to right child
# and add that to result
# we return result

# 3. Translate each sub-problem into pseudocode:
# def binary_tree_paths(root):
#   val = ""
#   if root:
#       val += str(root.val)
#   if root.left or root.child:
#       val += "->"

#   if root.left:
#       left_paths = binary_tree_paths(root.left)  # we get back a list of strings
#       for path in left_paths:
#           path = val + path
#   if root.right:
#       right_paths = binary_tree_paths(root.right)
#       for path in right_paths:
#           path = val + path
#   return left_paths + right_paths

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
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

# Time complexity: O(n)
# Why: we visit every node in the tree
# Space complexity: O(n)
# Why: function is recursive, we call a stack frame for every node we visit


# PROBLEM 3: Minimum Difference in BST
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# Understand
# input: root node of binary tree
# output: minimum difference in binary tree
# constraints: how small can the tree be
# edge case: one node, zero nodes - won't happen, at least two nodes

# Plan
# make an internal helper function that in order traverses the tree (so we compare the tree in ascending order),
# compare the difference between each node, and update the min diff we found so far
# to do this i will make an internal helper function that takes in the node, the previous inorder traversal value,
# the current min diff
# and return the current value and current min diff (so the upper call can calculate new diff using those values)
# base case is if no more node, we return the current prev value and min_diff
# else we find out if absolute difference between root's value and prev is smaller than min diff
# call the function recursively with root = next node, prev = root's val, min diff accordingly


# 3. Translate each sub-problem into pseudocode:
# def min_diff_in_bst(root):
#   def find_min_diff(root, prev, min_diff) -> prev, min_diff:
#       if not root:
#           return prev, min_diff
#       prev, min_diff = find_min_diff(root.left, root.val, min_diff)
#       if prev:
#           min_diff = min(min_diff, root.val - prev)
#       return find_min_diff(root.right, root.val, min_diff)
#   _, result = find_min_diff(root, None, float('inf'))
#   return result


# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def min_diff_in_bst(root):
    def find_min_diff(node, prev, min_diff):
        if not node:
            return prev, min_diff
        prev, min_diff = find_min_diff(node.left, prev, min_diff)
        if prev:
            min_diff = min(min_diff, node.val - prev)
        return find_min_diff(node.right, node.val, min_diff)

    _, result = find_min_diff(root, None, float('inf'))
    return result

# Time complexity: O(n)
# Why: we are examining every node in the tree to find difference
# Space complexity: O(h)
# Why: we create as many stack frame as the deepest node


# PROBLEM 4: Increasing Order Search Tree
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# I in order traverse the node, then add them into a list
# then i construct a new tree out of the list
# and return the node of the new tree

# 3. Translate each sub-problem into pseudocode:
# def increasing_bst(root):
#     nodes = []
#
#     def inorderTraversal(node):
#         if node:
#             inorderTraversal(node.left)
#             nodes.append(node)
#             inorderTraversal(node.right)
#
#     inorderTraversal(root)
#
#     root = TreeNode(nodes[0].val)
#     cur = root
#
#     for n in nodes[1:]:
#         cur.right = TreeNode(n.val)
#         cur = cur.right
#
#     return root

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def increasing_bst(root):
    nodes = []

    def inorderTraversal(node):
        if node:
            inorderTraversal(node.left)
            nodes.append(node)
            inorderTraversal(node.right)

    inorderTraversal(root)

    root = TreeNode(nodes[0].val)
    cur = root

    for n in nodes[1:]:
        cur.right = TreeNode(n.val)
        cur = cur.right

    return root

# Time complexity: O(n)
# Why: I visit every node in the tree once to construct a list
#       and visit them again to make a new list
# Space complexity: O(n)
# Why: I make a list that stored every node in the tree

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
# so first i want to find the size of the entire tree via dfs
# if size is odd i return false
# then i traverse the tree via dfs and
# find size of left tree
# and find size of right tree
# if there is a size of n / 2, we return true
# if the helper function finishes counting the size of the entire tree
# no subtree was found with exactly half the nodes
# we return false

# 3. Translate each sub-problem into pseudocode:
# 1) Define a helper function `count_nodes(root)` to count the total number of nodes in the tree.
#     a) If the current node is None, return 0.
#     b) Recursively count nodes in the left and right subtrees and add 1 for the current node.
# 2) Define another helper function `can_split_helper(root, total_nodes)` to check if any subtree can form half the total number of nodes.
#     a) If the current node is None, return 0.
#     b) Recursively count nodes in the left and right subtrees.
#     c) If any subtree count equals half the total number of nodes, set a flag to True.
#     d) Return the total count of nodes for the current subtree.
# 3) In the main function `can_split(root)`, calculate the total number of nodes.
# 4) If the total number of nodes is odd, return False.
# 5) Use the helper function to check if the tree can be split, and return the result.

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_nodes(root):
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


def can_split_helper(root, total_nodes):
    if not root:
        return 0

    left_count = can_split_helper(root.left, total_nodes)
    right_count = can_split_helper(root.right, total_nodes)

    # If any subtree has half of the total nodes, we can split the tree
    if left_count == total_nodes // 2 or right_count == total_nodes // 2:
        can_split_helper.found = True

    return 1 + left_count + right_count


def can_split(root):
    total_nodes = count_nodes(root)
    if total_nodes % 2 != 0:
        return False

    can_split_helper.found = False
    can_split_helper(root, total_nodes)
    return can_split_helper.found