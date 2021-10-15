# https://leetcode.com/discuss/int%E2%80%8D%E2%80%8D%E2%80%8D%E2%80%8D%E2%80%8D%E2%80%8D%E2%80%8C%E2%80%8D%E2%80%8C%E2%80%8D%E2%80%8D%E2%80%8D%E2%80%8C%E2%80%8C%E2%80%8C%E2%80%8D%E2%80%8D%E2%80%8D%E2%80%8Derview-experience/1066946
# Task 2

def transform(s):
  stack = []
  i, n = 1, len(s)
  if n < 2:
    return s
  else:
    stack.append(s[0])
  while i < n:
    if stack and (stack[-1], s[i]) in [('a', 'b'), ('b', 'a'), ('c', 'd'), ('d', 'c')]:
      stack.pop()
      i += 1
    else:
      stack.append(s[i])
      i += 1
  return ''.join(stack)

# print(transform("cbacd"))
# print(transform("cababd"))
# print(transform("cababda"))
    
