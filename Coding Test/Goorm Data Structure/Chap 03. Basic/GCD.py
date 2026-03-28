# Function to calculate the greatest common divisor
def gcd_sub(a, b): # a & b same -> end
    while a != b:
        if a > b:
            a -= b
        elif a < b:
            b -= a
    return a   
        
def gcd_mod(a, b):
    while b != 0:
        a, b = b, a % b
    return a
    
def gcd_rec(a, b):
    if a == b: 
        return a
    else:
        if a >= b: 
            return gcd_rec(a-b, b)
        else:
            return gcd_rec(a, b-a)
     
# get a & b (assumption: a > b)
print("수를 입력하세요")
a, b = map(int,input().split())

# Call gcd_sub, gcd_mod, gcd_rec respectively
# Store the return values in x, y, and z
x = gcd_sub(a, b)
y = gcd_mod(a, b)
z = gcd_rec(a, b)

print(x, y, z)