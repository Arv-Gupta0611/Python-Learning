i=int(input('Enter a integer--> '))
num=0
temp=i
while(temp!=0):
    r=temp%10
    temp=temp//10
    num=(num*10)+r
if (i==num):
    print(i,' is a palindrome no.')
else:
    print(i,' is not a palindrome no.')
