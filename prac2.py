x=[0.3, 0.5, 0.6]
w=[0.2, 0.1,-0.3]
y=0
for i in range(0,len(x)):
    y=y+x[i]*w[i]

print("x:",x)
print("w:",w)
print("y:",round(y,3))
