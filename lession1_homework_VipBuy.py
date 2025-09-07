# 輸入資料
print("會員等級: 1.VIP  2.金卡  3.銀卡  4.非會員")
member = int(input("請選擇會員等級(1-4): "))
price = float(input("請輸入商品單價: "))
quantity = int(input("請輸入購買數量: "))

# 計算原始總金額
total = price * quantity
print(f"\n原始金額: {total}元")

# 數量折扣：3件以上每件減20元
if quantity >= 3:
    total = total - (quantity * 20)
    print(f"數量折扣: -{quantity * 20}元")

# 會員等級折扣
if member == 1:  # VIP
    total = total * 0.85  # 15%折扣
    print("VIP折扣: 85折")
elif member == 2:  # 金卡
    total = total * 0.9   # 10%折扣
    print("金卡折扣: 9折")
elif member == 3:  # 銀卡
    total = total * 0.95  # 5%折扣
    print("銀卡折扣: 95折")

# 購買金額折扣
if total >= 2000:
    total = total * 0.8  # 8折
    print("滿2000元: 再8折")
elif total >= 1000:
    total = total * 0.9  # 9折
    print("滿1000元: 再9折")

print(f"\n最終金額: {total:.0f}元")