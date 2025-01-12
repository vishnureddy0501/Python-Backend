import random
class Dice:
    def Roll(self):
        coordinateX = random.randint(1, 6)
        coordinateY = random.randint(1, 6)
        point = f"({coordinateX}, {coordinateY})"
        print(point)
dice1 = Dice()
dice1.Roll()