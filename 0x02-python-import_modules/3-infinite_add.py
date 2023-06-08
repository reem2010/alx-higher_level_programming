#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    argc = len(argv)
    i = 1
    while i < argc:
        sum = sum + int(argv[i])
        i = i + 1
    print("{}".format(sum))
