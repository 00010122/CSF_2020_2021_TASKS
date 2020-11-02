number = int(input("Enter a decimal number: "))
option = input("Choose the option:\n 'I' for Integer\n 'B' for Binary\n 'O' for Octal\n 'H' for Hexadecimal\n"
               " Type 'All' to see all options ")
if option.upper() == "I":
    print("Integer - ", int(number))
elif option.upper() == "B":
    print("Binary - ", bin(number))
elif option.upper() == "O":
    print("Octal - ", oct(number))
elif option.upper == "H":
    print("Hexadecimal - ", hex(number))
elif option.upper() == "ALL":
    print("Integer -", int(number))
    print("Binary - ", bin(number))
    print("Octal - ", oct(number))
    print("Hexadecimal - ", hex(number))
else:
    print("Please type available option")
