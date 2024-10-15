# PROBLEM 1: Hello World!
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is this program trying to do?
#      What is the output of this program?

# PLAN
#2. Write out in plain English what you want to do:
#      I want to create a Python function that will print "Hello World!" to the terminal
#      and call it

#3. Translate each sub-problem into pseudocode:
#      3.1 function hello_world
#      3.1.1 print "Hello World!"
#      3.2 hello_world()

# Implement
#4. Translate the pseudocode into Python and share your final answer:
def hello_world():
  print("Hello world!")
hello_world()


# PROBLEM 2
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      What is the output of this program?
#      What is the mood variable used for?

# PLAN
#2. Write out in plain English what you want to do:
#      I want to change the code so that it will print a different emoji 
#      to reflect my current mood

#3. Translate each sub-problem into pseudocode:
#      3.1 function todays_mood:
#      3.1.1 mood = new_emoji
#      3.1.2 print mood
#      3.2 todays_mood()

# Implement
#4. Translate the pseudocode into Python and share your final answer:
def todays_mood():
    mood = "😃"
    print("Today's mood: " + mood)

todays_mood()


# PROBLEM 3
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      Where is the variable "menu" introduced?
#      How can we change the value of this variable?

# PLAN
# 2. Write out in plain English what you want to do:
#      I want to change the value of the menu variable so my final output will print:
#      Lunch today is: 🍱
# 3. Translate each sub-problem into pseudocode: 
#      3.1   function print_menu (menu)
#      3.1.1   print "Lunch today is: " + menu
#      3.2   print_menu("🍱")


# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def print_menu(menu):
  print("Lunch today is: " + menu)
print_menu("🍱")


# PROBLEM 4
# UNDERSTAND
# 1. Share 2 questions you would ask to help understand the question:
#      Where in the code does the calculation occur?
#      How can I change the calculation so it doubles the output?

# PLAN
# 2. Write out in plain English what you want to do:
#      I want to change the code so that it will print the double of the input
# 3. Translate each sub-problem into pseudocode: 
#      3.1   function sum(a, b)
#      3.1.1   return a + b
#      3.2   num = sum(13, 27)
#      3.3   num *= 2
#      3.4   print num

# IMPLEMENT
# 4. Translate the pseudocode into Python and share your final answer:
def sum(a, b):
  return a + b
num = sum(13, 27)
num *= 2
print(num)