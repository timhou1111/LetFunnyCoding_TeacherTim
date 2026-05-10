grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 魔法一：【上下翻轉】
# 原理：直接把最外層的 Row 順序顛倒
fast_up_down = grid[::-1]


# 魔法二：【左右翻轉】
# 原理：Row 順序不變，但把每一條 Row 裡面的數字顛倒
fast_left_right = [row[::-1] for row in grid]








#翻轉90度
def rotate_90_cw(grid):
    R = len(grid)       # 原本的總列數
    C = len(grid[0])    # 原本的總行數
    
    # 新矩陣的長寬要「互換」！
    # 宣告一個 C 列 R 行的空矩陣 (外層跑 C 次，內層產生 R 個 0)
    new_grid = [[0] * R for _ in range(C)]
    
    for r in range(R):
        for c in range(C):
            # 依照剛剛推導的公式填入
            new_grid[c][R - 1 - r] = grid[r][c]
            
    return new_grid





#zip拉鏈打包
#zip() 的本業是「把多個串列的第一個元素綁在一起，再把第二個元素綁在一起」。


names = ["小明", "小華", "小美"]
scores = [85, 92, 100]

# zip 把兩個串列拉在一起，每次迴圈吐出一對 (name, score)
for name, score in zip(names, scores):
    print(f"{name} 的分數是 {score}")


grid = [
    [1, 2, 3],
    [4, 5, 6]
]


rotated = [list(row)[::-1] for row in zip(*grid)]
print(*rotated)