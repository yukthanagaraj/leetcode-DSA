# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s):
        
        # If it's just a single integer
        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []
        num = ""
        negative = False

        for ch in s:

            if ch == '-':
                negative = True

            elif ch.isdigit():
                num += ch

            elif ch == '[':
                stack.append(NestedInteger())

            elif ch in ',]':
                
                if num:
                    value = int(num)
                    if negative:
                        value = -value

                    stack[-1].add(NestedInteger(value))

                num = ""
                negative = False

                if ch == ']' and len(stack) > 1:
                    top = stack.pop()
                    stack[-1].add(top)

        return stack[0]