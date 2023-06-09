class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:

        # let = []
        # Tar = ord(target)
        
        # for litter in letters:
        #     if ord(litter) > Tar:
        #         let.append(ord(litter))
        
        # if let == []:
        #     return letters[0]

        # return chr(min(let))

        # binary search
        

        right = len(letters) - 1
        left = 0
        t = ord(target)
        
        while left <= right:

            mid = (right + left) // 2
        
            if ord(letters[mid]) <= t:

                left = mid + 1

            else:

                right = mid - 1
        

        if left ==len(letters):
            return letters[0]
        else :
            return letters[left]