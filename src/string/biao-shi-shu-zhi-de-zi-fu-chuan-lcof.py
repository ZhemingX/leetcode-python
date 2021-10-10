# Solution 1 (常规解法)
class Solution:
    def isNumber(self, s: str) -> bool:
        def isInteger(s:str) -> bool:
            if len(s) and s[0] in ['+', '-']: return s[1:].isdigit()
            return s.isdigit()

        def isFraction(s:str) -> bool:
            if len(s) and s[0] in ['+', '-']:
                s = s[1:]
            if '.' in s:
                list_s = s.split('.')
                if len(list_s) != 2:
                    return False
                list_s = [d for d in list_s if len(d)]
                len_ = len(list_s)
                if len_  == 1 or len_ == 2:
                    return sum([d.isdigit() for d in list_s]) == len_
                return False
            return False 

        # eliminate all spaces in head or tail
        temp_s = s.strip()
        if 'e' in temp_s:
            list_s = temp_s.split('e')
            return len(list_s) == 2 and (isInteger(list_s[0]) or isFraction(list_s[0])) and isInteger(list_s[1]) 
        if 'E' in temp_s:
            list_s = temp_s.split('E')
            return len(list_s) == 2 and (isInteger(list_s[0]) or isFraction(list_s[0])) and isInteger(list_s[1]) 
        return isInteger(temp_s) or isFraction(temp_s)

'''
几个字符串判断函数：
s.digit(): 判断s是否只包含数字
s.isalpha(): 判断s是否只包含字母
s.isalnum(): 判断s是否只包含数字or字母
'''

# Solution 2 (有限状态机)
class Solution:
    def isNumber(self, s: str) -> bool:
        states = [
            { ' ': 0, 's': 1, 'd': 2, '.': 4 }, # 0. start with 'blank'
            { 'd': 2, '.': 4 } ,                # 1. 'sign' before 'e'
            { 'd': 2, '.': 3, 'e': 5, ' ': 8 }, # 2. 'digit' before 'dot'
            { 'd': 3, 'e': 5, ' ': 8 },         # 3. 'digit' after 'dot'
            { 'd': 3 },                         # 4. 'digit' after 'dot' (‘blank’ before 'dot')
            { 's': 6, 'd': 7 },                 # 5. 'e'
            { 'd': 7 },                         # 6. 'sign' after 'e'
            { 'd': 7, ' ': 8 },                 # 7. 'digit' after 'e'
            { ' ': 8 }                          # 8. end with 'blank'
        ]
        p = 0                           # start with state 0
        for c in s:
            if '0' <= c <= '9': t = 'd' # digit
            elif c in "+-": t = 's'     # sign
            elif c in "eE": t = 'e'     # e or E
            elif c in ". ": t = c       # dot, blank
            else: t = '?'               # unknown
            if t not in states[p]: return False
            p = states[p][t]
        return p in (2, 3, 7, 8)