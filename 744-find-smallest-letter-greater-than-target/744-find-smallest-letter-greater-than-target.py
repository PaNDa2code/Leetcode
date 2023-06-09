class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:

        let = []
        sma = []
        Tar = ord(target)
        
        for litter in letters:

            let.append(ord(litter))
        
        for i in let:

            if i > Tar:

                sma.append(i)

        if sma == []:
            return letters[0]

        return chr(min(sma))
