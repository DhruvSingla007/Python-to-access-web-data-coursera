import re

x = 'My favourite numbeer is 7 and I want to add 1.2 and 6.4 wich gives me a total of 7.6'

y = re.findall('[0-9]+', x)
print('y',y)

m  = re.findall('[0-9.]+',x)
print('m',m)

abc = "From dhruvsingla07@gmail.com Monday 13 April 2020"

z = re.findall('\S+@\S+',abc)
print('z',z)

a = re.findall('^From (\S+@\S+)', abc)
print('a',a)

b = re.findall('@(\S+)',abc)
print('b',b)

c = re.findall('^From.*@(\S+)', abc)
print('c',c)

