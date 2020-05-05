# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"

class Solution:
      def longestPalindrome(self, s: str) -> str:
        if len(s) > 1:
            maxSlice = (0, 0)

            def palindromeSlice(a, b):
                while 0 <= a <= b < len(s) and s[a] == s[b]:
                    a -= 1
                    b += 1
                return (a+1, b-1)

            for i in range(len(s)):
                oddSlice = palindromeSlice(i, i)
                evenSlice = palindromeSlice(i, i+1)
                maxSlice = max([maxSlice, oddSlice, evenSlice],
                               key=lambda x: x[1] - x[0])

            return s[maxSlice[0]: maxSlice[1]+1]

        return s