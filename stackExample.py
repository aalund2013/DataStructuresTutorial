"""
This code filters through a text document and determines
if each line has a balanced number of parenthesis,
square brackets, and curly braces.
"""

text = "balancedStack.txt"


def isBalanced(file):
    lineNum = 0
    with open(file, "r") as f:
        for line in f:
            balanced = True
            lineNum += 1
            stack = []
            for char in line:
                if balanced:
                    # put opening symbols in stack
                    if char == "(" or char == "{" or char == "[":
                        stack.append(char)
                    # if closing symbol has a matching opening symbol on top of the stack, pop it. Otherwise, it's not balanced.
                    elif char == ")":
                        if len(stack) == 0 or stack.pop() != "(":
                            balanced = False
                    elif char == "}":
                        if len(stack) == 0 or stack.pop() != "{":
                            balanced = False
                    elif char == "]":
                        if len(stack) == 0 or stack.pop() != "[":
                            balanced = False
            # returns true if stack is empty, false if there is anything left inside
            if len(stack) != 0:
                balanced = False
            if balanced:
                print(f"Line # {lineNum} is balanced")
            else:
                print(f"Line # {lineNum} is NOT balanced")


# Run the function
isBalanced(text)

"""
EXPECTED OUTPUT:
Line #1 is balanced
Line #2 is NOT balanced
Line #3 is NOT balanced
Line #4 is balanced
Line #5 is NOT balanced
Line #6 is balanced
Line #7 is balanced
Line #8 is NOT balanced
Line #9 is NOT balanced
"""
