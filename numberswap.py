num=int(input("enter the number:"))
int temp=num[0];
num[0]=num[-1];
num[-1]=temp;
print(num)
