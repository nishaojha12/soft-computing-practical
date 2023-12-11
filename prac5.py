x1=[0,0,1,1]
x2=[0,1,0,1]
w1=1
w2=1
y=[]
for i in range(0,len(x1)):
    xm=x1[i]*w1+x2[i]*w2
    if(xm==1):
        y.append(1)
    else:
        y.append(0)
    
print("x1:",x1)
print("x2:",x2)
print("y:",y)
