# 브루트포스 알고리즘: 완전 탐색

# 완전 탐색의 기본 동작 과정

1. 처음부터 끝까지 모두 확인(탐색)한다. (반복과 1 ~ 3차원 선형탐색, 재귀와 깊이 조건, 최대최소 선형탐색, 좌표 이동경로 정의 후 탐색 or 시뮬레이션, 비트마스크)
2. 불필요한 탐색을 줄일 가능성이 있는지 알아본다. (탐색의 범위축소 ex) += 1 대신 += k, 백트래킹)
+ 예시(최소한 처음중간끝이 나뉘도록)를 가지고 먼저 구현한 뒤 일반화 해나가기


# 시간 완전탐색

h = int(input()) # 86400개의 경우의 수. 3중 반복문 이용
cnt = 0
for i in range(n + 1):
	for j in range(60):
		for k in range(60):
			if '3' in str(i) + str(j) + str(k):
				cnt += 1
print(cnt)



# 3085 사탕게임

import sys
input = sys.stdin.readline

def check(arr): # '연속되는 숫자의 최댓값 확인하는 코드' 따로 떼서 함수로 만들기. 이렇게 쪼개서 생각할 수 있어야 함. 그리고 사실상 완전탐색 형태는 2차원 선형탐색.
    n = len(arr)
    max = 1

    for i in range(n):
        cnt = 1
        for j in range(1, n): # 가로 전체 탐색
            if arr[i][j] == arr[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt > max: # 매번 최댓값 갱신
                max = cnt
        cnt = 1
        for j in range(1, n): # 세로 전체 탐색
            if arr[j][i] == arr[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            if cnt > max:
                max = cnt
    return max


n = int(input())
arr = [list(input()) for _ in range(n)] # 이중 리스트로 바로 입력받기
answer = 0

for i in range(n):
    for j in range(n):
        if j + 1 < n:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            
            temp = check(arr)

            if temp > answer:
                answer = temp
               
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

        if i + 1 < n:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            
            temp = check(arr)

            if temp > answer:
                answer = temp
            
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            
print(answer)



# 1476 날짜 계산

a, b, c = map(int, input().split())
y = 1 # 연도 자체(답)를 1부터 선형 탐색함. 답이 y라고 하면 맞나?를 계속 확인

while True:
    if (y - a) % 15 == 0 and (y - b) % 28 == 0 and (y - c) % 19 == 0:
        print(y)
        break
    y += 1



# 6064 카잉달력

T = int(input())

for _ in range(T):
	M, N, x, y = map(int, input().split())
	year = x
	while 1:
		if year % N == y % N: # 연도 year를 1부터 탐색할 필요 없이, year += M으로 탐색해도 된다.
			print(year)
			break
		year += M
		if year > M * N:
			print(-1)
			break



# 1107 리모컨

import sys
input = sys.stdin.readline
target = int(input())
n = int(input())
broken = list(map(int, input().split()))

min_count = abs(100 - target) # 현재 채널에서 + 혹은 -만 사용하여 이동하는 경우. 최댓값을 초기값으로 설정.

for nums in range(1000001): # 고장난 채널을 제외한 모든 채널 탐색
    nums = str(nums)
    
    for j in range(len(nums)):
        if int(nums[j]) in broken:
            break
        elif j == len(nums) - 1:
            min_count = min(min_count, abs(int(nums) - target) + len(nums)) # 고장난 숫자 없이 마지막 자리까지 왔다면 min_count 비교 후 업데이트

print(min_count)



# 나이트 움직이기

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1 # 문자을 숫자로 대응. 아스키코드 이용

steps = [(-2, -1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)] # 나이트 이동 경로 8가지 정의

cnt = 0
for step in steps:
    next_row = row + step[0] # 열 이동
    next_column = column + step[1] # 행 이동
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <=8:
        cnt += 1
print(cnt)



# 유닛의 자동 이동

n, m = map(int, input().split())

x, y, direction = map(int, input().split())

d = [[0] * m for _ in range(n)]
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0] # 북, 동, 남, 서 방향 정의
dy = [0, 1, 0, -1]

def turn_left(): # 왼쪽으로 회전 함수
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue #
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)



# 14500 테트로미노

import sys
input = sys.stdin.readline
n, m = map(int, input().split())

s = []
tetromino = [[[0, 1], [0, 2], [0, 3]], [[1, 0], [2, 0], [3, 0]], # 테트로미노를 이동 경로라고 생각했을 때 좌표 이동 경로 정의
[[0, 1], [1, 0], [1, 1]], [[1, 0], [2, 0], [2, 1]],
[[1, 0], [2, 0], [2, -1]], [[0, 1], [0, 2], [1, 0]],
[[0, 1], [0, 2], [1, 2]], [[0, 1], [1, 1], [2, 1]],
[[0, 1], [1, 0], [2, 0]], [[0, 1], [0, 2], [-1, 2]],
[[1, 0], [1, 1], [1, 2]], [[1, 0], [1, 1], [2, 1]],
[[1, 0], [1, -1], [2, -1]], [[0, 1], [-1, 1], [-1, 2]],
[[0, 1], [1, 1], [1, 2]], [[0, 1], [0, 2], [1, 1]],
[[1, 0], [1, 1], [2, 0]], [[1, 0], [1, -1], [2, 0]],
[[0, 1], [0, 2], [-1, 1]]

for i in range(n):
    s.append(list(map(int, input().split())))
result = 0
for i in range(n): # 좌표 완전 탐색 하면서 이동 경로 탐색
    for j in range(m):
        for k in tetromino:
            try:
                sum_n = s[i][j] + s[i + k[0][0]][j + k[0][1]] + s[i + k[1][0]][j + k[1][1]] + s[i + k[2][0]][j + k[2][1]]
            except:
                sum_n = 0
            result = max(result, sum_n)
print(result)



# n과 m (3) 완전 탐색의 재귀적 구현 recursive bruteforce

n, m = list(map(int, input().split()))
 
s = []

def rec(): # bruteforce 인데 반복으로 안되서 재귀로 접근.
    if len(s) == m: # 종료 조건
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, n + 1): # 완전 탐색
            s.append(i)
            rec() # 재귀 호출
            s.pop()
rec()



# 9095 1,2,3 더하기 - 완전 탐색의 재귀적 구현

n = int(input())

def sums(n):
    if n == 1:
        return(1)
    elif n == 2:
        return(2)
    elif n == 3:
        return(4)
    else:
        return sums(n-1) + sums(n-2) + sums(n-3)
        
for i in range(n):
    a = int(input())
    print(sums(a))



# 14501 퇴사

import sys
input = sys.stdin.readline

n = int(input())
s = []
for i in range(n):
    s.append(list(map(int, input().split())))

M = 0

def go(day, total):
    global M
    if day == n:  # n에 알맞게 도착했을 때, 정답이 될 수 있다. # 깊이에 따른 종료조건.
        M = max(M, total)
        return
    if day > n:  # n을 초과한다면 범위 안에 일을 못끝내므로, 정답이 될 수 없다. # 깊이에 따른 종료조건
        return
    go(day + 1, total) # 이번 day는 일을 하지 않고 그냥 넘어간다!
    go(day + s[day][0], total + s[day][1]) # 이번 day일을 처리한다, 기간도 점프한다! # 모든 경우 재귀 호출해서 M값 최신화하기 (최대최소 bf + 재귀적 구현)

go(0, 0) # day는 0, total도 0부터 시작.
print(ans)



# 10819 차이를 최대로 - 최대최소 bf

import sys
input = sys.stdin.readline

def np(pl): # next permutation 알고리즘 (재귀로 구현하는 순열보다 빠름.)
	x = 0
	for i in range(len(pl) - 1, 0, -1):
		if pl[i - 1] < pl[i]:
			x = i - 1
			break
	for i in range(n - 1, 0, -1):
		if pl[x] < pl[i]:
			pl[x], pl[i] = pl[i], pl[x]
			pl = pl[:x + 1] + sorted(pl[x + 1:])
			return pl
	return [-1]


n = int(input())
a = list(map(int, input().split()))

a.sort()

ans = 0 # 최대값 저장, 최신화

s = 0
for j in range(len(a) - 1):
    s += abs(a[j] - a[j+1])
if s > ans:
    ans = s

arr = a

while 1:
	arr = np(arr)
	if arr == [-1]:
		break
	s = 0
	
	for j in range(len(arr) - 1):
		s += abs(arr[j] - arr[j+1])
	if s > ans:
		ans = s
print(ans)



# 14319 종이조각 - 비트마스킹

import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

paper = []
for _ in range(n):
	paper.append(list(map(int, input().rstrip())))

ans = []

for i range(1 << n*m): # 2의 n * m승 가지의 경우의 수 모두 확인
	total = 0
	for row in range(n):
		rowsum = 0
		for col in range(m):
			idx = row * m + col # idx는 주어진 배열의 번호
			if i & (1 << idx) != 0: # 대충 알겠는데, 1. 이렇게 확인하면 모든 경우의 수가 확인되는가? 2. 이 풀이를 떠올릴만한 개연성이 있나?
				rowsum = rowsum * 10 + paper[row][col]
			else:
				total += rowsum
				rowsum = 0
		total += rowsum
	
	for col in range(m):
		colsum = 0
		for row in range(n):
			idx = row * m + col
			if i & (1 << idx) == 0:
				colsum = colsum * 10 + paper[row][col]
			else:
				total += colsum
				colsum = 0
		total += colsum
	ans.append(total)

print(max(ans))


# 16035 배열 돌리기3 - arr을 바로 바꾸기보단 함수 쓰고 tmp에 담아서 arr에 넣어 바꾸기

import sys
input=sys.stdin.readline

def cal1(arr):
    temp=[[0]*m for _ in range(n)]
    for i in range(n):
        temp[i]=arr[n-i-1]
    return temp
def cal2(arr):
    temp=[[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            temp[i][j]=arr[i][m-j-1]
    return temp
def cal3(arr,n,m):
    temp=[[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            temp[i][j]=arr[n-j-1][i]
    return temp
def cal4(arr,n,m):
    temp=[[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            temp[i][j]=arr[j][m-i-1]
    return temp
def cal5(arr):
    temp=[[0]*m for _ in range(n)]
    for i in range(n//2):
        for j in range(m//2):
            temp[i][j+m//2]=arr[i][j]
    for i in range(n//2):
        for j in range(m//2,m):
            temp[i+n//2][j]=arr[i][j]
    for i in range(n//2,n):
        for j in range(m//2,m):
            temp[i][j-m//2]=arr[i][j]
    for i in range(n//2,n):
        for j in range(m//2):
            temp[i-n//2][j]=arr[i][j]
    return temp
def cal6(arr):
    temp=[[0]*m for _ in range(n)]
    for i in range(n//2):
        for j in range(m//2):
            temp[i+n//2][j]=arr[i][j]
    for i in range(n//2,n):
        for j in range(m//2):
            temp[i][j+m//2]=arr[i][j]
    for i in range(n//2,n):
        for j in range(m//2,m):
            temp[i-n//2][j]=arr[i][j]
    for i in range(n//2):
        for j in range(m//2,m):
            temp[i][j-m//2]=arr[i][j]
    return temp

n,m,r=map(int, input().split())
arr=[list(map(int, input().split())) for _ in range(n)]
cals=list(map(int, input().split()))

for cal in cals:
    if cal==1:
        arr=cal1(arr)
    elif cal==2:
        arr=cal2(arr)
    elif cal==3:
        arr=cal3(arr,n,m)
        n,m=m,n
    elif cal==4:
        arr=cal4(arr,n,m)
        n,m=m,n
    elif cal==5:
        arr=cal5(arr)
    else:
        arr=cal6(arr)

for i in arr:
    print(*i)

	     
# 16926 배열돌리기3 - 복잡한 bf는 예시를 이용해 일반화를 시작하기

import sys
input = sys.stdin.readline

n,m,r = map(int,input().split())

data = [list(map(int,input().split())) for _ in range(n)]

for _ in range(r):
    for i in range(min(n, m) // 2):
    	# x, y 는 돌려지는 배열중 가장 첫번째 배열 인덱스
        x, y = i, i
        temp = data[x][y]
                            # 안쪽까지 계속 고려해야하기 때문에 n-i랑 m-i까지로 범위설정
        for j in range(i + 1, n - i):  #좌
            x = j
            prev_value = data[x][y]
            data[x][y] = temp
            temp = prev_value

        for j in range(i + 1, m - i):  #하
            y = j
            prev_value = data[x][y]
            data[x][y] = temp
            temp = prev_value

        for j in range(i + 1, n - i):  #우
            x = n - j - 1
            prev_value = data[x][y]
            data[x][y] = temp
            temp = prev_value

        for j in range(i + 1, m - i):  #상
            y = m - j -1
            prev_value = data[x][y]
            data[x][y] = temp
            temp = prev_value

for i in range(n):
    for j in range(m):
        print(data[i][j], end=' ')
    print()


# 16927 배열돌리기2 - 제자리에 오는 걸 고려해서 r을 나눌생각, 더 나아가서 고리마다 다른 제자리 값을 적용해주는 것.

import math

N, M, R = map(int, input().split())

NUMBERS = [list(map(int, input().split())) for _ in range(N)]

turns = []
for k in range(min(N, M)//2):
    turns.append(2*((N-(2*k))+(M-(2*k)))-4)


for k in range(min(N,M)//2):
    for r in range(R%turns[k]):
        temp = NUMBERS[k][k]
        for i in range(1+k, M-k):
            NUMBERS[k][i-1] = NUMBERS[k][i]

        for i in range(1+k, N-k):
            NUMBERS[i-1][M-1-k] = NUMBERS[i][M-1-k]

        for i in range(1+k, M-k):
            NUMBERS[N-1-k][M-i]=NUMBERS[N-1-k][M-1-i]

        for i in range(1+k, N-k):
            NUMBERS[N-i][k] = NUMBERS[N-1-i][k]

        NUMBERS[1+k][k] = temp

for n in NUMBERS:
    print(" ".join(map(str,n)))
'''
