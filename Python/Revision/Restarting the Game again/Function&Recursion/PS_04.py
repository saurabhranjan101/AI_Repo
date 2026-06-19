#sum of first n numbers
# 5 = 5+4+3+2+1
# 4 = 4+3+2+1
# 3 = 3+2+1
# n = n + (n-1)

def sumrecur(n):
    if(n == 1):
        return 1
    return n + sumrecur(n-1)
print(sumrecur(4))