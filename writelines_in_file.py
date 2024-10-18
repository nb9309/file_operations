lst = {'hii',100,3.5,2+5j,'python','what'}
with open('wl_file','a') as fp:
    fp.writelines(str(lst)+'\n')
    print(type(fp))
print('is file closed',fp.closed)