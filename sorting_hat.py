gry,raven,huff,slyth,largest = 0,0,0,0,0
invalid = "Invalid input"

print(type(invalid))
# print(type(gry))

q1 = int(input("Do you like dawn or dusk? Enter 1 for dawn, 2 for dusk: "))
if q1 == 1:
    gry += 1
    raven += 1
elif q1 == 2:
    huff += 2
    slyth += 2
else:
    print(invalid)
q2 = int(input("When I'm dead, I want people to remember me as: 1. The Good 2. The Great 3. The Wise 4. The Bold: "))
if q2 >=1 and q2 <= 4:
    gry += 2
    raven += 2
    huff += 2
    slyth += 2
else :
    print(invalid)    
q3 = int(input("Which kind of instrument most pleases your ear? 1. The violin 2. The trumpet 3. The piano 4. The drum: "))
if q3 >=1 and q3 <= 4:
    gry += 4
    raven += 4
    huff += 4
    slyth += 4
else:
    print(invalid)
            
print(gry,raven,huff,slyth)    
if gry > largest:
    largest = gry
    print("Gryffindor")