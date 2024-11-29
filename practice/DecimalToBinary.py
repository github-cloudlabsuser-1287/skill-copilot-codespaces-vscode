# write a function to convert a decimal number to binary number
# input: 5
# output: 101
# input: 10
# output: 1010
# input: 15
# output: 1111

def decimalToBinary(n):
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * decimalToBinary(n // 2)

print(decimalToBinary(5))
print(decimalToBinary(10))
print(decimalToBinary(15))
print(decimalToBinary(0))
print(decimalToBinary(1))    