import pytest
from ..pyy.parser.tokenizer import Tokenizer
@pytest.fixture
def file_name():
    return 'input.yale'

@pytest.fixture
def code(file_name):
    code = ""
    with open(file_name,'r') as f:
        code = f.read()
    f.close()
    return code

@pytest.fixture
def tokenizer():
    return Tokenizer
 

class TestTokenizer:
    def test_token(self,code,tokenizer):
        t = tokenizer(code)
        t.tok(5)
        assert t.get() == "func"