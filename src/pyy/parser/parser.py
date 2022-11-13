from .scanner import Scanner

class Parser:
    def __init__(self,file):
        self.scanner = Scanner(file)
    
    def get(self):
        return self.scanner.get()
    
    def print_char(self):
        return self.scanner.print_char()

    def go(self):
        self.scanner.go()

# p = Parser('input.yale')
# print(p.get())
# p.print_char()