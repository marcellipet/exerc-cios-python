import matplotlib.pyplot as plt
trimestres = ["Q1", "Q2", "Q3"]
produto1 = [3000, 4000, 5000]
produto2 = [2000, 3000, 4000]

plt.bar(trimestres, produto2, bottom=produto1, color="lightcoral", label="Product 2")
plt.title("Sales of Two Products Over Three Quarters")
plt.xlabel("Quarters")
plt.ylabel("Sales ($)")
plt.legend()
plt.show()