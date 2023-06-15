import collections

class Solution:
    def maxLevelSum(self, root) -> int:
        max_sum, output, level = float('-inf'),0,0

        q = collections.deque()

        q.append(root)

        while q:
            level += 1
            sum_now = 0

            for i in range(len(q)):

                no = q.popleft()

                sum_now += no.val

                if no.left:
                    q.append(no.left)
                if no.right:
                    q.append(no.right)

            if max_sum < sum_now:
                max_sum ,output= sum_now,level

        return output