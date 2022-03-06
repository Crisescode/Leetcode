

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m, res = len(s), len(p), []
        if n < m:
            return res

        s_cnt = [0] * 26
        p_cnt = [0] * 26
        for i in range(m):
            s_cnt[ord(s[i]) - ord('a')] += 1
            p_cnt[ord(p[i]) - ord('a')] += 1

        # print(s_cnt)
        # print(p_cnt)

        if s_cnt == p_cnt:
            res.append(0)

        for i in range(m, n):
            s_cnt[ord(s[i - m]) - ord('a')] -= 1
            s_cnt[ord(s[i]) - ord('a')] += 1
            print("s_cnt", s_cnt)
            if s_cnt == p_cnt:
                res.append(i - m + 1)

        return res


if __name__ == "__main__":
    print(Solution().findAnagrams("cbaebabacd", "abc"))
