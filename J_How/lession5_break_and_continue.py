####迴圈的控制
##跳過或是終止迴圈的執行

######continue#######

#continue -->這回合不做，進入下個回合

#friend = ["Tim", "Tommy", "gaygay", "Lisa", "Vic", "terPe"]

# for i in range(len(friend)):
#     if friend[i] == "Lisa":
#         continue #我這『迴圈』後面的東西都不做
        
#     print(f"親你一下    {friend[i]}")

# for i in friend:
#     if i == "Lisa": #輪流當
#         continue #我這『迴圈』後面的東西都不做
        
#     print(f"親你一下{i}")





#######break#######
# 破壞整個迴圈，直接把它給廢了


friend = ["Tim", "Tommy", "gaygay", "strongGay", "Lisa", "Vic", "terPe"]


for i in friend:
    if i == "strongGay": #輪流當
        break #我這『迴圈』後面的東西都不做
        
    print(f"親你一下{i}")


###善用in 與 not in 來判斷陣列 裡面是否有這個值

man = "Max"

friend = ["Tim", "Tommy", "gaygay", "strongGay", "Lisa", "Vic", "terPe"]

print(man in friend) # True
print(man not in friend) # Flase

if man in friend:
    print("已經有這個朋友了")

if man not in friend:
    print("不認識")




