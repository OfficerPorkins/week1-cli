name = "OfficerPorkins"
print("Hello,", name)

age = 28
print(age + 1)

numbers = [4, 8, 15, 16, 23, 42]
for n in numbers:
    if n > 10:
        print(n)

def is_even(n):
    return n % 2 == 0 
 # == means true or false, % means remainder, so if the remainder is 0 then it is even   

print(is_even(4))
print(is_even(7))

def sum_over_ten(numbers):
    total = 0
    for n in numbers:
        if n > 10:
            total = total + n
    return total

print(sum_over_ten([4, 8, 15, 16, 23, 42]))