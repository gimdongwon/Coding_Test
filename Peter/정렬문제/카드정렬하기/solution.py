import heapq

n = 3
cards = [10, 40, 20]


def solution(n, cards):
    heapq.heapify(cards)
    count = 0

    while len(cards) > 1:
        before = heapq.heappop(cards)
        after = heapq.heappop(cards)

        sum_number = before + after

        count += sum_number

        heapq.heappush(cards, sum_number)

    return count


print(solution(n, cards))
