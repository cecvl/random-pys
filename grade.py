grades = [50,50,66,68,50]
sum  = 0
for i in grades:
    sum += i
average = sum/5
print(average)
if average < 55:
    print("Fail")
else:
    print("Pass")