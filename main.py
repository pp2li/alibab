class Solution(object):
    def game(self, guess, answer):
        """
        :type guess: List[int]
        :type answer: List[int]
        :rtype: int
        """
        m=0
        count = 0
        while m<3:
            if guess[m] == answer[m]:
                count+=1
            m+=1
        return count
