import numpy as np

arr=np.array([[1,2,3],[5,4,8],[6,8,3]])
s=np.sum(arr)
print(s)            #sum of all elements in matrix.

sum_row=np.sum(arr,axis=1)
print(sum_row)      #sum of all elements in each row.

sum_row=np.sum(arr,axis=0)
print(sum_row)      #sum of all elements in each column.

median=np.median(arr)
print(median)       #median of all elements.

average=np.average(arr)
print(average)      #average of all elements.