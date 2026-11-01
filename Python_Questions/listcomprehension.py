l=[12,23,34,45,56,67,78,89,90,0,11,22,33,44,55,66,77,88,99,10,123,234,345,456,567,678,789,890,901]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
newlist=[i*2 for i in l]        #1D
print(newlist)
        #2D                          #outer          #inner
newlist1=[ print(j+1000,end=" ") for i in matrix for j in i]
print()
                                    #inner        #outer
newlist2=[[ print(j+1000,end=" ") for j in i] for i in matrix ]