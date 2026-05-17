class Solution:
    def countAndSay(self, n):

        result = "1"

        for i in range(n - 1):

            temp = ""
            count = 1

            for j in range(len(result)):

                # count same digits
                if j + 1 < len(result) and result[j] == result[j + 1]:
                    count += 1

                else:
                    temp += str(count) + result[j]
                    count = 1

            result = temp

        return result