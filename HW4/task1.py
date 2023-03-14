text = input("write a text:")

if not text.isalpha():
    print("this is a number")

    if (int(text) % 2) == 0:
        print("Number is even")
    else:
        print("Number is odd")
else:
    print("This is a word")
    len_text = len(text)
    print(f"This word has a {len_text} letters")
