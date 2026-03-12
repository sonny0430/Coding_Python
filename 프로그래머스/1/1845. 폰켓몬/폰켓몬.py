def solution(nums):
    no_dp = len(set(nums))
    answer = no_dp if no_dp <= len(nums)/2 else len(nums)/2
    return answer