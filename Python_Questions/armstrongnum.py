num=int(input('Enter the number'))
lennum=num
n=num
# power=len(str(num))
power=0
result=0
digit=0
while(lennum>0):
    power+=1
    lennum=lennum//10
while(n!=0):
    digit=n%10
    result=result+digit**power
    n=n//10
if(result==num):
    print('Armstrong Number',num)
else:
    print('Not a armstrong no.', num)

#-----------------------------------------------------------------

num=int(input("Enter Number to check for Armstrong No. : "))
original=num
length=len(str(num))
result=0
while(original>0):
    rem=original%10
    result+=rem**length
    original=original//10
if(result==num):
    print(num," is an armstrong Number ")
else:
    print(num," is not a Armstrong no.")