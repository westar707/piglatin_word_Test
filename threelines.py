print('three lines')
print('Line one')
print('line two')
mystring = ('three lines')
f = open ('threelines.txt', 'wb')
f.write('three lines')
f.close()
f = open ('threelines.txt', 'a')
f.write('\n' + 'Hello')
f.close()