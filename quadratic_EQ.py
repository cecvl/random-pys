# ax**2 + bx + c
# use a = 1,b = 3 ,c = -4
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
# two possible solutions
# +(sqrt)
x = (-b + (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
print(x) # 1
print("or")
# -(sqrt)
x2 = (-b - (b ** 2 - 4 * a * c)** 0.5) / 2 * a
print(x2) # -4