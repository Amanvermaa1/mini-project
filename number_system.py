a = int(input('enter starting no. : '))
b = int(input('enter ending no. : '))
c = int(input('enter updation no. : '))
fr = int(input(' enter 0: for forward and 1 : for reverse order : '))
hv =int(input('0: for horizontal and 1 : for vertical : '))
if fr==0:
    if hv==0:
        for i in range(a,b,c):
            print(i,end=",")
    elif hv == 1:
        for i in range(a,b,c):
            print(i)
if fr==1:
    if hv==0:
        for i in range(b,a,-c):
            print(i,end=",")
    elif hv == 1:
        for i in range(b,a,-c):
            print(i)
else:
    print('invalid')

# if fr==0 and hv==0:
#     for i in range(a,b,c):
#         print(i,end=",")
# if fr==0 and hv==1:
#     for i in range(a,b,c):
#         print(i)
# if fr==1 and hv==0:
#     for i in range(b,a,-c):
#         print(i,end=",")
# if fr==1 and hv==1:
#     for i in range(b,a,-c):
#         print(i)
# else:
#     print('invalid')