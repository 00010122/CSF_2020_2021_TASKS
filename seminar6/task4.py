def compare_function():
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1

x = int(input("Enter a number "))
y = int(input("Enter a number "))

print(compare_function())
