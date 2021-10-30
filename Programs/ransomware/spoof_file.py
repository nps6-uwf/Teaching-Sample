from os import rename
from sys import argv


RTOL = "\u202e"
MASK = argv[3] if len(argv) > 3 else "txt"

rename(f"{argv[1]}.{argv[2]}", f"{argv[1]} {RTOL}{MASK}.{argv[2]}")