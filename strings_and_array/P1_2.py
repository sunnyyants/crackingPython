__author__ = 'SunnyYan'

# Reverse a null terminal string
# I decide to use 3 different methods

def method1(strings):
    if len(strings) == 1:
        return strings
    return method1(strings[1::1]) + strings[0]

def method2(strings):
    return strings[::-1]

def method3(strings):
    i = len(strings)-1
    result = []
    while(i >= 0):
        result.append(strings[i])
        i -= 1
    return ''.join(result)

print method1("abcdefg")
print method2("1234567")
print method3("leveleivia")