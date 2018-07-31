n=10
memo={}
import sys;sys.setrecursionlimit(2000)
def num_steps(n, memo):
    if n==0:
        return 1
    elif n<0:
        return 0
    if n in memo:
        return memo[n]
    num =num_steps(n-1, memo)+num_steps(n-2, memo)
    memo[n]=num
    return num
# print(num_steps(n, memo))

memo={}
nums=[1, 3, 5]
def num_steps_nums(n, nums, memo, num=0):
    if n==0:
        return 1
    elif n<0:
        return 0
    if n in memo:
        return memo[n]
    for i in range(len(nums)):
        num += num_steps_nums(n-nums[i], nums, memo)
        memo[n]=num
    return num
print(num_steps_nums(n, nums, memo))
