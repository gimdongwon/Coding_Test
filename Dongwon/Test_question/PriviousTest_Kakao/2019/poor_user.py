from itertools import permutations

def check(users, banned_id):
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False
        for j in range(len(users[i])):
            if banned_id[i][j] == "*":
                continue
            elif banned_id[i][j] != users[i][j]:
                return False
    else:
        return True


def solution(user_id, banned_id):
    user_permutation = list(permutations(user_id, len(banned_id)))
    result = []
    for users in user_permutation:
        if not check(users, banned_id):
            continue
        else:
            users = set(users)
            if users not in result:
                result.append(users)
    return len(result)