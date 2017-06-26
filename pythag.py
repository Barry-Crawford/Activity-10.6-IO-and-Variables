import math
SideA = input("What is the length of Side A: ")
SquareA = SideA * SideA
SideB = input("What is the length of Side B: ")
SquareB = SideB * SideB
SquareC = SquareA + SquareB
SideC = math.sqrt(SquareC)
print "The Length of Side C is {}".format(SideC)
