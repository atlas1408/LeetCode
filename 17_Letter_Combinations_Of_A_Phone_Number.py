class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        index = 0
        if not digits: return []
        while index < len(digits):
            print(index)
            currI = index
            while currI+1<len(digits) and digits[index:currI+2] in map:
                currI+=1
            currVal = map[digits[index:currI + 1]]
            if index-1>=0:
                newNos = digits[0:currI + 1]
                temp = []
                for outer in map[digits[0:index]]:
                    for inner in currVal:
                        temp.append(outer+inner)
                map[newNos] = temp
            index = currI+1
        return map[digits]