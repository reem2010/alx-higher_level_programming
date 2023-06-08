#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv)
    if argc == 1:
        print("0 arguments.")
    else:
        print("{} arguments:".format(argc - 1))
        i = 1
        while i < argc:
            print("{}: {}".format(i, argv[i]))
            i = i + 1
