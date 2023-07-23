#constraint sequence..

n = int(input())
for i in range(n):
    p = int(input())
    nums = list(map(int, input().split()))
    ans = []
    for j in range(p):
        if (nums[j] >= 0) and (nums[j] <= 10**9):
            ans.append("Yes")
        else:
            ans.append("No")

    if ("No" in ans):
        print("No")
    else:
        print("Yes")
