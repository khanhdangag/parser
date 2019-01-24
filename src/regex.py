import re

patern = re.compile(r"(?i)^[a-zA-Z]+[0-9]*i")

if patern.match("ABc"):
    print("True")
