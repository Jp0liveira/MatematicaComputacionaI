import matplotlib.pyplot as plt

# Valores de x, y e z
x = -0.09375
y = -2.0
z = -0.75

# Criação do gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plota o ponto (x, y, z)
ax.scatter(x, y, z, c='r', marker='o')

# Define os rótulos dos eixos
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# Exibe o gráfico
plt.show()
