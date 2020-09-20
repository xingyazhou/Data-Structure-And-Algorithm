# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 20:52:03 2020

937. Reorder Data in Log Files (Easy)
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

 

Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
 

Constraints:

0 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] is guaranteed to have an identifier, and a word after the identifier.

@author: xingya

"""

from collections import defaultdict

class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        
        d = defaultdict(list)
        l1 =[]
        l2 = []
        
        for log in logs:
            
            ind = log.index(" ")
            
            if log[ind+1:ind+2] >= 'a' and log[ind+1:ind+2] <='z':
                # letter-logs                       
                key = log[ind+1:]
                d[key].append(log[:ind])
              
            else:
                # digit-logs
                l2.append(log)
        
        d = sorted(d.items(), key = lambda kv: kv[0]) 
   
        for x in d:
            # same letter-log with different id
            if len(x[1]) > 1:
               # for the same letter-log, sorted the id
               x[1].sort()
               for y in x[1]:
                   l1.append(y + " " + x[0])
                   
            else:
                l1.append(x[1][0] + " " + x[0])
           
        return (l1 + l2)

            

        
logs =["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]
s = Solution()     
print(s.reorderLogFiles(logs))

# Output
# ['a2 act car', 'g1 act car', 'a8 act zoo', 'ab1 off key dog', 'a1 9 2 3 1', 'zo4 4 7']


"""
Runtime: 16 ms, faster than 99.40% of Python online submissions for Reorder Data in Log Files.
Memory Usage: 12.8 MB, less than 71.93% of Python online submissions for Reorder Data in Log Files.
"""

     
