class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:

        let = []
        sma = []
        Tar = ord(target)
        
        for litter in letters:
            if ord(litter) > Tar:
                let.append(ord(litter))
        
        if let == []:
            return letters[0]

        return chr(min(let))