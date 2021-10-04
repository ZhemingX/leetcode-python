from typing import List


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        import copy
        table_dict, food_dict = dict(), dict()
        # create food dict
        for order in orders:
            if order[2] not in food_dict.keys():
                food_dict[order[2]] = 0
        # create table fict
        for order in orders:
            tid = int(order[1])
            if tid not in table_dict.keys():
                table_dict[tid] = copy.deepcopy(food_dict)
            table_dict[tid][order[2]] += 1
        # create result
        res = [["Table"] + sorted(list(food_dict.keys()))]
        for tid in sorted(table_dict.keys()):
            row = [str(tid)]
            for k in sorted(table_dict[tid].keys()):
                row.append(str(table_dict[tid][k]))
            res.append(row)
        return res
