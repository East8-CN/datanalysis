import difflib
import sys

a = open('my.txt', 'r').readline()
b = open('new.txt', 'r').readline()
diff = difflib.ndiff(a, b)
sys.stdout.writelines(diff)
