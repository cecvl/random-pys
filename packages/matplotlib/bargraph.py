import matplotlib.pyplot as plt
import numpy as np

# faculties
x = np.array(["IT","MEDIA","BUSINESS", "EDUCATION"])
y = np.array([200, 300, 235, 242])

#plot bar() fxn
plt.bar(x,y)
plt.plot()
plt.xlabel("FACULTY")
plt.ylabel("NUMBER OF STUDENTS")
plt.title("2023 INTAKE")
plt.show()