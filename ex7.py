import matplotlib.pyplot as plt

dias = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

cidade1 = [22, 24, 25, 23, 20, 19, 18]
cidade2 = [18, 20, 21, 22, 19, 17, 16]

plt.figure()
plt.plot(dias, cidade1, marker='o', label="City 1")
plt.plot(dias, cidade2, marker='s', label="City 2")
plt.title("Temperature Variation in Two Cities")
plt.xlabel("Days")
plt.ylabel("Temperature(°C)")
plt.legend()
plt.show() 