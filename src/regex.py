import re

patern = re.compile(r"\;")

if patern.match(";"):
    print("True")
else:
    print("False")
