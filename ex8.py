import matplotlib.pyplot as plt

meses = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

ocupacao = [30, 45, 60, 70, 80, 90]

plt.figure()
plt.fill_between(meses, ocupacao, color= "lightblue", alpha=0.5)
plt.title("Storage Occupancy Over Six Months")
plt.xlabel("Months")
plt.ylabel("Occupancy (%)")
plt.show()