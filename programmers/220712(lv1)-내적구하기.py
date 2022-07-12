a1 = [1, 2, 3, 4]
b1 = [-3, -1, 0, 2]
r1 = 3

a2 = [-1, 0, 1]
b2 = [1, 0, -1]
r2 = -2


def solution(a, b):
    answer = 0
    for i, j in zip(a, b):
        answer += i * j
    return answer

print(f"{solution(a1, b1)} -> {r1}")
print(f"{solution(a2, b2)} -> {r2}")