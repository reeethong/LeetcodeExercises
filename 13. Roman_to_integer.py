class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {'M': 1000, 'D':500, 'C': 100, 'L':50, 'X':10,'V':5,'I':1} #use hashmap rather than if-elses
        result = 0
        for i in range(len(s)):
            if i != len(s)-1:
                if hashmap[s[i]] < hashmap[s[i+1]]:
                    result -= hashmap[s[i]]
                    continue
            result += hashmap[s[i]]
        return result
