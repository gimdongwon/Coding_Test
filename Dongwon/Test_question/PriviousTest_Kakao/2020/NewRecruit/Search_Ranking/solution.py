# 정확성만 통과

def solution(info, querys):
    result = []
    candidates = []
    for item in info:
        temp = item.split(" ")
        candidate = {
            "language": temp[0],
            "job": temp[1],
            "level": temp[2],
            "food": temp[3],
            "score": int(temp[4])
        }
        candidates.append(candidate)
    candidates.sort(key=lambda candidate: (candidate["score"]))
    for query in querys:
        people = 0
        query = query.split(" ")
        for candidate in candidates:
            if candidate["score"] >= int(query[7]):
                if candidate["language"] == query[0] or query[0] == "-":
                    if candidate["job"] == query[2] or query[2] == "-":
                        if candidate["level"] == query[4] or query[4] == "-":
                            if candidate["food"] == query[6] or query[6] == "-":
                                people += 1
        result.append(people)
    return result