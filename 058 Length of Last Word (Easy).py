'''
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

Constraints:
1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
'''

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s.replace(" ", "") == s:
            return len(s)
        else: 
            s = list(s)
            word_count = 0
            while  s[-1] == " ":
                s.pop()
            s = s[::-1]
            for char in s:
                if char == " ":
                    return word_count
                else:
                    word_count += 1
        return len(s)
    
'''
solution code is too complex however 
the runtime is basically zero beating 100 percent of complexity
the space complexity is o(1) which is nothing to be concerned about however its worse 
than most leetcode users

overall good solution only one problem is that too many edge cases had to be delth with
im sure there was a more syntax-style efficent way to deal with this
'''