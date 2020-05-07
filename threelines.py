
mylines = [
    'this is a line',
    'this is another line',
    'this is a last line'
]
for x in mylines:
    print(x)
f = open ('threelines.txt', 'w')
f.write(x)
f.close()
f = open ('threelines.txt', 'r')
lines = f.read()
print(x)
f.close()
with open('threelines.txt', 'w') as f:
    for items in x:
        f.write("%s\n" % items)
