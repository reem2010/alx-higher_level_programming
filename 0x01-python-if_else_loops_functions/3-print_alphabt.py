#!/usr/bin/python3
i = 97
s = ""
while (i < 123):
    if i != 113 and i != 101:
        s = s + chr(i)
        i = i + 1
print("{}".format(s), end="")
