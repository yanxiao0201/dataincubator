
class Solution:
    def __init__(self,N):
        self.res = 0
        self.count = 0
        self.number = N
    def permutation(self):
        list_num = range(1,self.number + 1)

        self.find_perm(0, list_num)

        return float(self.res)/self.count

    def find_perm(self,start, list_num):
        if start == len(list_num)-1:
            self.res += self.calculate(list_num)
            self.count += 1
            return
        for i in xrange(start, len(list_num)):
            list_num[start],list_num[i] = list_num[i], list_num[start]
            self.find_perm(start+1,list_num)
            list_num[start],list_num[i] = list_num[i], list_num[start]


    def calculate(self,list_num):
        res = 0
        for i in xrange(len(list_num)):
            if i == 0:
                res += list_num[i]

            else:
                res += abs(list_num[i] - list_num[i-1])
        return res


for i in xrange(1,11):
    a = Solution(i)
    print a.permutation()
