class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        less = -1

        v1 = version1.split('.')
        v2 = version2.split('.')

        if len(v1) > len(v2):
            v1, v2 = v2, v1
            less = 1

        for i in range(len(v1)):
            if int(v1[i]) < int(v2[i]):
                return less
            if int(v1[i]) > int(v2[i]):
                return -less

        for i in range(len(v1), len(v2)):
            if int(v2[i]) > 0:
                return less

        return 0


def test():
    print(Solution().compareVersion(version1="1.01", version2="1.001"))
    print(Solution().compareVersion(version1="1.0", version2="1.0.0"))
    print(Solution().compareVersion(version1="0.1", version2="1.1"))
    print(Solution().compareVersion(version1="1.1.1.19.0.0", version2="1.1.1.19.0.0.0"))


if __name__ == '__main__':
    test()
