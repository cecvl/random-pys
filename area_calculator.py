print("================")
print("AREA CALCULATOR")
print("================")

print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Exit")

pi = 22/7

choice = 0
while choice > 5 or choice < 1:
    choice = int(input("Enter choice : "))

# syntax: float(input()) NOT input(float())

match choice:
    case 1:
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            area = base * height / 2
            print("Area of Triangle: " + str(area))                  
    case 2:
            length = float(input("Enter length: "))
            breadth = float(input("Enter breadth: "))
            area = length * breadth
            print("Area of Rectangle: " + str(area))
    case 3:
            side = float(input("Enter side: "))
            area = side * side
            print("Area of Square: " + str(area))
    case 4:
            radius = float(input("Enter radius: "))
            area = pi * radius ** 2
            print("Area of Circle: " + str(area))
    case 5:
            print("Exiting Area Calculator...")
            exit()                      