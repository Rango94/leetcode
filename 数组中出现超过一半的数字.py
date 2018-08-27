# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        dic = {}
        for i in numbers:
            if dic == {}:
                try:
                    dic[i] += 1
                except:
                    dic[i] = 1
            else:
                try:
                    dic[i] += 1
                except:
                    flag = False
                    for key in dic:
                        dic[key] -= 1
                        if dic[key] <= 0:
                            flag = True
                    if flag:
                        dic.pop(key)
                        dic[i] = 1
        for key in dic:
            n = 0
            for i in numbers:
                if i == key:
                    n += 1
            if n > len(numbers) / 2:
                return key
            else:
                return 0
        return 0

        # write code here
a=[1,2,3,2,2,2,5,4,2]
s=Solution()
s.MoreThanHalfNum_Solution()