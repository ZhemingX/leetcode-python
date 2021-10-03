'''
Given a list: [2,9,5,1,6], given a target 12
return a boolean indicating if the target could possibly be a sum of list elements
'''


# Solution 1

def dfs(lst, target):
    if target == 0:
        return True
    elif len(lst) == 0:
        return False
    elif lst[0] > target:
        return False
    newList = list(lst)
    for elem in lst:
        newList.remove(elem)
        if target - elem == 0:
            return True
        elif dfs(newList, target - elem):
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


# print(isPossible2([2, 9, 5, 1, 6], 12))
# print(isPossible2([2, 3, 15, 1, 16], 8))
# print(isPossible2([1, 3, 4, 5, 6, 7, 8], 11))
