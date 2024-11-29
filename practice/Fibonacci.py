# write a function to return the nth value of the Fibonacci sequence
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(0)) # 0
print(fibonacci(1)) # 1
print(fibonacci(2)) # 1
print(fibonacci(3)) # 2
print(fibonacci(4)) # 3
print(fibonacci(5)) # 5
print(fibonacci(6)) # 8
print(fibonacci(7)) # 13    