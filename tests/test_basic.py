from . import vmtest
from . import parsertest
class TestBasic(vmtest.VMTest, parsertest.ParserTest):
    def __init__(self):
        print("init TestBasic")
    
    def test_variable(self):
        self.assert_parser_ok("example code")
        self.assert_vm_ok("example ast")
        