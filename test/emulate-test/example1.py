import dis

def cond():
    x = 3
    if x < 5:
        return 'yes'
    else:
        return 'no'

print(cond)
print("")
print(cond.__code__)

cond_byte = cond.__code__.co_code
print("")
print(cond_byte)
print("")
print(list(cond_byte))
print("")
print(dis.dis(cond))