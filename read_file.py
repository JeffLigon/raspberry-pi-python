# Open and read a file from command-line argument
import sys

if (len(sys.argv) != 2):
    print("Usage: python ReadFile.py filename")
    sys.exit()

scriptname = sys.argv[0]
filename = sys.argv[1]

file = open(filename, "r")
lines = file.readlines()
file.close()

for line in lines:
    print(line, end = '')