class Solution:
    def isPalindrome(self, s: str) -> bool:

        str1 = s.lower()

        left = 0
        right = len(str1) - 1

        while left < right:

            if not str1[left].isalnum():
                left += 1

            elif not str1[right].isalnum():
                right -= 1

            else:
                if str1[left] != str1[right]:
                    return False

                left += 1
                right -= 1

        return True