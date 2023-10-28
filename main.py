class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = list(s.lower())
        chars_count = len(chars)

        p1 = 0
        p2 = chars_count - 1
        while p1 < chars_count and p2 > 0 and p1 < p2:
            s1, s2 = chars[p1], chars[p2]

            if not s1.isalnum():
                p1 += 1
                continue

            if not s2.isalnum():
                p2 -= 1
                continue

            if s1 != s2:
                return False

            p1 += 1
            p2 -= 1

        return True


if __name__ == '__main__':
    cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        " ",
        "aa",
    ]

    for case in cases:
        print(Solution().isPalindrome(case))
