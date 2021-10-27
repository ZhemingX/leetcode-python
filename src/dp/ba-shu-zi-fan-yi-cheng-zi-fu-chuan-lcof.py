class Solution:
    def translateNum(self, num: int) -> int:
        num_list = list(str(num))
        num_list.append('0')
        num_list.reverse() # [0 8 5 2 2 1]
        len_list = len(num_list)
        res = (len_list)*[0]
        res[0], res[1] = 1, 1
        for i in range(2, len_list):
            if num_list[i] != '0' and int(num_list[i]+num_list[i-1]) <= 25:
                res[i] = res[i-1] + res[i-2]
            else:
                res[i] = res[i-1]
        return res[len_list-1]