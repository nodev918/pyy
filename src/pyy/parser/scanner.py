from .tokenizer import Tokenizer

class Scanner:
    def __init__(self,file_name):
        self.code = ""
        self.index = 0
        with open(file_name,'r') as f:
            self.code = f.read()
        f.close()
        self.tokenizer = Tokenizer(self.code)
    
    def get(self):
        return self.code
    
    def print_char(self):
        index = 0
        for char in self.code:
            print(f"{index}: {repr(char)}")
            index += 1
    
    def go(self):
        self.tokenizer.tok(self.index)
        print(self.tokenizer.get())
        




# input = ""
# with open('input.yale','r') as f:
#     input = f.read()

# print(input)
# print(type(input))
# print("")



# index = 0
# for char in input:
#     print(f"{index}: {repr(char)}")
#     index += 1

# f.close()