#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", 3)
say_my_name(3, "Smith")
try:
    say_my_name()
except Exception as e:
    print(e)
