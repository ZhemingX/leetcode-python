'''
Given a list: [2,9,5,1,6], given a target 12
return a boolean indicating if the target could possibly be a sum of list elements
'''


# Solution 1

def dfs(lst, target):
    if len(lst) == 0:
        return False
    elif lst[0] > target:
        return False
    newList = list(lst)
    for i in range(len(newList)):
        if target - newList[i] == 0:
            return True
        elif dfs(newList[i+1:], target - newList[i]):
            return True
    return False


def isPossible1(calCounts, requiredCals):
    calCounts.sort()
    return dfs(calCounts, requiredCals)

# ---------------------------------- #

# Solution 2


def isPossible2(calCounts, requiredCals):
    def dfs(calCounts, requireCals, start, end):
        if requireCals == 0:
            return True
        if start > end:
            return False
        for i in range(len(calCounts)):
            if i >= start and calCounts[i] <= requireCals:
                if dfs(calCounts, requireCals - calCounts[i], i + 1, end):
                    return True
        return False

    calCounts.sort()
    return dfs(calCounts, requiredCals, 0, len(calCounts) - 1)


# print(isPossible1([2, 9, 5, 1, 6], 12))
# print(isPossible1([2, 3, 15, 1, 16], 8))
# print(isPossible1([1, 3, 4, 5, 6, 7, 8], 11))
