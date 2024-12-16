import matplotlib.pyplot as plt

idades = [22, 25, 28, 30, 32, 35, 40, 45, 50, 52, 30, 28, 25, 22, 40]
plt.figure()
plt.boxplot(idades, patch_artist=True)
plt.title("Age Distribution")
plt.ylabel("Age")
plt.show()