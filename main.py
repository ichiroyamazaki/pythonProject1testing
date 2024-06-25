def is_odd(num):
if num == 0:
return False
else:
return is_even (num - 1)

num = int(input("Enter a number: "))
if is_even(num):
print(str(num) + " is an even number.")
else:
print(str(num) + " is an odd number.")