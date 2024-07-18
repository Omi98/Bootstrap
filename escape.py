# A simple code in python to generate encoded characters 
# for your HTML <pre> or <code> block.


import html 
import sys


code = sys.stdin.readlines()  # Press <ctrl-d> to end input

print()
print(f"\n\n»»———- Copy the below code & paste it in your html code block ———-««\n")
for line in code:
    line.splitlines()
    if len(line) != 0:
        code_modified = line.strip()
        print(html.escape(code_modified))
print()

# Characters include <, >, ", ', and &.