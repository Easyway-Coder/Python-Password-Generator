from string import *
import random

ch = ""
ln = int(input("Enter length of password: "))
typ = input("Enter type of password: ")
g_pass = ""

# L - Lowercase
if "l" in typ:
    ch += ascii_lowercase
# D - Digits
if "d" in typ:
    ch += digits
# U - Uppercase
if "u" in typ:
    ch += ascii_uppercase
# S - Symbols
if "s" in typ:
    ch += punctuation


for i in range(ln):
    g_pass += random.choice(ch)

print("Password Generated:", g_pass)
