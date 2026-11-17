# 02-04-04
# Problem: https://github.com/MrDebono/python-practice/blob/main/Unit-02/Chapter-04/02-04-04.md

n = int(input())

if n % 3 == 0 and n % 5 == 0:
    print("Fizz Buzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)
