from heapq import heappop

S = set()


def visited_or_not(Q, S):
    while Q is None:
        distance, vertices = heappop(Q)
        if vertices not in S:
            S.append(vertices)



