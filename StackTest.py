from Stack import Stack;
import unittest

class TestStackMethods(unittest.TestCase):

    def test_stack(self):
        stack = Stack();
        stack.push(4);
        self.assertEqual(stack.peek(), 4);
        stack.push(2);
        self.assertEqual(stack.peek(), 2);
        stack.push(-1);
        self.assertEqual(stack.peek(), -1);
        stack.push("A");
        self.assertEqual(stack.peek(), -1);
        stack.pop();
        self.assertEqual(stack.peek(), 2);
        stack.pop();
        self.assertEqual(stack.peek(), 4);
        stack.push(10);
        self.assertEqual(stack.peek(), 10);
        stack.push(5);
        self.assertEqual(stack.peek(), 5);
        stack.pop();
        self.assertEqual(stack.peek(), 10);
        stack.pop();

if __name__ == '__main__':
    unittest.main()
