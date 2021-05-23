#!/usr/bin/env python3

import re

def is_ok(text):
    match = re.match("[0-9 \-+*/()]+$", text)
    return bool(match)


input_string = input("Task: ")

if is_ok(input_string):
    # Разделение строки на цифры и действия
    actions = input_string.split(" ")
    print (actions)
else:
    # Напечатать что введен кривой пример
    print ("Кривой пример")

