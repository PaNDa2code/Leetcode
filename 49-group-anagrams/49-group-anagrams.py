class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        idxs = []
        words = []
        def str_2_list(st):
            out = []
            for char in st:
                out.append(char)
            return ''.join(sorted(out))
        
        for idx in range(len(strs)):
            
            word = strs[idx]
            
            word_l = str_2_list(word)
            
            words.append([word_l,idx])
            
        tmp = {}
        
        for [word,idx] in words:
            
            if word in tmp:
                
                tmp[word].append(idx)
                
            else:
                tmp[word] = [idx]
        
        print(tmp)
        out = []
        for word in tmp:
            l = []
            for idx in tmp[word]:
                l.append(strs[idx])
            out.append(l)
        
        return out
            
            
            
            
            
            
            
            