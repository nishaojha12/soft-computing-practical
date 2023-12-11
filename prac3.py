x=[0.2, 0.6]
w=[0.3, 0.7]
y=0
b=0.45
for i in range(0,len(x)):
    y=y+x[i]*w[i]
y=y+b
print("x:",x)
print("w:",w)
print("y:",round(y,3))
