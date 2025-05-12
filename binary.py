def binary_decimal(num):
    if num>=1:
        binary_decimal(num//2)
    print(num%2, end=" ")
binary_decimal(10)