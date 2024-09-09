import sys
counter = dict()

array = [1,1,2,2,3,4,5]


for i in array:
    if(i in counter.keys()):
        counter[i] += 1
    else:
        counter[i] = 1



print(counter)