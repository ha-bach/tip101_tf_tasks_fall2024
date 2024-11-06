# PROBLEM 1: Is Uni-Valued
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# a tree is univalued of if its node and its children agree on the same value
# so base case, we have no nodes
# i return True
# a leaf node
# i return True
# a parent node with only one level of children
# i return whether parent agree with children's values
# then i can return whether the parents agree and if the children are also univalued

# 3. Translate each sub-problem into pseudocode:
# def is_univalued(root):
# if not root:
#   return True
# if not root.right and not root.left:
#   return True
# if root.right and root.left:
#   return root.val == root.left.val == root.right.val and is_univalued(root.left) and is_univalued(root.right)
# if root.right:
#   return root.val == root.right.val and is_univalued(root.right)
# if root.left:
#   return root.val == root.left.val and is_univalued(root.left)
# print("Logic went wrong here")

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def is_univalued(root):
    if not root:
        return True
    if not root.right and not root.left:
        return True
    if root.right and root.left:
        return root.val == root.left.val == root.right.val and is_univalued(root.left) and is_univalued(root.right)
    if root.right:
        return root.val == root.right.val and is_univalued(root.right)
    if root.left:
        return root.val == root.left.val and is_univalued(root.left)
    print("Logic went wrong here")

# Time complexity: O(n)
# why: I'm checking every node in the tree to see if they agree
# Space complexity: O(n)
# why: everytime I check, a stack frame is opened for that recursive method


# PROBLEM 2: Binary Tree Height
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# given a binary tree's root node, i want to return its height
# so for every node, i will check if it has children
# if a node has value, it counts as one height
# i will get the height of the left child and the height of the right child
# and return current height + higher height between the children

# 3. Translate each sub-problem into pseudocode:
# def height(root):
#   if not root.left and root.right:
#       return 1
#   left_height = height(root.left)
#   right_height = height(root.right)
#   cur_height = 1 if root.val else 0
#   return cur_height + (left_height if left_height >= right_height else right_height)

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def height(root):
    if not root:
        return 0
    if not root.left and root.right:
        return 1
    left_height = height(root.left)
    right_height = height(root.right)
    cur_height = 1 if root.val else 0
    return cur_height + (left_height if left_height >= right_height else right_height)

# time complexity: O(n)
# why: we traverse entire tree to calculate height
# space complexity: O(n)
# why: we potentially create a stack frame for every node to calculate height


# PROBLEM 3: BST Insert
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# I want to write a function that takes in the root node,
# a key and a value, and insert a new node into the tree
# according to the key and value
# 4 possible cases:
# 1. root is empty: I insert in root
# 2. we found an existing key: we update the key
# 3. we insert to the left of some key: we create a new node and link the parent's left ptr there
# 4. we insert to the right of some key: we create a new node and link the parent's right ptr there
# so what i do is
# if root is empty, I create a node there and return root
# i set cur to root
# while cur is not empty
# i traverse the tree to find where we insert the node
# so if key == cur.key
#   i will update the node
# else if key < cur.key
#   i check if there is space to insert
#   so if not root.left
#       i will insert new node there, and link it to cur's left child, and return root
#   else, there is already a node there
#       i move to cur to that node
# else, same thing as left
#   if not root.right
#       i insert node there, link it to cur's right, and return root
#   else
#       cur = cur.right

# 3. Translate each sub-problem into pseudocode:
# def insert(root, key, value):
#   if not root:
#       root = Node(key, value)
#       return root
#   cur = root
#   while cur:
#       if key == cur.key:
#           cur.val = value
#           return root
#       if key < cur.key:
#           if not cur.left:
#               cur.left = Node(key, value)
#               return root
#           cur = cur.left
#       else:
#           if not cur.right:
#               cur.right = Node(key, value)
#               return root
#           cur = cur.right


# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def insert(root, key, value):
    if not root:
        root = TreeNode(key, value)
        return root
    cur = root
    while cur:
        if key == cur.key:
            cur.val = value
            return root
        if key < cur.key:
            if not cur.left:
                cur.left = TreeNode(key, value)
                return root
            cur = cur.left
        else:
            if not cur.right:
                cur.right = TreeNode(key, value)
                return root
            cur = cur.right

# Time complexity: O(h)
# Why: I traverse the height of the tree to find out where to insert
# Space complexity: O(1)
# Why: no data structures, only pointers

# PROBLEM 4: BST Remove I
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# I want to write a function that takes in a root node and node to remove,
# and remove that node in the BST of the root node
# if the node has to children, I will find the smallest node in the right subtree
# and move that node to where the node was removed

# 3. Translate each sub-problem into pseudocode:
# def remove_bst(root, key):
#   # Locate the node to be removed
#   if key < root.key:
#       root.left = remove_bst(root.left, key)
#   elif key > root.key:
#       root.right = remove_bst(root.right, key)
#   else:
#   # If the node has two children:
#   if root.left and root.right:
#       # Find the node's inorder successor (smallest node in right subtree)
#       successor = find_min(root.right)
#       # Swap the value of the node and its inorder successor
#       successor.key, root.key = root.key, successor.key
#       # Recursively remove the successor (which now has the current node's value)
#       root.right = remove_bst(root.right, key)
#   else:
#       if root.left: # if node has left child only
#           return root.right
#       else: # if node has right child or no child
#           return root.left
#   # Return the root of the updated tree

# def find_min(root):
#   cur = root
#   while cur.left:
#       cur = cur.left
#   return cur

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
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

# Time complexity: O(h)
# Why: I traverse the tree by level to find node
# Space complexity: O(h)
# Why: I traverse recursively, creating a stack frame each node I visit

# PROBLEM 5: BST In-order Successor
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# I will recursively traverse the tree to find the inorder successor
# If root is empty, I will return None (there is no key that is bigger)
# So first I need to narrow down the right subtree I want
# So if my key is larger than current key, I travel to right subtree
# If it is not, it is time to look for the inorder successor
# in the left subtree
# so I keep going left until I hit a leaf node
# or if i hit the key I am looking for
# in that case the solution would be the parent node
# so if i hit the key I am looking for, I return None
# and then i call the function on the left child
# if the function returns None, I am at a leaf node,
# i return my node
# else i return the output of the recursive call

# 3. Translate each sub-problem into pseudocode:
# def inorder_successor(root, current):
#   if not root:
#       return None
#   if root.key < current.key:
#       return inorder_successor(root.right, current)
#   if root is cur:
#       return None
#   successor = inorder_successor(root.left, current)
#   if not successor:
#       return root
#   return successor

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
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

# Time complexity: O(h)
# Why: I traverse the full height of a tree
# Space complexity: O(h)
# Why: Solution is recursive, I create as many stack frames as the nodes I visited
