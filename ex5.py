import matplotlib.pyplot as plt

notas = [7, 8, 5, 9, 10, 6, 8, 7, 9, 5, 10, 8, 6, 7, 9]
plt.figure()
plt.hist(notas, bins=5, color="lightgreen", edgecolor="black")
plt.title("Distribution of Grades")
plt.xlabel("Grades")
plt.ylabel("Frequency")
plt.show()

