class VirtualMachine:
    
    def __init__(self, ast):
        print("init VirtualMachine")
        self.frame = Frame()
        self.ast = ast
    
    def get(self):
        return self.ast

    def pop_frame(self):
        self.data_stack.pop()

class Frame:
    
    stack = []
    
    def __init__(self):
        print("init Frame")

    def pop_stack(self):
        self.stack.pop()