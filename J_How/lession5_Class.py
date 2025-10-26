# 什麼是Class(類別/物件)? --> 用程式建立一個這個世界上的任何物體（車子，人物，書籍，網購訂單.......）
# 

class BaskertBallPlayer:
    def __init__(self, player_name, player_position): #當底建構籃球員時，他必須『天生具備』什麼『屬性』
        self.name = player_name
        self.position = player_position
        self.shoot_point = 0
    
    def show(self):
        print("########本場數據###########")
        print(self.name)
        print(self.position)
        print(self.shoot_point)

    def shoot(self, ball):
        if ball == "三分球":
            print("投進三分")
            self.shoot_point +=3
        elif ball == "兩分球":
            print("投進兩分")
            self.shoot_point +=2

    def game_over(self):
        self.shoot_point = 0
        print("比賽結束，下場比賽得分歸0")
        


p1 = BaskertBallPlayer("Curry", "控球後衛")
p2 = BaskertBallPlayer("Kuminga", "小前鋒")


print(p2.position)
p2.position = "得分後衛"
print(p2.position)

p2.shoot("三分球")
p2.shoot("三分球")
p2.shoot("兩分球")
p2.shoot("三分球")

p2.show()

#隨機取數
import random
print(random.randrange(1,101))


