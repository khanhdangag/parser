import re

patern = re.compile(r"\and")

if patern.match("and"):
    print("True")
else:
    print("False")
