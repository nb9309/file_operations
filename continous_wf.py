with open('file_1','a') as fp:
    while 9:
        ch = input('enter value: ')
        if ch == '@':
            break
        else:
            fp.writelines('\n'+ch)
print('is file closed',fp.closed)