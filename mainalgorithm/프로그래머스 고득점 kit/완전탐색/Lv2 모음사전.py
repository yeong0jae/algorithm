'''
반복 vs 재귀
바텀업 vs 탑다운
itertools vs recursion
'''

from itertools import product

def solution(word):
    words = [] # 사전
    for i in range(1, 6):
        for c in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            # product는 중복순열을 만들어준다. repeat에 숫자를 넣어주면 그만큼의 길이의 중복순열을 만들어준다.
            # 1~5까지의 길이의 중복순열을 만들어준다.
            words.append(''.join(list(c)))

    words.sort()
    return words.index(word) + 1


# 재귀
# 재귀함수로 단어 사전 list를 만들고 인덱스를 반환하는 방법
def solution(word):
    answer = 0
    word_list = [] # 단어사전
    words = 'AEIOU'
    
    def dfs(cnt, w): 
        if cnt == 5: 
            return
        for i in range(len(words)): # 순회하면서 단어사전에 추가
            word_list.append(w + words[i])
            dfs(cnt+1, w + words[i]) # 추가한 후 그 상태에서 다시 로직 수행. 상태 전이
            
    dfs(0,"")
    
    return word_list.index(word)+1
