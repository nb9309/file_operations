try:
    r = open('file_1.py','r')
except FileNotFoundError:
    print('file is not exist')
else:
    print('file opend in read mode')
    print('is file colsed', r.closed)
    print(type(r))
finally:
    r.close()
    print('is file colsed', r.closed)