import ast

class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        dp = [0] * len(questions)
        for i in range(len(questions) - 1, -1, -1):
            index = i + questions[i][1] + 1
            if index < len(questions):
                dp[i] = dp[index] + questions[i][0]
            else:
                dp[i] = questions[i][0]
            if i < len(questions) - 1:
                dp[i] = max(dp[i + 1], dp[i])
        print(dp[0])

obj = Solution()
questions = ast.literal_eval(input("Enter list of numbers in list format: e.g [[3, 2], [4, 3], [4, 4], [2, 5]] "))
obj.mostPoints(questions)

        
