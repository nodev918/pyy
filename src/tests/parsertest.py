from ..pyy.parser.parser import Parser

class ParserTest:
    def __init__(self):
        print("init ParserTest")
    
    def assert_parser_ok(self, code):
        p = Parser(code)
        print(p.get())