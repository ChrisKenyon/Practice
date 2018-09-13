'''
  Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
    steps at a time. Implement a method to count how many possible ways the child can run up the
    stairs.
'''
def trip_step(n):
    memo = [0,1,2,4]
    for i in range(4,n+1):
        memo.append(memo[i-1] + memo[i-2] + memo[i-3])
    return memo[n]
