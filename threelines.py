lines = [
    'this is a line',
    'this is another line',
    'this is a last line'
]
f = open ('threelines.txt', 'w')
f.write('add new line')
f.close()
f = open ('threelines.txt', 'r')
lines = f.read()
print(lines)
f.close()
