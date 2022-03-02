# 반복과 재귀: loop가 필요한 알고리즘을 설계할 때, 반복문(iteration)과 재귀(recursive) 중 하나를 선택할 수 있다.

# 반복문의 기본 동작 과정
'''
1. 초깃값이 존재해야 한다.
2. 종료 조건을 설정하여 반복하는데, for은 횟수 조건(range), while은 상황 조건(if-break)이다.
'''

''' factorial iteration

result = 1
for i in range(1, n + 1):
  result *= i

print(result)
'''


# 재귀 함수의 기본 동작 과정
'''
1. 재귀 함수를 정의해야 한다. (매개변수 설정)
2. 종료 호출의 return과 재귀 호출의 return을 설정해야 한다.

+ 재귀 호출은 스택에서 push로 해석할 수 있고, 종료 호출은 스택에서 pop으로 해석할 수 있다.
따라서 스택 자료구조를 활용해야 하는 상당수의 알고리즘은 재귀 함수를 이용해서 간편하게 구현될 수 있다. ex) DFS
'''

''' factorial recursive

def factorial_recursive(n):
  if n <= 1:
    return 1
  return n * factorial_recursive(n - 1)
'''
