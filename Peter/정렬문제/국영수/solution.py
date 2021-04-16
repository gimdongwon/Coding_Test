n = 12
list = [
    ("JunKyu", 50, 60, 100),
    ("Sangkeun", 80, 60, 50),
    ("Sunyoung", 80, 70, 100),
    ("Soong", 50, 60, 90),
    ("Heabin", 50, 60, 100),
    ("Kangsoo", 60, 80, 100),
    ("Donghyuk", 80, 60, 100),
    ("Sei", 70, 70, 70),
    ("Wonseob", 70, 70, 90),
    ("Snaghyun", 70, 70, 80),
    ("nsj", 80, 80, 80),
    ("Taewhan", 50, 60, 90),
]


def solution(n, list):
    sorted_list = sorted(list, key=lambda x: (-x[1], x[2], -x[3], x[0]))
    print(sorted_list)


solution(n, list)
