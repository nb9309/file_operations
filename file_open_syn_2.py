try:
    with open('file_2.py','w') as op:
        print('is file colsed', op.closed)
except FileNotFoundError:
    print('file not exist')
else:
    print('file opend in w mode')
    print('is file colsed', op.closed)