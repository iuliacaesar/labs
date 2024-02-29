import matplotlib.pyplot as plt
import math
y1=[2537.8,2615.5,2664.1,2735.4,2768.4,2800.4,2866.5,2823.3,2897.6,2846.3,2882.1,2886.4,2893.9,2895.4,2919.3,2967.3,2968.9,2986.7,3036.8,3038.9]
y2 = [2298.8,2295.9,2419.8,2357,2370.6,2540.7,2521.8,2545.1,2584.1,2668.5,2684.5,2628.1,2673.3,2728.8,2628.8,2617.8,2734.4,2888.4,2654.3,2717.7]
x=[0]*20
xy=[0]*20
x2=[0]*20
y = [0]*20
for i in range(20):
    x[i]=math.log2((i+1)*50000)   

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
for i in range(6):
    xy[i] = y1[i]*x[i]
b = (sum(xy)-sum(x)*sum(y1)/6)/(sum(x2)-sum(x)**2/6)
for i in range(20):
    y[i] = b*x[i]
plt.plot(x, y, label = 'Худший случай')
plt.scatter(x, y1)  
plt.legend()
plt.title('График зависимости t(n) для бинарного поиска')
plt.xlabel('n')
plt.ylabel('t')
plt.show()