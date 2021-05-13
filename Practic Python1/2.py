import math

data = []

def sum(value):

    result = 0

    while value!=0:
        result += value % 10
        value //= 10
    return result

for i in range(0,1000):
    if  i % 2 != 0:
       data.append(math.pow(i,3))
sum_num=0
for i in range(len(data)):
    data[i] = data[i]
    if (sum(data[i])%7==0):
        sum_num+=data[i]
print(int(sum_num), "первое задание")
sum_num=0
for i in range(len(data)):
    if (sum(data[i]+17)%7==0):
        sum_num+=data[i]
print(int(sum_num), "второе задание ")