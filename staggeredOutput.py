"""
The program works as expected in the Python IDLE Shell.

On CMD or PowerShell it buffers all the output and then prints it all at once.

Will look into.
"""


import random as r
import time

howLong = r.randint(200, 400)

for i in range(howLong):
    delay = r.randint(1, 3) * r.randint(1, 3) * r.randint(1, 3)
    character = r.randint(7700, 8200)
    print(chr(character), end="")
    time.sleep(delay/100)

print()
print("done")
