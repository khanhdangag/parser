import re
import sys

rules = [
    (r"\d+", "NUMBER"),
    (r"\;", "SEMI"),
    (r"\:", "COLON"),
    (r"\,", "COMMA"),
    (r"\.", "DOT"),
    (r"\(", "LPAREN"),
    (r"\)", "RPAREN"),
    (r"\<", "LT"),
    (r"\>", "GT"),
    (r"\=", "EQ"),
    (r"\+", "PLUS"),
    (r"\-", "MINUS"),
    (r"\*", "MULTIPLY"),
    (r"\/", "DIVIDE"),
]

path = "input.txt"
input = ""
with open("input.txt", "r") as f:
    input = f.read().split()

print(input)
txt = "a<b"
x = re.search(rules[7], txt)
if x:
    print("YES! We have a match!")
else:
    print("No match")

