import sys
import os


if len(sys.argv) != 4:
    print("Użycie: calc.py <num1> < + - > <num2>")
    sys.exit(1)

num1 = int(sys.argv[1])
op = sys.argv[2]
num2 = int(sys.argv[3])

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
else:
    print("Zły operator")
    sys.exit(1)

with open("./tmp/wynik.txt", "w") as file:
    file.write( str(result))

print( result )
