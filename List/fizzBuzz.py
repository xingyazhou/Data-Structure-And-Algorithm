# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 21:10:04 2020

412. Fizz Buzz (Easy)

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

@author: xingya
"""

import unittest

class Solution:
    def fizzBuzz(self, n: int):
        
        output = []
        
        for i in range(1, n+1):

            if i % 3 == 0 and i % 5 == 0:
                output.append('FizzBuzz')
                
            elif i % 3 == 0:
                output.append('Fizz')
                
            elif i % 5 == 0:
                output.append('Buzz')
                
            else:
                output.append(str(i))
                
        return output
        

class Test(unittest.TestCase):
    print("\n\nTesting fizzBuzz ...")
    n = 15
    expected = [
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
    ]
   
    s = Solution()
    output = s.fizzBuzz(n)
    
    print(output)
    assert output == expected
    
if __name__ == '__main__':
    unittest.main()


"""
Runtime: 36 ms, faster than 92.06% of Python3 online submissions for Fizz Buzz.
Memory Usage: 15 MB, less than 99.51% of Python3 online submissions for Fizz Buzz.
"""