#계산기 프로그램



'''함수 선언 구조
def 함수명(매개변수):
        처리로직1
        처리로직2
'''


def plus(a, b):
    res = a + b
    return res

def minus(a, b):     
    res = a - b
    return res

def multiple(a, b):
    res = a*b
    return res
    
def divide(a, b):         #divide(나누기는) 매개변수에 0이 나오면 안됌
    if b == 0:           #옆 구문이 없으면 무한루프가 안됨
        return 0

    res = a/ b
    return res

# '''
# num = 0 
# x = 0  
# y = 0
# val = 0
# '''

# while True:
#     print('''메뉴
# 1. 덧셈
# 2. 뺄셈
# 3. 곱셈
# 4. 나눗셈
# 5. 종료
# 숫자입력: ''')

#     num = int(input())

#     if num ==1:
#         print('덧셈')
#         print('첫번째 값 :', end = ' ')
#         x = int(input())
#         print('두번째 값 :', end = ' ')
#         y = int(input())
#         val = plus(x, y)
#         print(f'{x} + {y} = {val}')
#     elif num ==2:
#         print('뺄셈')
#         print('첫번째 값 :', end = ' ')
#         x = int(input())
#         print('두번째 값 :', end = ' ')
#         y = int(input())
#         val = minus(x, y)
#         print(f'{x} - {y} = {val}')
#     elif num ==3:
#         print('곱셈')
#         print('첫번째 값 :', end = ' ')
#         x = int(input())
#         print('두번째 값 :', end = ' ')
#         y = int(input())
#         val = multiple(x, y)
#         print(f'{x} * {y} = {val}')
#     elif num ==4:
#         print('나눗셈')
#         print('첫번째 값 :', end = ' ')
#         x = int(input())
#         print('두번째 값 :', end = ' ')
#         y = int(input())
#         val = divide(x, y)
#         print(f'{x} / {y} = {val}')
#         break
#     else:
#         continue


def adds(*args):   #prameter, argements
        res = 0
        for i in args:
            res +=i
        return res

def mul_and_div(a,b):
    return (a *b, a / b)   #튜플

def add_and_minus_and_mul_and_div(a, b):
    return (a + b, a- b, a*b, a/b)


print(adds(1, 2, 3, 4,5, 6, 7, 8, 9, 10))
print(adds(1, 2, 3))

(mul_val, div_val) = mul_and_div(16,2)
print(mul_val)
print(div_val)
print(mul_and_div(16, 2))

print(add_and_minus_and_mul_and_div(17,5))




              