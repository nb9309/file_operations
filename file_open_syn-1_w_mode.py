try:
    o = open('file_1.py','w')
except FileNotFoundError:
    print('this file is not exist')
else:
    print('file opened')