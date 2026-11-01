#1/1!+2/2!+3/3!+4/4!+5/5!+6/6!+7/7!+8/8!+9/9!+10/10!
num = int(input('Enter no. of terms:'))
result=0
fact=1;
for i in range(1,num+1):
    fact=fact*i
    result=result+(i/fact)
print(f'Sum of sequence is {result}')    
