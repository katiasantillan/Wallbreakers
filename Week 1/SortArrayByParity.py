class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even = [i for i in A if i%2 == 0]
        odd = [i for i in A if i%2 != 0]

        return(even+odd)