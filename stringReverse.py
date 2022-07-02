"""
This is the solution to the challenge problem:
Return the reverse of any given string
"""

string = input("Enter any string: ")


def reverseString(string):
    # create list for stack
    reverse = []
    reversedString = ""
    for char in string:
        # loop through each character in the string and put it in the stack
        reverse.append(char)

    while len(reverse) > 0:
        # as long as there is something in the stack, take from the back and add it to the string
        reversedString = reversedString + reverse.pop()
    return reversedString
    # return the reversed string


# function call
print(reverseString(string))
