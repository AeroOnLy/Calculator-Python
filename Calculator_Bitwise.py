def andd(number_1 , number_2):
    return number_1 & number_2

def orr(number_1 , number_2):
    return number_1 | number_2

def xorr(number_1 , number_2):
    return number_1 ^ number_2

def nott(number_1 , number_2):
    return ~ number_1

print("Hi, I am a Calculator!")
print("Please select which of the following arithematic operation you want me to perform-\n" \
        "1. Bitwise AND (&)\n" \
        "2. Bitwise OR (|)\n" \
        "3. Bitwise XOR (^)\n" \
        "4. Bitwise NOT (~)\n")

operation = int(input("1, 2, 3, 4 : "))

number_1 = int(input('Please, Enter the first number: '))
number_2 = int(input('Please, Enter the second number: '))

if operation == 1:
    print(number_1, "&", number_2, "=", andd(number_1, number_2))

elif operation == 2:
    print(number_1, "|", number_2, "=", orr(number_1, number_2))

elif operation == 3:
    print(number_1, "^", number_2, "=", xorr(number_1, number_2))

elif operation == 4:
    print(number_1, "~", number_2, "=", nott(number_1, number_2))

else:
    print("Please enter valid input")
