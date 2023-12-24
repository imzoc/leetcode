class Solution:
    # access_times looks like this: [["name", time], ["name", time]]
    def findHighAccessEmployees(self, access_times: list) -> list:
        l = dict()
        for a in access_times:
            if a[0] not in l.keys():
                l[a[0]] = [int(a[1])]
            else:
                l[a[0]].append(int(a[1]))

        high_access_list = set()
        for name, times in l.items():
            times.sort()
            for u in range(len(times) - 2):
                if times[u] + 100 > times[u+2]:
                    high_access_list.add(name)

        return list(high_access_list)

'''
from icecream import ic
solution = Solution()
ic(solution.findHighAccessEmployees([["a","0549"],["b","0457"],["a","0532"],["a","0621"],["b","0540"]]))
ic(solution.findHighAccessEmployees([["d","0002"],["c","0808"],["c","0829"],["e","0215"],["d","1508"],["d","1444"],["d","1410"],["c","0809"]]))
ic(solution.findHighAccessEmployees([["cd","1025"],["ab","1025"],["cd","1046"],["cd","1055"],["ab","1124"],["ab","1120"]]))
'''