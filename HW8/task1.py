first = set(input("write numbers: "))
second = set(input("write numbers: "))
def same_elements(first, second):
    return first & second
same = same_elements(first,second)
print(same)
