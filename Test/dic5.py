dict1={"a":1,"b":2,"c":3}
dict2={"k":4,"l":5,"b":7,"a":7,"c":10}



dict3 = {}
  
  #YOUR CODE GOES HERE
d1=dict1.keys()
d2=dict2.keys()
dc1=set(d1)
dc2=set(d2)
i=dc1.intersection(dc2)
h=list(i)
if len(h)==0:
    print(dict3)
else:
    for t in range(len(h)):
        j=h[t]
        dcv1=dict1[str(j)]
        dcv2=dict2[str(j)]
        s=dcv1+dcv2
        dict3[str(j)]=s
    print(dict3)
