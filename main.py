class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = list(s.lower())
        l = len(chars)

        p1 = 0
        p2 = l - 1
        while p1 < l and p2 > 0 and p1 < p2:
            n1 = ord(chars[p1])
            if (n1 < 97 or n1 > 122) and (n1 < 48 or n1 > 57):
                p1 += 1
                continue

            n2 = ord(chars[p2])
            if (n2 < 97 or n2 > 122) and (n2 < 48 or n2 > 57):
                p2 -= 1
                continue

            if chars[p1] != chars[p2]:
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
