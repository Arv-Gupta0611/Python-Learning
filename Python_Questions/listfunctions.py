l=[1,1.1,True,False,"qwerty",[1,2,3,49,50,6,70,8,99,10]]
l.append(2.2) #Adds single item at last of list
print(l)
l.extend("aaaaa")   #Take a iterable item as parameter and append each item in list
print(l)
l.insert(4,"popsticks")     # Insert item at desired position
print(l)
l.remove(2.2)       #Remove a certain item from the list
print(l)
l.pop()         #delete last item in return / if parmeter given delete that parameter
print(l)
print(len(l))       #return length of list
print(min(l[6]))    #Return minimuum of integer/float list
print(max(l[6]))    #Return maximum of integer/float list
print(sum(l[6]))    #Return sum
print(l.count('a'))     #count certain item in list by parsing through it
print(l.index(False))   #Return index of certain item
print(sorted(l[6]))     #return sorted list but its a temporary execution list will not mutate original object
print(l)            #print list with original object
#These two belows are permanent operations
l[6].reverse()          #Return reversed list
print(l)
l[6].sort()             #Return sorted list
print(l)
