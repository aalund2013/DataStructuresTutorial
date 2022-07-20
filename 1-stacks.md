[Back to Welcome Page](0-welcome.md)

# Stacks

When learning about stacks it is helpful to think about a stack of items - like plates. The plates on the bottom will be the last plates to be used, while those on top will be the first. In a stack the First In Last Out (FILO) method is used (or Last In First Out (LIFO)).

What are some everyday applications of stacks? One that is easy to think about is the back button on your browser. Each time the back button is clicked it pulls the last page visited from the search history (a stack). In fact, if you click and hold on your back button you will see a drop down showing you the contents of the search history stack.
![Search History Stack](./Resources/browser_history.png)
^Each^ ^time^ ^a^ ^website^ ^is^ ^visited,^ ^it^ ^is^ ^pushed^ ^to^ ^the^ ^search^ ^history^ ^stack.^

The top of the list is the last page that was visited. Each time a new page is visited it is _pushed_ to the top of the stack (ex: searchHistory.append(_website_). Each time the back button is pressed, the top result is _popped_ from the stack (ex: searchHistory.pop(_website_)).
![Search History Pop](./Resources/browser_history_pop.png)
^Top^ ^website^ ^was^ ^popped^ ^from^ ^the^ ^stack^ ^when^ ^the^ ^back^ ^button^ ^was^ ^pressed.^

Here is a simple graphic to help understand the flow and layout of a stack: ![Stack Info Graphic](./Resources/stack.png)
^Image^ ^credit:^ ^https://www.geeksforgeeks.org/stack-data-structure-introduction-program/#:~:text=Stack%20is%20a%20linear%20data%20structure%20that%20follows,top%20of%20each%20other%20as%20a%20real-life%20example.^

In Python, the top of the stack is called the back of the stack. Stacks are a great data structure to use because they have O(1) performance on the main operations as no loops are used within those operations. The main operations include push(), pop(), empty(), and peek(). In Python these are performed as such:

| Stack Operation | Python Code         | Explanation                                 |
| --------------- | ------------------- | ------------------------------------------- |
| push(val)       | stack.append(val)   | Adds value to back of stack                 |
| pop()           | stack.pop()         | Removes and returns item from back of stack |
| empty()         | if len(stack) == 0: | Returns true if stack is empty              |
| peek()          | stack[0]            | Returns value from back of stack            |

## Real world use-cases

As mentioned before, the back button on the browser functions as a stack. Other common uses of a stack include the undo feature (ctrl+z), nested function calls and recursion, checking for balanced parenthesis, and the memory in your computer. When working with recursion or nested function calls, the first function called goes to the bottom of the stack while each subsequent function call gets added to the top.

## Code Example

When given a text document, find whether or not each line in the document has a balanced number of parenthesis, square brackets, and curly braces.

```
text = "balancedStack.txt"

def isBalanced(file):
    lineNum = 0
    with open(file, "r") as f:
        for line in f:
            balanced = True
            lineNum += 1
            stack = []
            for char in line:
                # if balanced is false don't check the other characters
                if balanced:
                    # put opening symbols in stack
                    if char == "(" or char == "{" or char == "[":
                        stack.append(char)

                    # if char does not match value at back of stack, balanced is false
                    elif char == ")":
                        if len(stack) == 0 or stack.pop() != "(":
                            balanced = False
                    elif char == "}":
                        if len(stack) == 0 or stack.pop() != "{":
                            balanced = False
                    elif char == "]":
                        if len(stack) == 0 or stack.pop() != "[":
                            balanced = False

            # balanced should be False if anything is left behind in the stack
            if len(stack) != 0:
                balanced = False

            # check value of balanced and return result
            if balanced:
                print(f"Line # {lineNum} is balanced")
            else:
                print(f"Line # {lineNum} is NOT balanced")


# Run the function
isBalanced(text)
```

For the given text file:

```
1  This is a paragraph with lots of random sentences (fun!).
2  It's purpose is to aid in an example of using a stack).
3  [Finding a balance in (), [], and {} can be so) easy!]
4  (If you {aren't having fun yet}, perhaps you are trying (TOO) hard?)
5  }Now, let's have [some{ (FUN!]
6  HI
7  ({[{({[[{(({[]}))}]]})}]})
8  ({[{({[[{(({[]}))}]]})}]}))
9  ()(

```

We can expect the following results:

```
Line # 1 is balanced
Line # 2 is NOT balanced
Line # 3 is NOT balanced
Line # 4 is balanced
Line # 5 is NOT balanced
Line # 6 is balanced
Line # 7 is balanced
Line # 8 is NOT balanced
```

## Try it for yourself

To apply this skill, try writing a program that utilizes a stack to return any given string as the reverse. Example:

| Given String             | Return String            |
| ------------------------ | ------------------------ |
| Frozen                   | nezorF                   |
| Into the unknown!        | !nownknu eht otnI        |
| I'll be a happy snowman! | !namwons yppah a eb ll'I |

Find the solution [here](stackExample.py).

### Resources Used

^-^ ^https://www.geeksforgeeks.org/stack-data-structure-introduction-program/#:~:text=Stack%20is%20a%20linear%20data%20structure%20that%20follows,top%20of%20each%20other%20as%20a%20real-life%20example.^

^-^ ^https://byui-cse.github.io/cse212-course/lesson03/03-teach_complicated_stack-solution.pdf^

^-^ ^https://byui-cse.github.io/cse212-course/lesson03/03-prepare.html^
