# 02-04-03
# Problem: https://github.com/MrDebono/python-practice/blob/main/Unit-02/Chapter-04/02-04-03.md

a = int(input())
b = int(input())
c = int(input())

tallest = a
if b > tallest:
    tallest = b
if c > tallest:
    tallest = c

print(tallest)
