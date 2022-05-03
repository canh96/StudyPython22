#구구단 프로그램

print('---구구단 프로그램---')


for x in range(2, 10):
    for y in range(1, 10):
        print(f'{x} x {y} = {x*y:2d}' ,end =',')
    print() #단 마다 줄 맞추기 위해서


for x in range(1,6):
    for y in range(x, 5):
        print('',end='')

    for y in range(1, x):
        print('*', end = '')

    #파이썬은 객체 지향 프로그래밍 언어입니다. 객체 지향 프로그램 언어에서는 이 함수를 메서드라고 부릅니다. 
    # 하지만, 파이썬은 특이하게 함수라고 하고 있는데요. 함수 Function 과 메서드 Method는 전혀 차이가 없습니다. 
    # 앞서 프로그래밍을 설명할 때 같은 의미의 다른 용어가 있다고 언급했었습니다.

