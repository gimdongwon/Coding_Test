# 가사 검색

# 1차 실패.

import re

def solution(words, queries):
    answer = []
    for query in queries:
        query = query.replace("?", ".")
        count = 0
        for word in words:
            print(query, word, re.findall(query, word))
            if re.findall(query, word) and len(query) == len(word):
                count+=1
        answer.append(count)
        
    return answer

from collections import defaultdict # 유사 dict이며 초기값을 객체의 기본값으로 지정가능하다.
from bisect import bisect_left, bisect_right

def count_by_lange(lst, start, end):
    return bisect_right(lst, end) - bisect_left(lst, start)

def solution(words, queries):
    answer = []
    cands = defaultdict(list) 
    reverse_cands = defaultdict(list) 
    
    for word in words:
        cands[len(word)].append(word)
        reverse_cands[len(word)].append(word[::-1])
        
    for cand in cands.values():
        cand.sort()
    for cand in reverse_cands.values():
        cand.sort()
    for query in queries:
        if query[0] == "?":
            lst = reverse_cands[len(query)]
            start, end = query[::-1].replace("?", "a"), query[::-1].replace("?", "z")
        else:
            lst = cands[len(query)]
            start, end = query.replace("?", "a"), query.replace("?", "z")
        answer.append(count_by_lange(lst, start, end))
    return answer
    
        
    return answer