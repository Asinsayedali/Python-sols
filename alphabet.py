n = int(input("enter the number"))
digit_sum =0
reversed_digit=0
while n > 0:
    last_digit = n%10
    digit_sum += last_digit
    reversed_digit = reversed_digit*10 + last_digit
    n = n//10
print(digit_sum)
print(reversed_digit)