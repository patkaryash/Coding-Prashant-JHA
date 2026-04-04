#WAP to rearrange positive and negative numbers
s = [-1,2,-3,4,5,-6]
p = []
n = []
for i in s:
    if i>0:
     p.append(i)
    else:
     n.append(i)
print(n)
print(p)
for i in range(len(p)):
    s[i*2]=p[i]
    s[i*2+1]=n[i]
print(s)
  
        
        