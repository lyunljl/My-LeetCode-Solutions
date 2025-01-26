'''
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

s and t consist of lowercase English letters.


Recommended Time & Space Complexity
You should aim for a solution with O(n + m) time and O(1) space, where n is the length of the string s and m is the length of the string t.


Hint 1
A brute force solution would be to sort the given strings and check for their equality. This would be an O(nlogn + mlogm) solution. 
Though this solution is acceptable, can you think of a better way without sorting the given strings?


Hint 2
By the definition of the anagram, we can rearrange the characters. Does the order of characters matter in both the strings? Then what matters?


Hint 3
We can just consider maintaining the frequency of each character. We can do this by having two separate hash tables for the two strings. 
Then, we can check whether the frequency of each character in string s is equal to that in string t and vice versa.
'''
# LEETCODE 242
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            s_new = list(s)
            t_new = list(t)
            s_new.sort() #O(nlog(n))
            t_new.sort() #O(mlog(m))
            if s_new == t_new:
                return True
            else:
                return False
            
# solution is acceptable with O(nlog(n) + mlog(m)) time. we :

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            return sorted(s) == sorted(t)
# solution is acceptable with O(nlog(n) + mlog(m)) time. 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS = {}
        countT = {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
    
# solution is acceptable with O(n + m) time. and space of o(1)