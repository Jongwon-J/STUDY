## Problem 7 ##
def fibo(times):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
n = int(input())   

for i in range(n):
    print(fibo(i))

## Problem 6 ##
# def calculate(a, b):
#     return a+2*b

# x, y = map(int, input().split())
# print(calculate(x, y))

## Problem 5 ##
# for i in range(10000, -1, -2):
#   
# print(i)

## Problem 4 ##
# num = int(input("수를 입력하세요 : "))

# if (num % 3 == 0) and (num % 5 ==0): print('FizzBuzz')
# elif num % 3 == 0: print('Fizz')
# elif num % 5 == 0: print('Buzz')

## Problem 3 ##
# x = 1
# x += 1
# print(x*2)

## Problem 2 ##
# import math
# print(math.tan(1))

## Problem 1 ##
# print("Hello, World")