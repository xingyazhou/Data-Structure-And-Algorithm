# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 22:12:18 2020

359. Logger Rate Limiter (Easy)
Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not printed in the last 10 seconds.

Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.
It is possible that several messages arrive roughly at the same time.

Example:

Logger logger = new Logger();

// logging string "foo" at timestamp 1
logger.shouldPrintMessage(1, "foo"); returns true; 

// logging string "bar" at timestamp 2
logger.shouldPrintMessage(2,"bar"); returns true;

// logging string "foo" at timestamp 3
logger.shouldPrintMessage(3,"foo"); returns false;

// logging string "bar" at timestamp 8
logger.shouldPrintMessage(8,"bar"); returns false;

// logging string "foo" at timestamp 10
logger.shouldPrintMessage(10,"foo"); returns false;

// logging string "foo" at timestamp 11
logger.shouldPrintMessage(11,"foo"); returns true;

@author: xingya

"""

import unittest

class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.d:
            self.d[message] = timestamp
            return True
        else:
            if timestamp - self.d[message]  >= 10:
                self.d[message] = timestamp
                return True
            else:
                return False
            
class Test(unittest.TestCase):
    def testShouldPrintMessage(self):
        print("\n\nTesting ShouldPrintMessage ...")
        
        logger = Logger()
        output1 = logger.shouldPrintMessage(1, "foo")
        output2 = logger.shouldPrintMessage(2, "bar")
        output3 = logger.shouldPrintMessage(3, "foo")
        output4 = logger.shouldPrintMessage(8, "bar")
        output5 = logger.shouldPrintMessage(10, "foo")
        output6 = logger.shouldPrintMessage(11, "foo")
        
        print(output1, output2, output3, output4, output5, output6)
        
        assert output1 == True
        assert output2 == True
        assert output3 == False
        assert output4 == False
        assert output5 == False
        assert output6 == True

        
if __name__ == '__main__':
    unittest.main()           
        
"""
Runtime: 132 ms, faster than 98.13% of Python3 online submissions for Logger Rate Limiter.
Memory Usage: 19.9 MB, less than 99.78% of Python3 online submissions for Logger Rate Limiter.
"""