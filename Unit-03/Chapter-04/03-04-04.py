# 03-04-04
# Problem: https://github.com/MrDebono/python-practice/blob/main/Unit-03/Chapter-04/03-04-04.md

s = input()
result = ""

for i in range(len(s)):
    if s[i] == " ":
        if result == "":
            result = str(i)
        else:
            result += ", " + str(i)

if result == "":
    print("no spaces found")
else:
    print(result)
