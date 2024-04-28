age=int(input("enter age : "))
name=input("enter name : ")
if(age>=18):
    print(name)
    print("eligible to vote")
    print("1.BJP 2.AAP 3.CONGRESS 4.BSP")
    choice=int(input("vote to : "))
    if choice==1:
        print("BJP")
    elif choice==2:
        print('aap')
    elif choice==3:
        print("congress")
    elif choice==4:
        print('BSP')
else:
        print(' You are not eligible to vote')
