from ..pyy.vm.vm import VirtualMachine

class VMTest:
    def __init__(self):
        print("init VMTest")
    
    def assert_vm_ok(self, ast):
        vm = VirtualMachine(ast)
        print("assert_ok")