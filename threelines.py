<<<<<<< HEAD

mylines = [
=======
lines = [
>>>>>>> d9e5289b8b9bd9b65f0db4e80acac834f8f290e4
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
<<<<<<< HEAD
print(x)
f.close()
with open('threelines.txt', 'w') as f:
    for items in x:
        f.write("%s\n" % items)
=======
print(lines)
f.close()
>>>>>>> d9e5289b8b9bd9b65f0db4e80acac834f8f290e4
