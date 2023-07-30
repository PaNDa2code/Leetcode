class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        ans = [0]*len(temperatures)      
        for idx in range(len(temperatures)):
            tmp = temperatures[idx]
            while stack and tmp > stack[-1][0]:
                smaller_idx = stack.pop()[1]
                ans[smaller_idx] = idx - smaller_idx            
            stack.append([tmp,idx])
        return ans