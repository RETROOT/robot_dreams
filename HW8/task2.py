first = set(input("write a numbers: "))
second = set(input("write a numbers: "))

def unique_elements(first, second):
    return first.symmetric_difference(second)
unique=unique_elements(first,second)
print(unique)
