import re as re

handle = open('text.txt','r')

'''
for line in handle:
    line = line.rstrip()
    if re.search('^X.*', line):
        print(line)


for line in handle:
    line = line.rstrip()
    if re.search('^X.+', line):
        print(line)
'''

for line in handle:
    line = line.rstrip()
    if re.search('^X-\S+:', line):
        print(line)