# PROBLEM 1: Valid Parentheses
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# i will create a stack and add every opening parentheses in
# every time i see a closing parenthesis, i check if it matches the one that is a the top of the stack
# if it is not, i return false
# else i pop the stack
# when i am done processing the input string
# i will check if the stack is empty
# if it is i return true
# if not i return false

# 3. Translate each sub-problem into pseudocode:
# 1) Initialize an empty stack.
# 2) Create a mapping of closing brackets to their corresponding opening brackets.
# 3) Iterate through each character in the string:
#     a) If the character is a closing bracket:
#         i) Check if the stack is not empty and the top of the stack is the matching opening bracket.
#         ii) If not, return False.
#     b) If the character is an opening bracket, push it onto the stack.
# 4) After processing all characters, check if the stack is empty.
# 5) If the stack is empty, return True (all brackets were matched); otherwise, return False.

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def is_valid(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_map:
            top_element = stack.pop() if stack else '#'
            if bracket_map[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack


# PROBLEM 2: Best Time to Buy and Sell Stock
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# I traverse the list once
# i keep track of the min price and max profit
# every new node i update them accordingly
# after im done traversing the list i will return the max profit

# 3. Translate each sub-problem into pseudocode:
# 1) Initialize min_price to a very large number and max_profit to 0.
# 2) Iterate through each price in the list:
#     a) Update min_price to the minimum of min_price and the current price.
#     b) Calculate the current profit by subtracting min_price from the current price.
#     c) Update max_profit to the maximum of max_profit and the current profit.
# 3) Return max_profit.

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def max_profit(prices):
    # Initialize variables
    min_price = float('inf')
    max_profit = 0

    # Iterate through each price in the array
    for price in prices:
        # Update the minimum price seen so far
        min_price = min(min_price, price)
        # Calculate the potential profit
        current_profit = price - min_price
        # Update the maximum profit seen so far
        max_profit = max(max_profit, current_profit)

    return max_profit


# PROBLEM 3: Shuffle Merge
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# while i haven't hit the end of either lists
# i add one node from list 1 and one node from list 2
# then i go to their next nodes
# when i'm outside the loop
# i will continue adding the rest of the nodes of to the new merged list
# i return the new merged list

# 3. Translate each sub-problem into pseudocode:
# 1) Check if either head_a or head_b is None, return the non-None list.
# 2) Initialize merged_head with head_a and set current pointers for both lists.
# 3) Use a toggle to alternate between the lists while traversing.
# 4) Append nodes alternately from each list to the merged list.
# 5) If one list is exhausted, append the remaining nodes from the other list.
# 6) Return the merged_head.

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def shuffle_merge(head_a, head_b):
    if not head_a:
        return head_b
    if not head_b:
        return head_a

    # Initialize the merged list with the first node of list A
    merged_head = head_a
    current_a = head_a.next
    current_b = head_b
    current_merged = merged_head

    # Alternate appending nodes from each list
    toggle = True  # Starts with List B because List A's head is already used
    while current_a and current_b:
        if toggle:
            current_merged.next = current_b
            current_b = current_b.next
        else:
            current_merged.next = current_a
            current_a = current_a.next
        current_merged = current_merged.next
        toggle = not toggle  # Switch between List A and List B

    # Append the remaining nodes from either list
    current_merged.next = current_a if current_a else current_b

    return merged_head


# PROBLEM 4: Group Anagrams
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# for each word, i will make a dictionary of each unique letter and their occurrence
# i sort and turn them into tuple for easy comparison
# if the words have the same tuple, i add them to the same list
# i create a dictionary with the tuple as the key, the list of anagrams as the value
# at the end, i return all the dictionary values in a list

# 3. Translate each sub-problem into pseudocode:
# 1) Initialize an empty hash map (anagrams_dict).
# 2) Iterate over each word in the input list:
#     a) Sort the characters of the word to form the key.
#     b) If the key is already in the hash map, append the word to the list.
#     c) If the key is not in the hash map, create a new entry with the key and the word as the first element in the list.
# 3) Initialize an empty list (answer).
# 4) Iterate over the values in the hash map and append each list of anagrams to the answer list.
# 5) Return the answer list.

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def group_anagrams(strs):
    anagrams_dict = {}

    for word in strs:
        word_as_list = [char for char in word]
        word_as_list.sort()
        key = tuple(word_as_list)
        if anagrams_dict.get(key):
            anagrams_dict[key].append(word)
        else:
            anagrams_dict[key] = [word]

    answer = []

    for key, value in anagrams_dict.items():
        answer.append(value)
    return answer


# PROBLEM 5: Sum Root to Leaf Numbers
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the input of the function?
#      What is the output of the function?

# PLAN
# 2. Write out in plain English what you want to do:
# i create a helper function
# i traverse the tree recursively
# if i see a leaf node, i return a list of its value
# i let the left result be my current value appended to every value of the helper function of my left child
# i let the right result be my current value appended to every value of the helper function of my right child
# i return a list that is the combination of left result and right result

# 3. Translate each sub-problem into pseudocode:
# 1) Define a helper function `dfs(node, current_number)` that:
#     a) Returns 0 if the node is None.
#     b) Updates `current_number` by appending the node's value.
#     c) Returns `current_number` if the node is a leaf.
#     d) Recursively calls `dfs` for the left and right children.
#     e) Returns the sum of the results from the left and right subtrees.
# 2) Initialize the DFS with the root node and an initial `current_number` of 0.
# 3) Return the result of the DFS.

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def sum_numbers(root):
    def dfs(node, current_number):
        if node is None:
            return 0

        current_number = current_number * 10 + node.val

        # If the current node is a leaf, return the current number
        if node.left is None and node.right is None:
            return current_number

        # Recursively sum the numbers from the left and right subtrees
        left_sum = dfs(node.left, current_number)
        right_sum = dfs(node.right, current_number)

        return left_sum + right_sum

    # Start DFS with the root and initial current number as 0
    return dfs(root, 0)

