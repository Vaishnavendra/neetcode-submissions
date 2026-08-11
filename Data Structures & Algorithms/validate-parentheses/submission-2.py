class Solution:
    def isValid(self, s: str) -> bool:
        dic={")":"(","}":"{","]":"["}
        stack=[]
        for w in s:
            if w in dic:
                if (stack and stack[-1] == dic[w]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(w)
        return True if not stack else False
            
        