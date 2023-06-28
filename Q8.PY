class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0


def reverse_string(input_string):
    stack = Stack()
    reversed_string = ""

    for char in input_string:
        stack.push(char)
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string

input_str = "Hello, World!"
reversed_str = reverse_string(input_str)
print("Reversed string:", reversed_str)