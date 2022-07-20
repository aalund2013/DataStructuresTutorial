# Data Structure Tutorial

Python Stacks, Linked Lists, and Trees
CSE212 Final Project
Adrianna Lund

## Welcome

In this tutorial we will define Stacks, Linked Lists and Trees. We will learn about the syntax and use cases for each of the data structures and then explore an example solution. Finally, we'll leave you with a challenge problem to solve on your own.

## The Stack

### Understanding the stack

First, we will explore the stack. When we talk about a stack, I want you to think about that pile of papers that has been building up in your office or kitchen counter (or wherever else you pile that stuff). To become the pile that it is, you set one paper on top of another, on top of another, on top of another, and so on. To clear it off, you'll need to review those papers. There is one easy and accessible way to empty that stack of papers. The last paper you placed in the pile will be the first one you pick up and process (for me, that mostly means throw away and occasionally stick it in a file.).

The same is true of a stack. When a program receives a function call it puts it on the stack. If no other requests come in, it processes that call. But for every request that comes in, it gets set on the top of the stack. Eventually one of two things happens - you overflow the stack (exceed the maximum number of requests on the stack) or it takes the last request it received and executes it. Then it continues to take the top request and execute it, until the stack is empty.

### Structure, key terms, and syntax

This is referred to as either LIFO - last in first out, or FILO - first in last out. The first item that goes into the stack will be the last item to be run. The last item added will be the first to run. You can see in the image below that the top (also called the front) of the stack is where the last item was added, the bottom (or the back) is where the first item added is found. To "push" an item means to add it to the top of the stack and to "pop" an item is to remove the top item. A stack is empty when there are no items in it.
![Stack Info Graphic](./Resources/stack.png)
[^(Picture^ ^from^ ^The^ ^DEV^ ^Community)^](https://res.cloudinary.com/practicaldev/image/fetch/s--s1Qbl8Gf--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/mwcwre09s12vqa3gvl7a.png)

### Code Example

One simple example of utilizing a stack is creating the reverse o
