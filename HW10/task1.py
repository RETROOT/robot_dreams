def print_numbers(n):
    if n == -1:
        return
    print(n)
    print_numbers(n - 1)

number = int(input("Print the number: "))
print_numbers(number)