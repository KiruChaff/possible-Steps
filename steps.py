import sys;sys.setrecursionlimit(2000)

## Amount of steps
n=4

## RETURNS THE NUMBER OF WAYS GO UP N-STAIRS WITH EITHER ONE OR TWO STEPS
def num_steps(n, memo={}):
    if n==0: ## NUMBER OF STEPS WAS ADEQUATE
        return 1
    elif n<0: ## OVERSHOT THE GOAL
        return 0
    if n in memo: ## MEMOIZATION
        return memo[n]
    ## FOR EACH STATE TRY BOTH 1 AND 2 STEPS
    num = num_steps(n-1, memo)+num_steps(n-2, memo)
    memo[n]=num
    return num
## RETURNS THE NUMBER OF WAYS TO GO UP N-STAIRS WITH A SET OF STEPS--PRINCIPLE IS THE SAME
def num_steps_nums(n, nums, memo={}, num=0):
    if n==0:
        return 1
    elif n<0:
        return 0
    if n in memo:
        return memo[n]
    for i in range(len(nums)): ## ITERATE THROUGH THE SET OF STEPS TO TAKE
        num += num_steps_nums(n-nums[i], nums, memo)
        memo[n]=num
    return num

##----------------------------------------------------------##

print(num_steps(n, memo))

nums=[1, 3, 5]
print(num_steps_nums(n, nums, memo))

## output:
## >>>5
## >>>3
