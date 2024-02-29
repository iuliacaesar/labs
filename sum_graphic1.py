import matplotlib.pyplot as plt
import math
y1=[25161.3,105906.3333, 226650.3333, 403112]
y2 = [19.18181818, 49, 74.09090909, 110.2727273]
x=[0]*4
xy=[0]*4
x2=[0]*4
y = [0]*4
for i in range(4):
    x[i]=((i+1)*500)**2 

for i in range(4):
    xy[i] = y2[i]*x[i]
    x2[i] = x[i]**2
    
b = (sum(xy)-sum(x)*sum(y2)/6)/(sum(x2)-sum(x)**2/6)
#sigma_b=((sum(y2)-sum(t)**2/6)/(sum(x2)-sum(p)**2/6)-b**2)**0.5/6**0.5
#a = sum(t)/6 - sum(p)/6*b
#print(b)
for i in range(4):
    y[i] = b*x[i]
plt.plot(x, y, label = 'Средний случай')
plt.scatter(x, y2)
for i in range(4):
    xy[i] = y1[i]*x[i]
b = (sum(xy)-sum(x)*sum(y1)/6)/(sum(x2)-sum(x)**2/6)
for i in range(4):
    y[i] = b*x[i]
#plt.plot(x, y, label = 'Худший случай')
#plt.scatter(x, y1)  
plt.legend()
plt.title('График зависимости t(n) для поиска суммы')
plt.xlabel('n')
plt.ylabel('t')
plt.show()