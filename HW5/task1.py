text = input("Print text: ")

for txt in text:
    if txt.isdigit():
        if int(txt) % 2 == 0:
            print(txt + " is even.")
        else:
            print(txt + " is odd.")
    elif txt.isalpha():
        if txt.isupper():
            print(txt + " is cappital letter.")
        else:
            print(txt + " is a lowercase letter.")
    else:
        print(txt + " is a symbol.")
