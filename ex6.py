import matplotlib.pyplot as plt

alturas = [1.60, 1.75, 1.80, 1.65, 1.70]
pesos = [60, 70, 80, 65, 75]
plt.figure()
plt.scatter(alturas, pesos, color="purple")
plt.title("Height vs Weight")
plt.xlabel("Height (m)")
plt.ylabel("Weight (kg)")
plt.show()