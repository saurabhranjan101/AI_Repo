'''
num = [2,7,11,15]
target = 9
output = [0,1] -> Index of sum of two numbers which is equal to 9(Basically sum of 2 & 7 9. 2 is at 0th position & 7 is at 1st position)
'''
# num = [2,7,11,15]
# target = 9
num = [3,2,4]
target = 6
for i in range(0, len(num)): #0,1,2
    for j in range(i+1, len(num)):#1,2
        if((num[i] + num[j]) == target):
            print([i,j])