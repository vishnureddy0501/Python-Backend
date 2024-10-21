def isPalindrome(s):
    pass
def longestPalindromicSubstring(s):
    for i in range(0,len(s)):
        for j in range(i+1, len(s) + 1):
            str = s[i:j]
            isPalindrome(str)
longestPalindromicSubstring("aabb")