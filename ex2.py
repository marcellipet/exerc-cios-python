import matplotlib.pyplot as plt

cursos = ["Engenharia", "Medicina", "Direito", "Economia"]
alunos = [45, 30, 20, 25]
plt.figure()
plt.bar(cursos, alunos, color="skyblue")
plt.title("Number of Students in Different Courses ")
plt.xlabel("Courses")
plt.ylabel("Number of Students")
plt.show()