# PROBLEM 1: Level Order Traversal of Binary Tree
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# i want to create a queue that keeps track of the nodes i'm going to visit
# while the queue is not empty,
# i will pop the first node and add its children into the queue

# 3. Translate each sub-problem into pseudocode:
# If the tree is empty:
# return an empty list

# Create an empty queue using deque
# Create an empty list to store the explored nodes

# Add the root to the queue

# While the queue is not empty:
# Pop the next node off the queue (pop from the left side!)
# Add the popped node to the list of explored nodes

# Add each of the popped node's children to the end of the queue

# Return the list of visited nodes

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def level_order(root):
    # if the tree is empty
    if root is None:
        # return an empty list
        return []

    # create a new empty queue
    queue = deque()
    # create a list of nodes we have already explored
    visited = []

    # append the root of the tree to the queue
    queue.append(root)

    # while there are still nodes to explore
    while queue:
        # pop next node off the queue
        current_node = queue.popleft()

        # add the root to list of visited nodes
        visited.append(current_node.val)

        # if the current node has a left child
        if current_node.left is not None:
            # add the left child to the queue
            queue.append(current_node.left)

        # if the current node has a right child
        if current_node.right is not None:
            # add the right child to the queue
            queue.append(current_node.right)

    # return the list of visited nodes
    return visited


# PROBLEM 2: Find Minimum Depth of Binary Tree
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# I will traverse the tree recursively
# if i find a leaf node,
# i will return 1
# i return 1 + min(min_height(left child), min_height(right child))

# 3. Translate each sub-problem into pseudocode:
# def min_depth(root):
#     if not root:
#         return 0
#     if not root.left and not root.right:
#         return 1
#     return 1 + min(min_depth(root.left), min_depth(root.right))

# Time complexity: O(n)
# Why: We visit each node once
# Space complexity: O(n)
# For each node we visit, we create a recursion stack frame


# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def min_depth(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return 1 + min(min_depth(root.left), min_depth(root.right))

# Time complexity: O(n)
# Why: We visit each node once
# Space complexity: O(n)
# For each node we visit, we create a recursion stack frame

# PROBLEM 3:  Odd-Even Level Sum Difference in Binary Tree
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# 1) If the tree is empty, return 0.
# 2) Create an empty queue and add the root node with level 1.
# 3) Initialize sums for odd and even levels to 0.
# 4) While the queue is not empty:
#     a) Get the number of nodes at the current level.
#     b) For each node at the current level:
#         i) Pop the node from the queue.
#         ii) Add its value to the appropriate sum (odd or even) based on the current level.
#         iii) Add the left and right children to the queue for the next level.
#     c) Increment the level.
# 5) Return the difference between the odd and even sums.

# 3. Translate each sub-problem into pseudocode:

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def level_difference(root):
    if not root:
        return 0

    queue = deque([root])
    level = 1
    odd_sum = 0
    even_sum = 0

    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()

            if level % 2 == 1:
                odd_sum += node.val
            else:
                even_sum += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        level += 1

    return odd_sum - even_sum


# PROBLEM 4: Level Order Traversal of Binary Tree with Nested Lists
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# i traverse the tree using level order
# i also keep track of the level
# and an odd sum and even sum
# every time i visit a node, i add its value to appropriate sum
# and the end i return the difference between two sums

# 3. Translate each sub-problem into pseudocode:
# 1) If the tree is empty, return an empty list.
# 2) Create an empty queue and an empty list to store the result.
# 3) Add the root to the queue.
# 4) While the queue is not empty:
#     a) Get the number of nodes at the current level.
#     b) Create a list to store the values of the current level nodes.
#     c) For each node at the current level:
#         i) Pop the node from the queue.
#         ii) Add its value to the current level list.
#         iii) Add the left and right children to the queue for the next level.
#     d) Add the current level list to the result list.
# 5) Return the result list.

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def level_order(root):
    if not root:
        return []

    result = []
    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        level_nodes = []

        for i in range(level_size):
            node = queue.popleft()
            level_nodes.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level_nodes)

    return result

# PROBLEM 5: Sum of Binary Tree Node Tilts
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
# I will visit each node in the tree using post-order traversal
# for each node,
# if a node doesn’t have a left child, treat its sum as 0 (similarly for the right child).
# as i traverse, i compute the sum of node values for both the left and right subtrees.
# and return the total tilt for the node

# 3. Translate each sub-problem into pseudocode:
# function findTilt(root):
#     totalTilt = 0
#
#     function calculateTilt(node):
#         if node is null:
#             return 0  // Sum of an empty tree is 0
#
#         leftSum = calculateTilt(node.left)
#         rightSum = calculateTilt(node.right)
#
#         tilt = abs(leftSum - rightSum)
#         totalTilt += tilt  // Accumulate tilt
#
#         return leftSum + rightSum + node.value  // Return the sum of the current subtree
#
#     calculateTilt(root)
#     return totalTilt

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def findTilt(root):
    totalTilt = 0

    def calculateTilt(node):
        nonlocal totalTilt

        if node is None:
            return 0

        leftSum = calculateTilt(node.left)
        rightSum = calculateTilt(node.right)

        tilt = abs(leftSum - rightSum)
        totalTilt += tilt

        return leftSum + rightSum + node.val

    calculateTilt(root)
    return totalTilt