# 导入随机工具包
import random

# 控制台输出你的选择（1.石头 2.剪刀 3.布）
player = int(input("控制台输出你的选择（1.石头 2.剪刀 3.布）"))

# 电脑随机出拳（目前只能出石头）
computer = random.randint(1, 3)
print("玩家选择是 %d - 电脑的选择是 %d" % (player, computer))

# 比较胜负
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("人类牛皮！")
elif player == computer:
    print("平分秋色")
else:
    print("电脑牛皮")