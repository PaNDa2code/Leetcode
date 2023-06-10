class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        
        
        maxCandies = max(candies)
        bools = []
        
        # def test(x):
        #     return x + extraCandies >= maxCandies

        for i in candies:

            bools.append(i + extraCandies >= maxCandies)

        return bools