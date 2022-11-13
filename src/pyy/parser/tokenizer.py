class Tokenizer:
    def __init__(self,code):
        self.code = code
        self.token = ""
    def tok(self,index):
        _return = ""
        while self.code[index] != ' ' and self.code[index] != '(':
            ch = self.code[index]
            _return += ch
            index += 1
        self.token = _return
        return _return
        
    def get(self):
        return self.token