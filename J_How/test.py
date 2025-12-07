word1 = input() 
word2 = input()
x = []
a = 0

for i in range (len(word1)+len(word2)):
    print("i is",i)
    if (a == 0):
        if (i%2 == 0):
            x.append(word1[int((i)/2)])
            print("(word1) x is",x)
            if (int((i)/2+1)>=len(word1)):
                a = 1
                print("into a1")
                continue
        else:
            x.append(word2[int((i-1)/2)])
            print("(word2)x is",x)
            if (int((i-1)/2+1)>=len(word2)):
                a = 2
                print("into a2")
                continue
    if (a==1):
        x.append(word2[i-len(word1)])
    if (a==2):
        x.append(word1[i-len(word2)])

print("final",x)
for j in range (len(x)):
    print(x[j], end="")