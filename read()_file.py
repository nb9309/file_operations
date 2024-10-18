
file = input('enter file name: ')
with open(file) as fp:
    data = fp.read()
    print(data)
print('is file closed',fp.closed)