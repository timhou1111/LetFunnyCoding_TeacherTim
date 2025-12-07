# 題目描述
# 給你兩個字串 word1 和 word2。請將這兩個字串以交替順序合併，從 word1 開始。如果其中一個字串比另一個長，就把剩餘的字母接在合併後的字串最後面。
# 請回傳合併後的字串。

# 輸入：word1 = "abc", word2 = "pqr"
# 輸出："apbqcr"

# 解釋：合併過程如下：
# word1:  a   b   c
# word2:    p   q   r
# 合併後: a p b q c r
# ```

# ### 範例 2：
# ```
# 輸入：word1 = "ab", word2 = "pqrs"
# 輸出："apbqrs"

# 解釋：注意 word2 比較長，所以 "rs" 被接在最後面。
# word1:  a   b 
# word2:    p   q   r   s
# 合併後: apbqrs
# ```

# ### 範例 3：
# ```
# 輸入：word1 = "abcd", word2 = "pq"
# 輸出："apbqcd"

# 解釋：注意 word1 比較長，所以 "cd" 被接在最後面。
# word1:  a   b   c   d
# word2:    p   q 
# 合併後: a p b q c   d


# 限制條件

# 1 <= word1.length, word2.length <= 100
# word1 和 word2 只包含小寫英文字母

word_1 = input()
word_1_length = len(word_1)
word_2 = input()
word_2_length =len(word_2)

pick_number = 0
ans = ""

while word_1_length > pick_number and word_2_length > pick_number:
    ans = ans + word_1[pick_number]
    ans = ans + word_2[pick_number]
    pick_number += 1

while word_1_length > pick_number:
    ans = ans + word_1[pick_number]
    pick_number += 1

while word_2_length > pick_number:
    ans = ans + word_2[pick_number]
    pick_number += 1
    
print(ans)