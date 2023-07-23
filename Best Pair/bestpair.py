##Best Pairs by Hackerrank
##
##Given an array of N integers, find max(LCM(ai, aj)) possible in the array such that 1 <= i < j <= N.
##
##In simple words, find max LCM possible of two values of the array, that are at distinct positions in the array. Print the
##max LCM possible.


def lcm_finder(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater = greater + 1

    return lcm


n = int(input())
nums = list(map(int, input().split()))
new = []
for i in range(n):
    for j in range(n):
        if j > i:
            new.append(lcm_finder(nums[i], nums[j]))

print(new)
print(max(new))
