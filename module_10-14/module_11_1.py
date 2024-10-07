import matplotlib.pyplot as plt
import numpy as np

# Данные
x = [1, 2, 3, 4, 5]
y = [1, 20, 13, 20, 1]

# plt.plot(x, y)
#
# plt.title('М')
# plt.xlabel('X')
# plt.ylabel('Y')

# Построение круговой диаграммы
plt.title('состав воздуха')
labels = ['N2', 'O2', 'Ar', 'CO2']
sizes = [78, 21, 0.9, 0.1]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

plt.axis('equal')

plt.show()


# Построение примерной гистограммы пиков облученного образца KI
x_peaks = [20, 37, 45, 50, 60, 65, 70, 80]

heights = [80000, 25000, 30000, 20000, 15000, 10000, 5000, 300]

data = []
for peak, height in zip(x_peaks, heights):
    data.append(np.random.normal(peak, 1, height))

data = np.concatenate(data)

plt.hist(data, bins=1000, color='blue')
plt.title('попытка изобразить дифрактограмму')
plt.xlabel('угол дифракции')
plt.ylabel('интенсивность')
plt.show()
