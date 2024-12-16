import matplotlib.pyplot as plt

meses = ["Jan", "Feb", "Mar", "Apr", "May"]
vendas = [5000, 7000, 6000, 6500, 8000]
plt.figure()
plt.barh(meses, vendas, color="lightcoral")
plt.title("Average Sales Over Five Months")
plt.xlabel("Sales ($)")
plt.ylabel("Months")
plt.show()