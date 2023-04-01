def arg_adds (*args):
    arg = input("Write args with spaces :") .split()
    result = sum(map(int, arg))
    return result

print(arg_adds())