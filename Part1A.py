import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt('life-expectancy-china-1960-2016.txt',delimiter=',',names=['x','y'])
data1960 = data[0][1]
data2016 = data[-1][1]
increase = (data2016 - data1960)/data1960

plt.figure(figsize=(10,5))
plt.plot(data['x'],data['y'])
plt.ylabel('Life Expectancy')
plt.tick_params(axis='x', rotation=70)
plt.title(f'China Life Increasement: {increase:.2%}')
plt.show()

