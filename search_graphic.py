import matplotlib.pyplot as plt
y1=[4458.333333, 8776, 13148, 17501.66667, 22199.33333, 27947, 32788.33333,35681, 39374.33333, 45856, 49558.33333, 52715,56627,60664.66667,65319.33333, 72776.66667, 76327.33333, 78343,85794.66667,87071]
y2 = [1648.17, 4659.17, 6246.33, 6549.50, 9280.50, 10065.83, 13191.17, 16550.50, 17901.83, 20129.00,11190.50, 37357.50, 28233.50, 28880.67,38776.67, 38807.00, 35986.83, 44580.17, 43759.33, 35769.83]
x = [0]*20
xy=[0]*20
x2=[0]*20
y = [0]*20
for i in range(20):
    x[i]=(i+1)*50000

for i in range(20):
    xy[i] = y2[i]*x[i]
    x2[i] = x[i]**2
    
b = (sum(xy)-sum(x)*sum(y2)/6)/(sum(x2)-sum(x)**2/6)
#sigma_b=((sum(y2)-sum(t)**2/6)/(sum(x2)-sum(p)**2/6)-b**2)**0.5/6**0.5
#a = sum(t)/6 - sum(p)/6*b
#print(b)
for i in range(20):
    y[i] = b*x[i]
plt.plot(x, y, label = 'Средний случай')
plt.scatter(x, y2)
for i in range(20):
    xy[i] = y1[i]*x[i]
    x2[i] = x[i]**2
b = (sum(xy)-sum(x)*sum(y1)/6)/(sum(x2)-sum(x)**2/6)
for i in range(20):
    y[i] = b*x[i]
plt.plot(x, y, label = 'Худший случай')
plt.scatter(x, y1)
plt.legend()
plt.title('График зависимости t(n) для линейного поиска')
plt.xlabel('n')
plt.ylabel('t')
plt.show()