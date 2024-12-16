import matplotlib.pyplot as plt

temperaturas = [22, 21, 23, 25, 20, 19, 21]
dias = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
plt.figure()
plt.plot(dias, temperaturas, marker='o')
plt.title("Temperature Variation Over a Week")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.show()

