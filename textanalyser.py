#This analyses texts in a file and returns the composition of each letter as a percentage

def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

file = open("newfile.txt", "w")
file.write("""Programmers funny facts
Programmmers will start the count from zero and not one
The root is at the top of the tree
Prograaming is different from coding
CtrlC and CtrlV have saved more lives that Batman and Robin
CTrlZ is better than a time machine
There is one thing called constant variable
Programmmers always look for a girl who can code
When you format your hard drive the files are not deleted
Mbps and MBps internet connection dont mean the same thing
Programmers are the main source of income for eye doctors
Programmmers love to code day and night
Sleeping with a problem can actually solve it
""")
file.close()
filename = "newfile.txt"
with open(filename) as f:
    text = f.read()

for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * (count_char(text, char) / len(text))
    print("{0} - {1}%".format(char, round(perc, 2)))

