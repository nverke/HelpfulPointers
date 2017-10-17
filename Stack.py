# Create a class from scratch (look it up) that implements a stack.
# The class should have the following three functions.
# Push(n): puts n on the top of the stack.
# Pop(): removes and returns the value on top of the stack.
# Peek(): returns but does not remove the value ontop of the stack.
#
# Examples:
# -------------------
# stack = new Stack()
# stack.push(3)
# stack.push(6)
# stack.push(4)
# stack.peek() [should return 4]
# stack.pop() [also returns 4]
# stack.pop() [should return 6]
# -------------------

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.insert(0,item)

     def pop(self):
         return self.items.pop(0)

     def peek(self):
         return self.items[0]

     def size(self):
         return len(self.items)

def Stacker():
    stack = Stack();
	item = int(raw_input("hey, define a variable already."));
	print ("Hey whatcha want to do?");

	menu = int(raw_input("1:push my var 2: pop a var 3: peek at stack");

	output = 0

	if (menu == 1):
		s.push(item);
	elif (menu == 2):
		print(s.pop()));
	elif (menu == 3):
		print(s.peek());
	else
		print("U failed to use the menu");

	return output;

while(output == 0):
	output = Stacker();

Stacker()
