# x = int(input())

# for i in range(x):
#     y = [int(i) for i in input().split()]
#     diff = 0
#     fif_num = 0
#     if y[1] - y[0] == y[2] - y[1] == y[3] - y[2]:
#         diff = y[1] - y[0]
#         fif_num = y[3] + diff
#     elif y[1] // y[0] == y[2] // y[1] == y[3] // y[2]:
#         diff = y[1] // y[0]
#         fif_num =  y[3] * diff
    
#     y.append(fif_num)
#     print(" ".join(map(str,y)))




x = [1,2,3,4,5]

print(x)

print(" ".join(map(str,x)))
# # print(" ".join(map(int,x)))


# rownum = input()
# for i in range(int(rownum)):
#     y = input()
#     z = y.split()
#     [2,4,6,8]
#     if int(z[3])/int(z[2]) == int(z[2])/ int(z[1]):
#         z.append(int(int(z[1])/int(z[0])* int(z[3])))  
#         print(z)
#     else:
#         z.append(int(int(z[1])-int(z[0])+ int(z[3]))) 
#         print(z)