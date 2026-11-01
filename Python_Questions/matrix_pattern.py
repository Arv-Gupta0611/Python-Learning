# for i in range(5):      # No. of rows 
#     for j in range(5):  # No. of columns
#         print('*', end="  ")
#     print()
# print()
# print()
# for i in range(5):      # No. of rows 
#     for j in range(5):  # No. of columns
#         print(j, end="  ")
#     print()
# print()
# print()
# for i in range(5):      # No. of rows 
#     for j in range(5):  # No. of columns
#         print(i, end="  ")
#     print()
# print()
# print()
# for i in range(5):      # No. of rows 
#     for j in range(5):  # No. of columns
#         print(i,j, end="  ")
#     print() 
# print()
# print()
# for i in range(1,6):      # No. of rows 
#     for j in range(1,i+1):  # No. of columns
#         print(j, end="  ")
#     print()

# # 1  
# # 1  2  
# # 1  2  3  
# # 1  2  3  4  
# # 1  2  3  4  5
# print()
# print()
# for i in range(1,6):      # No. of rows 
#     for j in range(1,i+1):  # No. of columns
#         print(i, end="  ")
#     print()

# # 1  
# # 2  2  
# # 3  3  3  
# # 4  4  4  4  
# # 5  5  5  5  5
# print()
# print()
# for i in range(1,5):      # No. of rows 
#     for j in range(1,i+1):  # No. of columns
#         print('*', end="  ")
#     print()
# print()
# print()

# n=int(input('Enter No. of Rows '))
# for i in range(1,n+1):      # No. of rows 
#     for j in range(1,i+1):  # No. of columns
#         print('*', end="  ")
#     print()


n=int(input('Enter No. of Rows '))
for i in range(1,n):      # No. of rows 
    for j in range(1,i+1):  # No. of columns
        if(i%2==0):
            print(i, end="  ")
        else:
            print('*', end="  ")
    print()