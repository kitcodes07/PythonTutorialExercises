from os import strerror

data = bytearray(10)
"""
for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
"""
# Your code that reads bytes from the stream should go here.
try:
    bf = open('file.bin', 'rb')
    bf.readinto(data)
    #ch = bf.read(1)
    """
    while ch != '':
        print(chr(ch), end='')
        ch = bf.read(1)
    """
    bf.close()
    for b in data:
        print(b, end=" ")


except IOError as e:
    print("I/O error occurred:", strerror(e.errno))