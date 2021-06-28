import sys
import re
import pathlib

if len(sys.argv) > 1:
    fileName = sys.argv[1]
else: # if no arg, ask for input
    fileName = input("Please enter filename: ");

file =pathlib.Path(fileName)
# check that input matches an existing file
if file.exists ():
    print()
else:
    print("Can't find file", file)
    sys.exit()

data = open(file, "r")

relregex = re.compile(r"(.*)mca[1-8](.*)")
oneregex = re.compile(r"(^[^1\s])")
elemregex = re.compile(r"(\A[A-Z][a-z]?)(\s)([KL]a)")
outregex = re.compile(r"(^[^Output])")

for line in data:
    if re.match(relregex, line):  # find lines with mca[1-8]
        if re.match(oneregex, line):   # remove lines starting with 1
            if re.match(outregex, line):    # remove lines starting with Output
                        line = line.replace(",", "")  # remove all comas
                        line = re.sub(elemregex,r"\1_\3", line)
                        line = re.sub(r" +",",",line)
                        sys.stdout.write(line)
                    
data.close()
print("Done!")
