item_list = input("write a letters: ")
def setup_upper():
    upper_list=list(map(str.upper, item_list))
    return upper_list
print(setup_upper())