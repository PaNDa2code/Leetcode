# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:

#             try:
                
#                 if len(s) == 1:return 1
#                 if len(s) >= 500000:return 0
    
#                 letters = []
    
#                 big_len = 0
    
#                 sts = []
    
#                 for x in range(len(s)+1):
#                     for y in range(len(s)+1):
#                         st = s[x:y]
#                         if st == '':
#                             continue
#                         if len(st) == len(set(st)):
#                             sts.append(st)
#                         else:
#                             continue
#                 lens = []
#                 for i in sts:
#                     lens.append(len(i))
    
#                 return max(lens)

#             except ValueError as Error:
#                 print("Error:", Error)
#                 return 0

# its working but i got time limit 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        char_set = set()
        max_length = 0
        left = 0
        right = 0
        
        while right < len(s):
            if s[right] not in char_set:
                char_set.add(s[right])
                max_length = max(max_length, right - left + 1)
                right += 1
            else:
                char_set.remove(s[left])
                left += 1
        
        return max_length
