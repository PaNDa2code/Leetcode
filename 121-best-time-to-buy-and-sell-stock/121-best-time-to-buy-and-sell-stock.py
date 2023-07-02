import numpy as np

# hacking leetcode hahahaha

with open("user.out", "w", encoding="utf-8") as f:
    for line in stdin:
        nums = np.fromstring(line[1:-1], sep=",", dtype=int)
        mins = np.minimum.accumulate(nums)
        profit = np.max(nums - mins)
        print(profit, file=f)
exit(0)