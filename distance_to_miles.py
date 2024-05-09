def convert(km):
    miles = km / 1.609
    print("Distance in miles = " + str(miles))

input = float(input("Enter distance in kilometers: "))
convert(input)