# First-in, First-out, dynamic set data structure
# no size cap
class Queue:

    # Initialize empty list of items and tail index to zero
    def __init__(self):
        self.items = []
        self.tail = 0

    # Return true if Queue is empty or false if not
    # Queue is empty if Tail index equals zero
    def isEmpty(self):
        if self.tail == 0:
            return True
        else:
            return False

    # Append item to end of list and increment Tail index
    def enqueue(self, item):
        self.items.append(item)
        self.tail += 1

    # Remove and return first item in list and decrement Tail index
    # if Queue underflows, or is empty, then return false
    def dequeue(self):
        if self.isEmpty():
            return False
        else:
            self.tail -= 1
            return self.items.pop(0)

    # Return first item in Queue
    # if Queue is empty, then return false
    def peek(self):
        if self.isEmpty():
            return False
        else:
            return self.items[0]

    # Print all of the items in the Queue
    # if no items exists, then print the Queue is empty
    def printQueue(self):
        if self.isEmpty():
            print 'Queue is empty'
        else:
            for item in self.items:
                print item
