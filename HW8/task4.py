some_list = input("write something: ")

def is_number(s):
    return s.isdigit()
numbers= list(filter(is_number, some_list))
print(numbers)