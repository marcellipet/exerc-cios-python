import matplotlib.pyplot as plt
 
transportes = ["Carro", "Bicicleta", "Transporte", "A Pé"]
percentuais = [40, 20, 30, 10]
plt.figure()
plt.pie(percentuais, labels=transportes, autopct='%1.1f%%', startangle=140)
plt.title("Modes of Transportation in a City")
plt.show()