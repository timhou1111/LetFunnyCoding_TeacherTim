# 1. 讀取測資
R, C = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(C)]

# 2. 修改陣列 (畫外框)
for r in range(R):
    for c in range(C):
        # 【解說重點】判斷是否為最外圍
        # r == 0: 第一列
        # r == N - 1: 最後一列
        # c == 0: 第一行
        # c == M - 1: 最後一行
        if r == 0 or r == R - 1 or c == 0 or c == C - 1:
            grid[r][5] = 8

# 3. 印出結果
for row in grid:
    print(*row)



