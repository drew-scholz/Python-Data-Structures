# Last-in, First-out, dynamic set data structure
# no size cap
class Stack:

    # Initialize empty list of Items and set Top index to zero
    def __init__(self):
        self.items = []
        self.top = 0

    # Return true if Stack is empty or false if not
    # Stack is empty if Top index is zero
    def isEmpty(self):
        if self.top == 0:
            return True
        else:
            return False

    # Append Item to end of Stack and increment Top index
    def push(self, item):
        self.items.append(item)
        self.top += 1

    # Remove the last Item from the Stack and decrement Top index,
    # if Stack underflows, or is empty, then return false
    def pop(self):
        if self.isEmpty():
            return False
        else:
            self.top -= 1
            return self.items.pop()

    # Return last Item without removing it,
    # if Stack is empty, then return false
    def peek(self):
        if self.isEmpty():
            return False;
        else:
            return self.items[self.top - 1]

    # Print all of the Items in the Stack
    # if no Items exists, then print the Stack is empty
    def printStack(self):
        if self.isEmpty():
            print 'Stack is empty'
        else:
            for item in self.items:
                print item
                