nums1 = [1, 2, 3, 4]
r1 = 1

nums2 = [1, 2, 7, 6, 4]
r2 = 4

# 소수인지 아닌지를 판별하는 함수 생성
def prime_num(sum_noc):
    for i in range(2, sum_noc//2+1):
        if sum_noc % i == 0:
            return False
    return True


def solution(nums):
    from itertools import combinations # -> 경우의 수를 계산할 module import
    noc = list(combinations(nums, 3)) # -> noc에 3개로 만들 수 있는 Number of Cases를 담는다

    answer = 0 # -> 소수일 경우 count 할 변수 선언
    for i in noc:
        if prime_num(sum(i)): # -> 전체 sum이 소수일 경우
            answer += 1

    return answer

print(f"{solution(nums1)} -> {r1}")
print(f"{solution(nums2)} -> {r2}")