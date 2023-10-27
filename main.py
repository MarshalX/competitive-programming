import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        chars = list(s)
        valid_chars = set(string.ascii_lowercase + string.digits)

        s1 = ''
        s2 = ''
        for char in chars:
            if char in valid_chars:
                s1 += char
                s2 = char + s2

        return s1 == s2


if __name__ == '__main__':
    cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        " ",
    ]

    for case in cases:
        print(Solution().isPalindrome(case))
