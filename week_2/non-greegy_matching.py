import re as re

x = "From: This will also include in greedy : blah blah"

y = re.findall('^F.+:',x)
print(y)

z = re.findall('^F.+?:',x)
print(z)